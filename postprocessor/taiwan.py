from framework.scraper_engine.handlers.post_processor.interface import IPostProcessor
from framework.scraper_engine.types import *


class TW104MetadataPostProcessor(IPostProcessor):
    """
        Process metadata i.e. city and job_category details.
    """
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        meta_data: list = output.data[0]
        if not meta_data:
            self.extracted_data.data = []
        else:
            processed_data = self.process_metadata(meta_data)
            self.extracted_data.data = processed_data

    def process_metadata(self, meta_data):
        job_cat_list = meta_data.get("job_cat", [])
        area_list = meta_data.get("area", [])
        job_categories = self.get_job_categories(job_cat_list)
        areas = self.get_areas(area_list)
        final_data = self.get_final_data(areas, job_categories)
        return final_data

    @staticmethod
    def get_job_categories(data):
        """
            returns all job category code list
        """
        if not data:
            return []
        job_category_list = []
        for main_job in data:
            for job in main_job.get("jobcats"):
                job_category_list.append({"job_category_code": job.get('jobcat'), "job_category": job.get('text')})

        return job_category_list

    @staticmethod
    def get_areas(data):
        """
            returns all area codes list
        """
        if not data:
            return []
        area_list = []
        for main_area in data:
            for area in main_area.get('area'):
                area_list.append({"city": area.get('text'), "city_code": area.get('area')})
        return area_list

    @staticmethod
    def get_final_data(areas, job_categories):
        """
            returns cartesian product of area codes and job_category_codes list
        """
        if not areas or not job_categories:
            return []
        final_data = [{"city_code": area.get('city_code'), "city": area.get('city'), "job_category": job.get('job_category'), "job_category_code": job.get('job_category_code'), "job_url": f"https://www.104.com.tw/jb/category/?cat=2&no={job.get('job_category_code')}&area={area.get('city_code')}&jobsource=sitemap"} for area in areas for job in job_categories]
        return final_data
