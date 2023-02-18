from flask import Flask, request, jsonify
import speech_recognition as sr
import pyttsx3
import openai
from gtts import gTTS
import os

# app = Flask(__name__)

class File(self):
    def __init__(self):
        self
class SpeechRecognizer:
    def __init__(self):
        self.r = sr.Recognizer()

    def recognize_speech(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            audio = self.r.record(source)
        text = self.r.recognize_google(audio)
        return text


class TextToSpeech:
    def __init__(self):
        self.language = 'en'

    def convert_to_audio(self, text):
        tts = gTTS(text=text, lang=self.language)
        audio_file = 'response.mp3'
        tts.save(audio_file)
        return audio_file


class ChatGPT:
    def __init__(self):
        self.api_key = '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'
        openai.api_key = self.api_key
        self.model_engine = 'text-davinci-002'

    def generate_response(self, input_text):
        response = openai.Completion.create(
            engine=self.model_engine,
            prompt=input_text,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()



# @app.route('/voice-command', methods=['POST'])
# def voice_command():
#     file = request.files['file']
#     audio_file = 'command.wav'
#     file.save(audio_file)
#     text = speech_recognizer.recognize_speech(audio_file)
#     response_text = chat_gpt.generate_response(text)
#     response_audio_file = text_to_speech.convert_to_audio(response_text)
#     return jsonify({'response_audio_file': response_audio_file})


def main():
    r = sr.Recognizer()
    speech_recognizer = SpeechRecognizer()
    text_to_speech = TextToSpeech()
    chat_gpt = ChatGPT()
    engine = pyttsx3.init()

# set the voice and rate
    engine.setProperty("voice", "english-us")
    engine.setProperty("rate", 150)

    # get the text to be spoken
    # text = "Hello, this is an example of how to play audio directly from text in Python."

    # play the audio
    

# use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source, phrase_time_limit=10)

    # save the audio to a WAV file
    with open("audio.wav", "wb") as f:
        f.write(audio.get_wav_data())

# recognize speech from the audio
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        result = chat_gpt.generate_response(text)
        print(f"here the result of GPT => {result}")
        engine.say(result)
        audio = text_to_speech.convert_to_audio(result)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print(
            f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == '__main__':
    # app.run()
    main()
