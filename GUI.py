import tkinter as tk
import speech_recognition as sr
from PIL import Image, ImageTk
import pyttsx3
import pyaudio
import time
import getChatGPT as gpt

robo = pyttsx3.init()
voz = robo.getProperty('voices')
robo.setProperty('voice', voz[0].id)

def pergunta():
    robo = pyttsx3.init()
    robo.say("Qual a sua pergunta?")
    robo.runAndWait()
    microphone_on()

def microphone_on():
    robo.say("Já vou responder")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language='pt-BR',show_all=False)
        resposta = gpt.ask_gpt3(texto)
        print('Resposta'+resposta)
        # robo.setProperty('voice', voz[0].id)
        robo.say(resposta)
        robo.runAndWait()
    except sr.UnknownValueError:
         print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
         print("Could not request results from Google Speech Recognition service; {0}".format(e))

root = tk.Tk()
root.geometry("300x650+50+50")
root.title("HALL9000")
root.config(bg="black")

# Carregando a imagem usando PIL
image = Image.open("HAL9000_Case.svg.png")

# Criando uma imagem do Tkinter para exibir a imagem
tk_image = ImageTk.PhotoImage(image)


# Criando um widget Label para exibir a imagem
image_label = tk.Label(root, image=tk_image)
image_label.pack()

microphone_button = tk.Button(root, text="Iniciar", command=pergunta)
microphone_button.pack()

root.mainloop()
