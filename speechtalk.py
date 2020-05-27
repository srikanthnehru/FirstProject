import speech_recognition
import pyaudio
import re

recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("Say Something")
    try:
        for i in range(5):
            audio = recognizer.listen(source)
            print("Google speech recognition thinks you said:")
            words = recognizer.recognize_google(audio)
            matches = re.search("my name is (.*)", words)
            if "hello" in words:
                print("Hello to you too!")
            elif "how are you" in words:
                print("I am well, thanks!")
            elif "goodbye" in words:
                print("Goodbye to you too!")
            elif matches:
                print("Thanks for telling your name ",matches[1])
            else:
                print("Huh?")
    except speech_recognition.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except speech_recognition.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
