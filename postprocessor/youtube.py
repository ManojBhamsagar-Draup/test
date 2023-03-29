from framework.scraper_engine.handlers.post_processor.interface import IPostProcessor
from framework.scraper_engine.types import *


class YoutubeChannelPostProcess(IPostProcessor):
    """
        Post processor used to get playlist id, channel_url from channel_id
    """
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        data: list = output.data
        if not data:
            self.extracted_data.data = []
        else:
            self.extracted_data.data = self.get_channel_data(data)

    @staticmethod
    def get_channel_data(data):
        channel_id = data[0].get('channel_id', '')
        if not channel_id:
            return []
        playlist_id = "UU" + channel_id[2:]
        youtube_company_url = "https://www.youtube.com/channel/" + channel_id
        return [{"channel_id": channel_id, "playlist_id": playlist_id, "youtube_company_url": youtube_company_url}]


class YoutubeDetailsPostProcess(IPostProcessor):
    """
        post processor used to get video id
    """
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        data: list = output.data
        if not data:
            self.extracted_data.data = []
        else:
            self.extracted_data.data = self.get_channel_data(data)

    @staticmethod
    def get_channel_data(data):
        video_id = data[0].pop('video_id')
        if not video_id:
            return []
        final_data = [{"video_id": video_id, "video_details": data[0]}]
        return final_data
