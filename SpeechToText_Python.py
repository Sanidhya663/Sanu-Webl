#pip install SpeechRecognition==3.14.5
#pip install pyaudio

import speech_recognition as sr
import os
import threading

# pip install mtranslate
# pip install pyaudio
from mtranslate import translate

#pip install colorama
from colorama import Fore,Style,init

init(autoreset=True)

def print_loop():
    #while True:
        print(Fore.GREEN+ "Listening..",end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)

def Translate_hindi_to_english(text):
    english_text = translate(text,"en-us")
    return english_text

def Speech_To_Text_Python():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 34000
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.3
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.2

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.GREEN + "Listening..", end="", flush=True)
            try:
                audio = recognizer.listen(source,timeout=None)
                print("\r" + Fore.LIGHTBLACK_EX + "Recognizing....", end="",flush=True)
                recognizer_text = recognizer.recognize_google(audio).lower()
                if recognizer_text:
                    trans_text = Translate_hindi_to_english(recognizer_text)
                    print("\r" + Fore.BLUE + "You : " + trans_text)
                    return trans_text
                else:
                    return ""
            except sr.UnknownValueError:
                recognizer_text = ""
            except sr.RequestError as ex:
                print("\r" + Fore.RED + f"Network error: {ex}. Check internet/DNS and try again.")
                return ""
            finally:
                print("\r",end="",flush=True)

            os.system("cls" if os.name == "nt" else "clear")
        stt_thread = threading.Thread(target=Speech_To_Text_Python)
        print_thread = threading.Thread(target=print_loop)
        stt_thread.start()
        print_loop.start()
        stt_thread.join()
        print_loop.join()




