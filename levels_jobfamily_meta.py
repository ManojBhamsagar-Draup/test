from framework.scraper_engine.handlers.post_processor.interface import IPostProcessor
from framework.scraper_engine.types import *


class LevelsJobFamilyPostProcessor(IPostProcessor):
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        levels_data: list = output.data
        company_name = kwargs.get('input_parameters', {}).get('company_name')
        self.extracted_data.data = self.process_levels_data(levels_data, company_name)

    @staticmethod
    def process_levels_data(levels_data, company_name):
        final_data = []
        for role in levels_data:
            final_data.append({"company_name": company_name, "job_family": role.get("job_family", ""), "link": f"companies/{company_name}/salaries/{role.get('job_family', '')}"})
        return final_data
