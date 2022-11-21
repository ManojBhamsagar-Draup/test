from framework.scraper_engine.handlers.post_processor.interface import IPostProcessor
from framework.scraper_engine.types import *
from system.logger.factory import LoggerFactory
from scalpl import Cut

logger = LoggerFactory.create(name='YahooFinance')


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
        data = data[0] if data else {}
        ticker = url.split("/")[-3].upper()
        finDictionary = {'ticker': ticker, 'company_name': data.get('company_name'), 'yahoo_financial_link': url, 'data': {}}
        data = Cut(data.get('data', {}))
        fin_data = data.get('fin_data')
        if data.get('other_data'):
            fin_data = {**data.get('fin_data'), **data.get('other_data')}
        details = data.get('details', {}).get(data.get('market_source')) if data.get('market_source') else None
        change = data.get('change')
        if change and (change[0] != '-'):
            change = '+{0}'.format(change)
        time = data.get(f'time.{ticker}.regularMarketTime.fmt')
        price_details = '{0} {1} ({2})'.format(data.get('regular_val'), change, data.get('percent_change'))
        quote_market_notice = 'At close: {0}'.format(time)
        currency_details = '{0} - {1} {2}. Currency in {3}'.format(data.get('exchange_name'), data.get('exchange_name'), details, data.get('currency'))
        finDictionary['company_price_details'] = price_details
        finDictionary['company_currency_details'] = currency_details
        finDictionary['quote_market_notice'] = quote_market_notice
        finDictionary['data'] = fin_data
        return [finDictionary]
