from framework.scraper_engine.handlers.post_processor.interface import IPostProcessor
from framework.scraper_engine.types import *


class CorporateTaxPostProcessor(IPostProcessor):
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        data = output.data
        self.extracted_data.data = self.process_data(data)

    @staticmethod
    def process_data(data):
        year = None
        scraped_data = None
        if data:
            year = data[0].get("year", "")
            scraped_data = data[0].get("data", [])
        if year and scraped_data:
            for ele in scraped_data:
                ele["corporate_tax_rate_" + year] = ele.pop("corporate_tax_rate")
            data[0].pop('year')
            data[0]['data'] = scraped_data
        return scraped_data
