from voice.listen import listen
from voice.speak import speak
from physics.qa import answer_physics
import webbrowser
import datetime
import os

def run():
    speak("Jarvis Physics Assistant activated")

    while True:
        command = listen()

        if "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {time}")

        elif "open google" in command:
            webbrowser.open("https://google.com")

        elif "open code" in command:
            os.system("code")

        elif "physics" in command or "define" in command or "explain" in command:
            response = answer_physics(command)
            speak(response)

        elif "stop" in command:
            speak("Goodbye")
            break

run()
