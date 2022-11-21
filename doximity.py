from framework.scraper_engine.handlers.post_processor.interface import IPostProcessor
from framework.scraper_engine.types import *


class DoximitySpecialityPostProcessor(IPostProcessor):
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        directory_link = kwargs.get("input_parameters", {}).get("directory_link", "")
        data: list = output.data[0].get("data", [])
        directory_name = output.data[0].get("directory_name", "")
        self.extracted_data.data = self.process_data(data, directory_name, directory_link)

    @staticmethod
    def process_data(data, directory_name, directory_link):
        if not data or not directory_name or not directory_link:
            return
        for doc in data:
            doc["directory_name"] = directory_name
            doc["directory_link"] = directory_link
        return data


class DoximityPersonsPostProcessor(IPostProcessor):
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        speciality_link = kwargs.get("input_parameters", {}).get("speciality_link", "")
        directory_name = output.data[0].get("directory_name", "")
        speciality_name = output.data[0].get("speciality_name", "")
        data: list = output.data[0].get("data", [])
        self.extracted_data.data = self.process_data(data, directory_name, speciality_name, speciality_link)

    @staticmethod
    def process_data(data, directory_name, speciality_name, speciality_link):
        if not data or not directory_name or not speciality_name or not speciality_link:
            return
        for doc in data:
            doc["directory_name"] = directory_name
            doc["speciality_name"] = speciality_name
            doc["speciality_link"] = speciality_link
        return data
