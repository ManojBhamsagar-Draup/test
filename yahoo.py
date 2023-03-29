from framework.scraper_engine.handlers.post_processor.interface import IPostProcessor
from framework.scraper_engine.types import *
from system.logger.factory import LoggerFactory

logger = LoggerFactory.create(name='YahooFinance')
logger_context = "YahooFinance"


class YahooFinancialsOutputTransformer(IPostProcessor):
    """
        Postprocessor to retrieve yahoo financial data.
    """
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        data = output.data
        try:
            final_output = self.yahoo_financials(data, output.main_response_props.get('response_props', {}).get('url'))
            self.extracted_data.data = final_output
        except Exception as e:
            logger._warning_mixin(msg=f"post processing failed for yahoo financials with exception: {e}",
                                  context=self)

    @staticmethod
    def yahoo_financials(data, url):
        if not data:
            return []
        data = data[0] if data else {}
        ticker = url.split("/")[-3].upper()
        finDictionary = {'ticker': ticker, 'yahoo_financial_link': url}
        company_price_details = YahooFinancialsOutputTransformer.get_company_price_details(data.get('company_price_details'))
        finDictionary['company_price_details'] = company_price_details
        finDictionary['company_name'] = data.get('company_name')
        finDictionary['company_currency_details'] = data.get('company_currency_details')
        finDictionary['quote_market_notice'] = data.get('quote_market_notice')
        return [finDictionary]

    @staticmethod
    def get_company_price_details(company_prices):
        company_price_details = None
        try:
            regular_price = company_prices[0].get('regular_price')
            market_change = company_prices[0].get('market_change')
            change_percentage = company_prices[0].get('change_percentage')
            company_price_details = f"{regular_price} {market_change} {change_percentage}"
        except Exception as e:
            logger._exception_mixin(msg=f"cannot get company_price_details: {repr(e)}", context=logger_context)
        return company_price_details if company_price_details else ""


class YahooFinancialDataTransformer(IPostProcessor):
    """
        Postprocessor to retrieve yahoo financial data.
    """
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        fin_data: list = output.data
        ticker = kwargs.get('input_parameters').get('ticker')
        if fin_data:
            self.extracted_data.data = self.process_yahoo_financial_data(fin_data, ticker)
        else:
            self.extracted_data.data = []

    def process_yahoo_financial_data(self, fin_data, ticker):
        finDictionary = {'ticker': ticker}
        final_data = self.get_financial_data(fin_data)
        finDictionary['data'] = final_data
        return [finDictionary]

    @staticmethod
    def get_financial_data(financial_data):
        data = dict()
        for doc in financial_data:
            fin_data = doc.get('fin_data')
            fin_type = fin_data.get('meta').get('type')[0]
            data[fin_type] = fin_data.get(fin_type, [])
        return data
