import speech_recognition as sr
##It allows computers to understand human language.
import pyttsx3
##text-to-speech conversion library
import datetime
##for date and time
import wikipedia as wiki
# for wikipedia
import webbrowser
# for web activity
import os
##provides the facility to establish the interaction between the user and the operating system.
import time
# ## Using this import we can read system time and date
import subprocess
##is a module used to run new codes and applications by creating new processes
from ecapture import ecapture as ec
# capturing picture
import wolframalpha
# allow us to calculate the expert-level answers with its algorithms, knowledgebase, and Artificial Intelligence (AI) technology of Wolfram
import json
# used to transfer data as text that can be sent over a network
import requests
# The requests module allows you to send HTTP requests using Python
import pyjokes
# for jpkes
import pywhatkit

# used to send the message by the Python script




print('Loading your AI personal assistant - G One')
listener = sr.Recognizer()
# for listing user voice
engine =pyttsx3.init('sapi5')

voices =engine.getProperty('voices')
engine.setProperty('voice' ,voices[1].id)




def speak(text):
    engine.say(text)
    engine.runAndWait()


# show according to the system time
def wishMe():
    hour =datetime.datetime.now().hour
    if hour>=0 and hour <12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour <18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)


        try:
            statement=r.recognize_google(audio,language='en-in')
            print("user said:{statement}\n")


        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


speak("Loading your AI personal assistant G-One")
wishMe()




if __name__ == '__main__':

    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            # whenever no statement go stop
            break

        # if good bye or ok bye or stop say user alexa stop
        if "goodbye" in statement or "okay bye" in statement or "stop" in statement or "shut up" in statement:
            speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            break
        ##if alexa listen youtube word redirect to youtube page
        elif 'youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
            break
        ##if alexa listen google word redirect to google page
        elif 'google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)
            break


        ##if alexa listen gmail word redirect to gmail page
        elif 'gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
            break


        ##if alexa listen nitc word redirect to eduserver page page
        elif 'nitc' in statement:
            webbrowser.open_new_tab("https://eduserver.nitc.ac.in/login/index.php")
            speak("Nitc eduserver is  open now")
            time.sleep(5)
            break


        ##if alexa listen facebook word redirect to facebook page
        elif 'facebook' in statement:
            webbrowser.open_new_tab("https://www.facebook.com/")
            speak("facebook is  open now")
            time.sleep(5)
            break


        ##if alexa listen instagram word redirect to instagram page
        elif 'instagram' in statement:
            webbrowser.open_new_tab("https://www.instagram.com/")
            speak("instagram is  open now")
            time.sleep(5)
            break


        ##if alexa listen weather word then ask to city name page
        ##showing city Temperature in kelvin unit
        ##humidity in percentage
        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
                break
            else:
                speak(" City Not Found ")
                break

            # ## USING THIS CODE BLOCK USER CAN GET TO KNOW CURRENT TIME
        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            time.sleep(5)


        # ## IT IS A SIMPLE SPEECH CODE BLOCK
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am G-one version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')
            break
        # ## IT IS A SIMPLE SPEECH CODE BLOCK
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by rajkumar and durgesh")
            print("I was built by rajkumar  and durgesh")
            break
        # ## USING THIS CODE BLOCK USER CAN GO OVER STACKOVERFLOW TO
        # POST AND SEARCH FOR QUERIES
        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")
            break
        # ## USING THIS CODE BLOCK USER CAN GET ONGOING NEWS LIVE
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
            break
        # ## USING THIS CODE BLOCK USER CAN START THEIR CAMERA.
        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")
            time.sleep(5)
            Break
        # ## USING THIS CODE BLOCK USER CAN BROWSE THROUGH INTERNET
        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
            break
        # ## USING THIS CODE BLOCK USER CAN HEAR JOKES BY VIRTUAL ASST.
        elif 'joke' in statement:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        # ## USING THIS CODE BLOCK USER CAN PLAY VIDEO SONG ON YOUTUBE
        elif 'play' in statement:
            song = statement.replace('play', '')
            speak('playing ' + song)
            # print(song)
            pywhatkit.playonyt(song)
            time.sleep(5)
            break
        # ## USING THIS CODE BLOCK USER CAN SEARCH ON WIKIPEDIA FOR
        # FAMOUS PERSONA
        elif 'who is this' in statement:
            person = statement.replace('who is this', '')
            info = wiki.summary(person, 1)
            print(info)
            speak(info)
            Break
        # ## USING THIS CODE BLOCK USER CAN ASK QUERY LIKE COMPUTATIONAL
        # AND GEOGRAPHICAL et.c
        elif 'question' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            break
        # ## USING THIS CODE BLOCK USER CAN DIRECTLY SHUTDOWN THEIR PC
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
            break
time.sleep(3)























