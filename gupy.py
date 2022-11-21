from framework.scraper_engine.handlers.post_processor.interface import IPostProcessor
from framework.scraper_engine.types import *


class GupyPostProcessor(IPostProcessor):
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        job_data: list = output.data
        self.extracted_data.data = self.process_gupy_data(job_data)

    @staticmethod
    def process_gupy_data(job_data):
        for item in job_data:
            if item["job_location"]:
                continue
            if not item["state"] and item["is_remote_work"]:
                item["job_location"] = "remote"
            elif item["state"]:
                item["job_location"] = item["state"]
        return job_data
