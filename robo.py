import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 3.1. Created by Dilli")
    while True:
        x = input("Enter what you want me to speak (or enter 'q' to quit): ")
        if x.lower() == "q":
            speak("Bye bye, friend!")
            break
        speak(x)
