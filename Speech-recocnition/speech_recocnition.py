import speech_recognition as sr 
import pyttsx3

r=sr.Recognizer()


def record_text():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2,duration=0.5)

                audio2= r.listen(source2)

                mytext=r.recognize_google(audio2)

                return mytext
        except sr.RequestError as e:
            print("error")
        except sr.UnknownValueError:
            print("error")
    return

def output_text(text):
    f= open("Output.txt","a")
    f.write(text)
    f.write("\n")
    f.close(    )
    return(text)

while(1):
    text= record_text()
    output_text(text)
    print("wrote text")
