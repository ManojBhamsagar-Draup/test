import re


def get_output_data(response, **kwargs):
    if not response:
        return ""
    pattern = "(var APOLLO_STATE=)(.*)(;)"
    doc = re.split(pattern, response)[2]
    data = '{"data":[{"output":' + doc + '}]}'
    return data

from framework.scraper_engine.handlers.post_processor.interface import IPostProcessor
from framework.scraper_engine.types import *


class XingProfilesPostProcess(IPostProcessor):
    """
        Post processor used to get profiles details from scraped data.
    """
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        data: list = output.data
        input_params = kwargs["input_parameters"]
        if not data:
            self.extracted_data.data = []
        else:
            self.extracted_data.data = self.get_profile_data(data, input_params)

    def get_profile_data(self, data, input_params):
        if not data:
            return []
        final_data = dict()
        profile_data = data[0].get('profile_data', {})
        for key, values in profile_data.items():
            if "XingId" in key:
                profile_name, location, profile_image, job_title = self.get_basic_profile_details(self, values)
                if profile_name:
                    final_data["profile_name"] = profile_name
                    final_data["location"] = location
                    final_data["detail_url"] = input_params.get('profile_link', '')
                    final_data["image_url"] = profile_image
                    final_data["job_title"] = job_title
            if "ROOT_QUERY" in key:
                work_experience_timeline = None
                education_timeline = None
                languages_info = None
                for field, value in values.items():
                    if "profileWorkExperience" in field:
                        work_experience_timeline = values.get(field, {}).get('collection', [])
                    if "profileEducation" in field:
                        education_timeline = values.get(field, {}).get('education', [])
                    if "profileLanguageSkills" in field:
                        languages_info = values.get(field, {}).get('collection', [])
                work_experience = None
                education = None
                languages = None
                if work_experience_timeline:
                    work_experience = self.get_work_experience(work_experience_timeline)
                if education_timeline:
                    education = self.get_education(education_timeline)
                if languages_info:
                    languages = self.get_languages(languages_info)
                if work_experience or education or languages:
                    final_data["work_experience"] = work_experience
                    final_data["education"] = education
                    final_data["languages"] = languages

        return [final_data]

    @staticmethod
    def get_basic_profile_details(self, data):
        profile_name = ""
        location = ""
        profile_image = ""
        job_title = ""

        if data:
            profile_name = f"{data.get('firstName', '').strip()} {data.get('lastName', '').strip()}"
        if data.get('location'):
            location = f"{data.get('location').get('city', '')} {data.get('location').get('country').get('localizationValue', '')}"
        if data.get('profileImage({"size":"SQUARE_256"})', []):
            profile_image = data.get('profileImage({"size":"SQUARE_256"})', [])[0].get('url', '')
        if data.get('occupations', []):
            job_title = data.get('occupations')[0].get('summary', '')
        return profile_name, location, profile_image, job_title

    @staticmethod
    def get_work_experience(work_experience_timeline):
        if not work_experience_timeline:
            return []
        work_experience = []
        for doc in work_experience_timeline:
            work_experience.append({"job_title": doc.get('jobTitle', ''),
                                    "start_date": doc.get('beginDate', ''),
                                    "end_date": doc.get('endDate', ''),
                                    "company_name": doc.get('companyName', ''),
                                    "is_current_company": doc.get('currentCompany', ''),
                                    "duration": doc.get('localizedTimeString', '').replace("*", ""),
                                    "work_summary": doc.get('companyNotes', '')})
        return work_experience

    @staticmethod
    def get_education(education_timeline):
        if not education_timeline:
            return []
        education = []
        for doc in education_timeline:
            education.append({"school_name": doc.get('schoolName', ''),
                              "start_date": doc.get('beginDate', ''),
                              "end_date": doc.get('endDate', ''),
                              "degree_name": doc.get('degree', ''),
                              "subject": doc.get('subject', ''),
                              "duration": doc.get('localizedTimeString', '').replace("*", "")})
        return education

    @staticmethod
    def get_languages(languages_list):
        if not languages_list:
            return []
        languages = []
        for doc in languages_list:
            languages.append({"language": doc.get('displayLanguage', ''),
                              "language_proficiency": doc.get('skillLevelId', '')})
        return languages
