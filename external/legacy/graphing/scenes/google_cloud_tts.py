from google.cloud import texttospeech
from manim_voiceover.services.base import SpeechService

class GoogleCloudTTSService(SpeechService):
    def __init__(self, credentials_path, language_code='en-US', 
                 voice_name='en-US-Standard-C', **kwargs):
        super().__init__(**kwargs)
        self.client = texttospeech.TextToSpeechClient.from_service_account_file(credentials_path)
        self.language_code = language_code
        self.voice_name = voice_name

    def generate_from_text(self, text, **kwargs):
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code=self.language_code,
            name=self.voice_name
        )
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
        response = self.client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )
        return response.audio_content
