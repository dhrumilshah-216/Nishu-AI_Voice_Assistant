import speech_recognition as sr
from functions import speak, process_command

assistant_name = "Nishu"

if(__name__ == "__main__"):
    speak("Hey Dhrumil.... I'm ready.")      # Startup greeting

    while True:
        r = sr.Recognizer() 
        
        try:
             # Listen for wake word
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            wake_word = r.recognize_google(audio)
            print(f"{assistant_name} thinks you said --> " + wake_word)

            if "nishu" in wake_word.lower():
                print("Wake word detected!")
                speak("What's up, Dhrumil bro?")

                # Listen for the actual command
                with sr.Microphone() as source:
                    print("Nishu is activated...\nWhat do you want me to do?")
                    audio = r.listen(source)
                command = r.recognize_google(audio)
                process_command(command)

        except sr.UnknownValueError:
            print(f"{assistant_name} could not understand audio")
            
        except Exception as e:
            print(f"{assistant_name} found error; \n{e}")