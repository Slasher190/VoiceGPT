
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