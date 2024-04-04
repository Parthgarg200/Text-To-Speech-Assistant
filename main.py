import win32com.client as wincom

if __name__ == '__main__':
    speak = wincom.Dispatch("SAPI.SpVoice")
    speak.Speak("Welcome to your personal speacking assistant. ")
    speak.speak("enter the text you want me to speak")
    print("(Enter 'exit' anytime you want to turn me off )")
    while True:
        x = input("Your text:  ")
        if x == "exit":
            speak.Speak("Thank you for using me, your assistant is signing off, Have a nice day")
            break
        speak.Speak(x)