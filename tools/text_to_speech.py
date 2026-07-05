from gtts import gTTS
import os


def text_to_speech(text):

    tts = gTTS(text=text, lang="en")

    output_path = "voice_output.mp3"

    tts.save(output_path)

    return output_path