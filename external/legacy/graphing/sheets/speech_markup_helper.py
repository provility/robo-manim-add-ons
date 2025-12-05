class SpeechMarkupHelper:
    def slow_text(self, text):
        """Wraps text in SSML to make it spoken slowly."""
        return f"<speak><prosody rate='slow'>{text}</prosody></speak>"
        


    def fast_text(self, text):
        """Wraps text in SSML to make it spoken quickly."""
        return f"<speak><prosody rate='fast'>{text}</prosody></speak>"

    def emphasize_text(self, text, level="strong"):
        """Wraps text in SSML to add emphasis. Level can be 'strong', 'moderate', or 'reduced'."""
        return f"<speak><emphasis level='{level}'>{text}</emphasis></speak>"

    def pitch_adjusted_text(self, text, pitch="high"):
        """Wraps text in SSML to adjust pitch. Options include 'high', 'low', '+10%', '-10%'."""
        return f"<speak><prosody pitch='{pitch}'>{text}</prosody></speak>"

    def pause_after_text(self, text, time="500ms"):
        """Wraps text in SSML and adds a pause after the text. Time can be in ms (e.g., '500ms')."""
        return f"<speak>{text}<break time='{time}'/></speak>"

    def spell_out_as_characters(self, text):
        """Wraps text in SSML to spell out each character individually."""
        return f"<speak><say-as interpret-as='characters'>{text}</say-as></speak>"

    def interpret_as_fraction(self, text):
        """Wraps text in SSML to interpret it as a fraction."""
        return f"<speak><say-as interpret-as='fraction'>{text}</say-as></speak>"


