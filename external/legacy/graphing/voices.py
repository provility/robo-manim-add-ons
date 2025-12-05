from enum import Enum

class VoiceConfig(Enum):
    TARA = ("Tara", "P7vsEyTOpZ6YUTulin8m")
    AMRIT =("Amritanshu Professional voice", "1qZOLVpd1TVic43MSkFY")
    RIYA = ("Riya", "vYENaCJHl4vFKNDYPr8y")
    ARJUN = ("Arjun", "xc8cUCvu6d9f4tV51JqT")
        
    def __init__(self, voice_name, voice_id):
        self.voice_name = voice_name
        self.voice_id = voice_id
