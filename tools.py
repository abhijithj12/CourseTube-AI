from crewai.tools import tool
from pytubefix import YouTube,Playlist
from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp
from faster_whisper import WhisperModel
import os


@tool
def get_transcript(video_url: str) -> str:
    """
    Fetches transcript from a single YouTube video.
    Works even if the video belongs to a playlist.
    Processes ONLY the selected video.
    """
    try:
        yt = YouTube(video_url)
        video_id = yt.video_id
        transcript_list = YouTubeTranscriptApi().fetch(video_id)
        transcript = ' '.join([d.text for d in transcript_list])
        return transcript

    except Exception as e:
        return f"Error: {str(e)}"


@tool
def get_metadata(video_url: str) -> str:
    """
    Extracts metadata from a YouTube video.
    If the video belongs to a playlist,only the selected video is processed.
    Use this tool to get information about the video before processing.
    """
   
    try:
        yt=YouTube(video_url)
        title=yt.title
        channel_name=yt.author
        duration=round(yt.length/60)
        metadata=f"""
        Title: {title}
        Channel Name: {channel_name}
        Duration: {duration} minutes
        """
        return metadata

    except Exception as e:
        return f"Error: {str(e)}"

@tool
def transcribe_with_wisper(video_url:str) -> str:
    """
    Only use this tool when get_youtube_transcript tool fails or returns an error.
    Downloads audio from a YouTube video and transcribes it using Whisper.
    This works on videos that have no captions or subtitles available.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.mp3',
        'quiet': True,
        'noplaylist': True
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        model = WhisperModel("small", device="cpu", compute_type="int8")
        segments, info = model.transcribe("audio.mp3")
        transcript = " ".join([segment.text for segment in segments])
        os.remove("audio.mp3")

        return transcript

    except Exception as e:
        return f"Error: {str(e)}"