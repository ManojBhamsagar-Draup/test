from framework.scraper_engine.handlers.post_processor.interface import IPostProcessor
from framework.scraper_engine.types import *


class NumbeoAllPostProcessor(IPostProcessor):
    """
        post processor adds year, rank and unique id to the scraped data
    """
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        year = kwargs.get('input_parameters', '').get('year_url', '')
        if not year:
            import re
            pattern = "(.*)(jsp\?title=)(.*)"
            main_response_props = self.extracted_data.main_response_props
            year_url = main_response_props.get("response_props", {}).get('url', {})
            year = re.split(pattern=pattern, string=year_url)[3]
        data: list = output.data
        if not data or not year:
            self.extracted_data = []
        self.extracted_data.data = self.process_numbeo_data(data, year)

    @staticmethod
    def process_numbeo_data(data, year):
        for rank in range(len(data)):
            data[rank]['rank'] = rank + 1
            data[rank]['year'] = year
            data[rank]['uid'] = data[rank]['location'] + " " + str(year)
        return data
