import speech_recognition
import pyaudio

recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("Say Something")
    audio = recognizer.listen(source)


try:
    print("Google speech recognition thinks you said:")
    print(recognizer.recognize_google(audio))
except speech_recognition.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except speech_recognition.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
