
import os
import win32com.client
import pyttsx3 as pt
import speech_recognition as sr
import webbrowser as wb
import subprocess as sub
from config import apikey1
import openai



def ai(prompt):
    text = f"ai response for prompt:{prompt}\n********\n"
    openai.api_key = apikey1

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("ai"):
        os.mkdir("ai")
    with open(f"ai/{prompt[0:10]}.txt", "w") as f:
        f.write(text)


# todo:define method to make voice input
def say(text):
    voi = pt.init()  # making the pyttsx3 variable
    voi.setProperty('rate', 120)  # setting speaking rate
    voi.say(text)  # inputting text to variable
    voi.runAndWait()  # making it wait

    # OR


def say1(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


# todo:take input as a voice
def takeCommand():
    recognize = sr.Recognizer()

    mic = sr.Microphone()
    with mic as source:

        recognize.adjust_for_ambient_noise(source)  # this will adjust the speech in case of ambient voice
        audio = recognize.listen(source)  # for audio input
        try:
            query = recognize.recognize_google(audio)
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Unable to recognize speech.")
        except sr.RequestError as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    choice = int(input("Enter Your Choice 1: for voice input or Enter Choice 2: for written input\n"))
if choice == 1:
    chrome_loc = "C:\Program Files\Google\Chrome\Application"
    print('PyCharm')
    say("Hello I am jarvis AI at your service")

    while True:
        print("Listning...")
        query = takeCommand()

        sites = {
            "Youtube": "https://www.youtube.com",
            "google": "https://google.com",
            "Wikipedia": "https://www.wikipedia.com",
            "Instagram": "https://www.instagram.com"
        }
        # todo: add more sites
        for site in sites:
            if f"Open {site}".lower() in query.lower():
                say(f"Opening {site} sir....")
                # webbrowser.open(site)
                chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

                wb.register('chrome', None, wb.BackgroundBrowser(chrome_path))
                wb.get('chrome').open(sites[site])
        # todo: make jarvis do tasks
        if f"Open Visual Studio".lower() in query.lower():
            say("Opening Visual Studio sir...")
            sub.Popen("C:/Program Files/Microsoft Visual Studio/2022/Community/Common7/IDE/devenv.exe")
        if f"Thank you".lower() in query.lower():
            say("Your welcome I am here for you ant time you need me")
            break
        if f"Open Chrome".lower() in query.lower():
            say("Opening google Chrome Sir")
            sub.Popen("C:/Program Files/Google/Chrome/Application/Chrome.exe")
        if f"Open Whatsapp".lower() in query.lower():
            say("Opening Whatsapp sir")
            sub.Popen("C:/Users/dell/AppData/Local/WhatsApp/WhatsApp.exe")
        if f"Using AI".lower() in query.lower():
            ai(prompt=query)

if choice == 2:

    while 1:
        say("Hello I am jarvis AI at your service")
        print("Anything you write will be answered\n")
        text = input("Write your query or To exit write NULL\n")
        if text == "NULL":
            break
        if text != "NULL":
            ai(prompt=text)
