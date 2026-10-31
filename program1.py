# voice to speech 
# pip install SpeechRecognition
# for Microphones 
# pip install PyAudio
# for check
# python -m speech_recognition

# check python versions
# py --list 
# set up virtual env
# py -3.11 -m venv .vtt
# .vtt/Scripts/activate 

import speech_recognition as s

sr = s.Recognizer()

print("Hello! How Can I  Help You ")

try:
    with s.Microphone() as m:
        sr.adjust_for_ambient_noise(m, duration=1)
        audio = sr.listen(m)

    query = sr.recognize_google(audio, language="en-IN")
    print("Your Query:", query)

except s.UnknownValueError:
    print(" Could you plese reat again.")
except s.RequestError as e:
    print("Google Speech Recognition service se connect nahi ho saka:", e)
except OSError as e:
    print("Microphone error:", e)

