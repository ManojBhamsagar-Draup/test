from framework.scraper_engine.handlers.post_processor.interface import IPostProcessor
from framework.scraper_engine.types import *
import scalpl
import json


class UdemyDetailsPostProcessor(IPostProcessor):
    """
        This postprocessor will be used to get requirements of the course
    """
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        course_data: list = output.data
        self.extracted_data.data = self.process_udemy_details_data(course_data)

    @staticmethod
    def process_udemy_details_data(course_data):
        target_data = course_data[0].get('details', {}).get('requirements', "")
        target_data = json.loads(target_data)
        scalped = scalpl.Cut(target_data)
        requirements = scalped.get('serverSideProps').get('course').get('prerequisites')
        course_data[0]['details']['requirements'] = requirements
        return course_data
