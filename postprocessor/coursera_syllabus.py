from framework.scraper_engine.handlers.post_processor.interface import IPostProcessor
from framework.scraper_engine.types import *


class CourseraSyllabusPostProcessor(IPostProcessor):
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        detail_url = output.main_response_props.get('response_props', {}).get('url', "")
        syllabus_data: list = output.data
        self.extracted_data.data = self.process_syllabus_data(syllabus_data, detail_url)

    @staticmethod
    def process_syllabus_data(syllabus_data, detail_url):
        syllabus_data = syllabus_data[0].get('syllabus_details')
        data = []
        count = 1
        for key, value in syllabus_data.items():
            if "material.weeks." in key:
                temp_key = "week " + str(count)
                modules_list = []
                modules = syllabus_data.get(key).get("modules")
                module_count = 1
                for module in modules:
                    temp_module_key = "module " + str(module_count)
                    module_key = module.get("id")
                    temp_doc = dict()
                    temp_doc['name'] = syllabus_data[module_key].get('name')
                    temp_doc['description'] = syllabus_data[module_key].get('description')
                    temp_doc['total_videos'] = syllabus_data[module_key].get('totalVideos')
                    temp_doc['total_quizzes'] = syllabus_data[module_key].get('totalQuizzes')
                    temp_doc['total_duration'] = syllabus_data[module_key].get('totalDuration')
                    temp_doc['total_lecture_duration'] = syllabus_data[module_key].get('totalLectureDuration')
                    temp_doc['total_readings'] = syllabus_data[module_key].get('totalReadings')
                    other_details = []
                    for item in syllabus_data[module_key].get('items'):
                        other_details.append(syllabus_data.get(item.get('id')))
                    temp_doc['other_details'] = other_details
                    modules_list.append({temp_module_key: temp_doc})
                    module_count += 1
                data.append({temp_key: modules_list})
                count += 1
        syllabus_data = []
        syllabus_data.append({"syllabus_details": data, "detail_url": detail_url})
        return syllabus_data
