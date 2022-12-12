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

    def process_udemy_details_data(self, course_data):
        target_data = course_data[0].get('details', {}).get('requirements', "")
        target_data = json.loads(target_data)
        scalped = scalpl.Cut(target_data)
        requirements = scalped.get('serverSideProps.course.prerequisites')
        other_details = self.get_other_details(target_data)
        course_data[0]['details']['requirements'] = requirements
        course_data[0]['details']['other_details'] = other_details
        return course_data

    @staticmethod
    def get_other_details(self, other_data):
        other_details = []
        data = scalpl.Cut(other_data)
        instruction_level = data.get('serverSideProps.course.instructionalLevel')
        instructors = data.get('serverSideProps.course.instructors.instructors_info')
        number_of_reviews = data.get('serverSideProps.course.numReviews')
        number_of_students = data.get('serverSideProps.course.numStudents')
        objectives = data.get('serverSideProps.course.objectives')
        rating = data.get('serverSideProps.course.rating')
        target_audiences = data.get('serverSideProps.course.targetAudiences')
        other_details.append({'instruction_level': instruction_level, 'instructors': instructors,
                              'number_of_reviews': number_of_reviews, 'number_of_students':number_of_students,
                              'objectives': objectives, 'rating': rating, 'target_audiences': target_audiences})
        return other_details
