from framework.scraper_engine.handlers.post_processor.interface import IPostProcessor
from framework.scraper_engine.types import *
from utils.common_helper_functions import check_domain_match
from system.logger.factory import LoggerFactory
from fuzzywuzzy import fuzz

logger = LoggerFactory.create(name='CompanyNode')
logger_context = "CompanyNode"


class IndeedCompanyNode(IPostProcessor):
    """
        Postprocessor to check Indeed domain url.
    """
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        data = output.data
        input_params = kwargs['input_parameters']
        try:
            final_output = self.process_indeed_company(data, input_params)
            self.extracted_data.data = final_output
        except Exception as e:
            logger._warning_mixin(msg=f"post processing failed for Indeed company with exception: {e}",
                                  context=self)

    @staticmethod
    def process_indeed_company(data, input_params):
        if not data:
            return []
        data = data[0] if data else {}
        indeed_company_name = data.get('indeed_company_name', '')
        indeed_company_url = input_params.get('visit_link', '')
        indeed_domain_url = data.get('indeed_domain_url', '')
        rank = input_params.get('rank', 1)
        actual_company_name = input_params.get('company_name', '')
        actual_domain_url = input_params.get('domain_url', '')
        domain_match = check_domain_match(indeed_domain_url, actual_domain_url)
        company_name_match_percentage = 100
        if rank > 1:
            company_name_match_percentage = fuzz.ratio(actual_company_name, indeed_company_name)
        final_data = []
        if domain_match and (company_name_match_percentage >= 80):
            final_data.append({'indeed_company_name': indeed_company_name,
                               'indeed_company_url': indeed_company_url,
                               'company_name': actual_company_name,
                               'domain_url': actual_domain_url})
        return final_data if final_data else []


class CrunchbaseCompanyNode(IPostProcessor):
    """
        Postprocessor to check Crunchbase domain url.
    """
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        data = output.data
        input_params = kwargs['input_parameters']
        try:
            final_output = self.process_crunchbase_company(data, input_params)
            self.extracted_data.data = final_output
        except Exception as e:
            logger._warning_mixin(msg=f"post processing failed for Crunchbase company with exception: {e}",
                                  context=self)

    def process_crunchbase_company(self, data, input_params):
        if not data:
            return []
        data = data[0] if data else {}
        crunchbase_company_name = data.get('crunchbase_company_name', '')
        crunchbase_company_url = data.get('crunchbase_company_url', '')
        short_description = data.get('short_description', '')
        company_founded = data.get('company_founded', '')
        locations = data.get('hq_location', '')
        linkedin_url = data.get('linkedin_url', '')
        facebook_url = data.get('facebook_url', '')
        twitter_url = data.get('twitter_url', '')
        company_name = input_params.get('company_name')
        crunchbase_domain_url = data.get('crunchbase_domain_url', '')
        actual_domain_url = input_params.get('domain_url')
        hq_location = self.get_hq_location_string(locations)
        domain_match = check_domain_match(crunchbase_domain_url, actual_domain_url)
        final_data = []
        if domain_match:
            final_data.append({"crunchbase_company_name": crunchbase_company_name,
                               "crunchbase_company_url": crunchbase_company_url,
                               "short_description": short_description,
                               "company_founded": company_founded,
                               "hq_location": hq_location,
                               "linkedin_url": linkedin_url,
                               "facebook_url": facebook_url,
                               "twitter_url": twitter_url,
                               "company_name": company_name,
                               "domain_url": actual_domain_url})
        return final_data if final_data else []

    @staticmethod
    def get_hq_location_string(locations):
        if not locations:
            return ""
        location = locations[0].get('value', '')
        for idx in range(1, len(locations)):
            location += ", " + locations[idx].get('value', '')
        return location


class GlassdoorCompanyNode(IPostProcessor):
    """
        Postprocessor to check Glassdoor domain url.
    """
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        data = output.data
        input_params = kwargs['input_parameters']
        try:
            final_output = self.process_glassdoor_company(data, input_params)
            self.extracted_data.data = final_output
        except Exception as e:
            logger._warning_mixin(msg=f"post processing failed for Glassdoor company with exception: {e}",
                                  context=self)

    @staticmethod
    def process_glassdoor_company(data, input_params):
        if not data:
            return []
        data = data[0] if data else {}
        glassdoor_company_name = data.get('glassdoor_company_name', '')
        glassdoor_company_url = input_params.get('visit_link')
        glassdoor_domain_url = data.get('glassdoor_domain_url', '')
        actual_domain_url = input_params.get('domain_url', '')
        domain_match = check_domain_match(glassdoor_domain_url, actual_domain_url)
        final_data = []
        if domain_match:
            final_data.append({'glassdoor_company_name': glassdoor_company_name,
                               'glassdoor_company_url': glassdoor_company_url,
                               'domain_url': actual_domain_url})
        return final_data if final_data else []


class YahooCompanyNode(IPostProcessor):
    """
        Postprocessor to check Yahoo domain url.
    """
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        data = output.data
        input_params = kwargs['input_parameters']
        try:
            final_output = self.process_yahoo_company(data, input_params)
            self.extracted_data.data = final_output
        except Exception as e:
            logger._warning_mixin(msg=f"post processing failed for Yahoo company with exception: {e}",
                                  context=self)

    @staticmethod
    def process_yahoo_company(data, input_params):
        if not data:
            return []
        yahoo_company_name = input_params.get('yahoo_company_name', '')
        yahoo_ticker = input_params.get('yahoo_ticker', '')
        yahoo_domain_url = data[0].get('yahoo_domain_url', '')
        actual_domain_url = input_params.get('domain_url', '')
        company_name = input_params.get('original_company_name', '')
        domain_check = check_domain_match(yahoo_domain_url, actual_domain_url)
        final_data = []
        if domain_check and yahoo_ticker:
            final_data.append({'company_name': company_name,
                               'domain_url': actual_domain_url,
                               'yahoo_company_name': yahoo_company_name,
                               'yahoo_ticker': yahoo_ticker,
                               'yahoo_financial_url': f"https://finance.yahoo.com/quote/{yahoo_ticker}/financials"

                               })
        return final_data if final_data else []


class AddRank(IPostProcessor):
    """
        Postprocessor to add Rank.
    """
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        data = output.data
        try:
            final_output = self.add_rank(data)
            self.extracted_data.data = final_output
        except Exception as e:
            logger._warning_mixin(msg=f"post processing failed for adding score due to: {e}",
                                  context=self)

    @staticmethod
    def add_rank(data):
        if not data:
            return []
        rank = 1
        for doc in data:
            doc["rank"] = rank
            rank += 1
        return data


class FinhubCompanyNode(IPostProcessor):
    """
        Postprocessor to get Finhub data.
    """
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        data = output.data
        input_params = kwargs['input_parameters']
        try:
            final_output = self.process_finhub_company(data, input_params)
            self.extracted_data.data = final_output
        except Exception as e:
            logger._warning_mixin(msg=f"post processing failed for Finhub company with exception: {e}",
                                  context=self)

    def process_finhub_company(self, data, input_params):
        if not data:
            return []
        ticker = data[0].get('finhub_ticker', '')
        finhub_ticker, stock_exchange = self.get_ticker(ticker)
        finhub_domain_url = data[0].get('finhub_domain_url', '')
        isin = data[0].get('isin', '')
        actual_domain_url = input_params.get('domain_url')
        domain_check = check_domain_match(finhub_domain_url, actual_domain_url)
        final_data = []
        if domain_check and isin:
            final_data.append({'finhub_ticker': finhub_ticker,
                               'finhub_stock_exchange': stock_exchange,
                               'isin': isin,
                               'domain_url': actual_domain_url})
        return final_data if final_data else []

    @staticmethod
    def get_ticker(ticker):
        """
            returns stock exchange and finhub ticker
        """
        if not ticker:
            return ['', '']
        if "." in ticker:
            split_ticker = ticker.split('.')
            return [".".join(split_ticker[0:-1]), split_ticker[-1]]
        else:
            return [ticker, '']


class YahooTickerProcess(IPostProcessor):
    """
        Postprocessor to get Yahoo tickers.
    """
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        data = output.data
        input_params = kwargs['input_parameters']
        try:
            final_output = self.process_yahoo_ticerks(data, input_params)
            self.extracted_data.data = final_output
        except Exception as e:
            logger._warning_mixin(msg=f"post processing failed for Finhub company with exception: {e}",
                                  context=self)

    def process_yahoo_ticerks(self, data, input_params):
        if not data:
            return []
        yahoo_company_name = data[0].get('yahoo_company_name', '')
        yahoo_ticker = data[0].get('yahoo_ticker', '')
        company_node = data[0].get('company_node', '')
        finhub_tickers = self.get_finhub_tickers(yahoo_ticker)
        final_data = []
        for ticker_idx in range(len(finhub_tickers)):
            final_data.append({'yahoo_company_name': yahoo_company_name,
                               'yahoo_ticker': yahoo_ticker,
                               'company_node': company_node,
                               'finhub_ticker': finhub_tickers[ticker_idx],
                               'rank': ticker_idx + 1,
                               })
        return final_data if final_data else []

    @staticmethod
    def get_finhub_tickers(yahoo_ticker):
        if not yahoo_ticker:
            return []
        if yahoo_ticker.startswith('0'):
            return [yahoo_ticker[::], yahoo_ticker[1:]]
        else:
            return [yahoo_ticker]
