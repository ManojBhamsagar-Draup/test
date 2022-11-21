from framework.scraper_engine.handlers.post_processor.interface import IPostProcessor
from framework.scraper_engine.types import *


class LevelsLevelPostProcessor(IPostProcessor):
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        levels_data: list = output.data
        company_name = kwargs.get('input_parameters', {}).get('company_name')
        job_family = kwargs.get('input_parameters', {}).get('job_family')
        self.extracted_data.data = self.process_levels_data(levels_data, company_name, job_family)

    @staticmethod
    def process_levels_data(levels_data, company_name, job_family):
        final_data = []
        for level in levels_data:
            final_data.append({"company_name": company_name, "job_family": job_family, "level": level.get("level", ""), "job_title": level.get("job_title", ""), "link": f"/companies/{company_name}/salaries/{job_family}/levels/{level.get('level', '')}"})
        return final_data
