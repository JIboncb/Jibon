# import section
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyttsx3
import pywhatkit
import pyjokes
import rotatescreen
import os
import PyPDF2
from textblob import TextBlob
import platform
import calendar
import cowsay
from translate import Translator
import sounddevice
from scipy.io.wavfile import write
from speedtest import Speedtest
import psutil

print('Initializing Julie')

# variables section
home = 'Panchagarh'
live_in = 'Dinajpur'
boss = 'Sir'
ai_name = 'Julie'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# wishMe function
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak('Good morning sir')

    elif hour>=12 and hour<18:
        speak('Good afternoon sir')

    else:
        speak('Good evening sir')
    speak('How can I help you')

# command taking function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)

    try :
        print('Recognizing...')
        query = r.recognize_google(audio, language= 'en-in')
        query = query.lower()
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please")
    return query

# programme start
speak('Initializing')
speak(ai_name)
wishMe()

# if elif section
while True:
    query = takeCommand()
    print(query)

    if 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace('wikipedia', '')
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        speak('Opening youtube')
        url = 'youtube.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open facebook' in query.lower():
        speak('Opening facebook')
        url = 'facebook.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        speak('Opening google')
        url = 'google.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open stackoverflow' in query.lower():
        speak('Opening stackoverflow')
        url = 'stackoverflow.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'joke' in query:
        speak(pyjokes.get_joke())

    elif 'play' in query:
        song = query.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)

    elif 'who is' in query:
        speak('Searching wikipedia...')
        query = query.replace('who is', '')
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif "where is" in query:
        query = query.replace("where is", "")
        location = query
        speak("User asked to Locate")
        speak(location)
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open('https://www.google.com/maps/place/' +  location)

    elif 'go on a date' in query:
        speak('sorry sir, I can not go with you, because i am an AI')

    elif 'who are you' in query:
        speak('i am an ai assistant created by Jibon')

    elif 'created you' in query:
        speak('i have been created by Jibon')

    elif 'are you single' in query:
        speak('I am finding the perfect one')

    elif 'be my girlfriend' in query:
        speak('Maybe you should give me some time')

    elif 'how are you' in query:
        speak("I am fine, Thank you")
        speak("How are you, Sir")

    elif 'fine' in query or "good" in query:
        speak("It's good to know that your fine")

    elif 'exit' in query or 'stop' in query:
        speak("Thanks for giving me your time")
        exit()

    elif 'search' in query or 'play' in query:
        query = query.replace("search", "")
        query = query.replace("play", "")
        webbrowser.open(query)

    elif "who i am" in query:
        speak("If you can talk then definitely your human.")

    elif "why you came to world" in query:
        speak("Thanks to Jibon. further It's a secret")

    elif ai_name in query:
        wishMe()
        speak(f"{ai_name} 1 point o in your service Mister")

    elif "can you help me" in query:
        speak("of course sir, it is my pleasure")

    elif "my favourite song" in query:
        speak("your favourite song is mood")

    elif 'hi' in query:
        speak('hello sir')

    elif 'rotate the screen' in query:
        speak('ok sir')
        screen = rotatescreen.get_primary_display()
        for i in range(13):
            time.sleep(1)
            screen.rotate_to(i * 90 % 360)

    elif 'what is your name' in query:
        speak('My friends call me')
        speak(ai_name)

    elif 'exit' in query or 'close' in query:
        speak('Thanks for giving me your time')
        exit()

    elif  'say whatever i write' in query:
        while True:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)

            text = input('Say something:')
            engine.say(text)
            engine.runAndWait()

            if 'stop' in text:
                exit()
            elif 'exit' in text:
                exit()

    elif 'my songs' in query:
        speak('Here you g with music')
        music_dir = 'links'
        songs = os.listdir(music_dir)
        print(songs)
        random = os.startfile(os.path.join(music_dir, songs[0]))

    elif 'reason for you' in query.lower():
        speak("I was created as the first big project by Mister Jibon")

    elif 'how to hack' in query:
        speak("no sir, you didn't programmed me to do these things")

    elif 'good morning' in query:
        speak('Good morning sir')

    elif 'i love you' in query:
        speak("It's hard to understand")

    elif 'is love' in query:
        speak('It is the 7th sence that destroy all other sence')

    elif "why you came to world" in query:
        speak("Thanks to Jibon. further It's a secret")

    elif 'want to change your name' in query:
        speak('If you want to change my name you have to go to the variable section and change the ai name.')

    elif 'think about love' in query:
        speak('Love is an useless thing. It will distroy your life')

    elif 'where is my home' in query:
        speak(f'Your home is in {home}')

    elif 'i live' in query:
        speak(f'You live in {live_in}')

    elif 'know hacking' in query:
        speak("No, I don't")

    elif 'pdf reader' in query:
        speak('opening pdf reader')
        book = open("name.pdf", "rb")
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        print(pages)

    elif 'open spell checker' in query:
        a = input("Input text:")
        print('Your word:' + str(a))
        b = TextBlob(a)
        print('Corrected text:' + str(b.correct()))

    elif 'system information' in query:
        myS = platform.uname()

        print(f'System: {myS.system}')
        print(f'Node name: {myS.node}')
        print(f'Release: {myS.release}')
        print(f'Version: {myS.version}')
        print(f'Machine: {myS.machine}')
        print(f'Processor: {myS.processor}')

    elif 'a pattern' in query:
        def pattern(n):
            for i in range(n):
                print((i+1)*'*')
            for i in range(n-1,0,-1):
                print(i*'*')
        pattern(5)

    elif 'open calendar' in query:
        try:
            speak('tell me the number of the year')
            y = int(takeCommand())
            speak('Tell me the number of the month')
            m = int(takeCommand())

            print(calendar.month(y, m))
        except Exception as e:
            print(e)
            speak("Sorry sir, I didn't understand")

    elif 'cowsay' in query:
        cowsay.daemon(input('Enter word:'))

    elif 'record voice' in query:
        fs = 44100
        sc = int(input("Enter the duration in seconds: "))
        print("Recording...\n")
        recordVoice = sounddevice.rec(int(sc * fs),samplerate = fs, channels = 2)
        sounddevice.wait()
        write("out.wav",fs,recordVoice)
        print("Finished...\nPlease check it")

    elif 'check the internet speed' in query:
        st = Speedtest()
        speak("Checking speed....")
        print("Your connection's download speed is:", st.download())
        speak("Your connection's download speed is:" + str(st.download()))
        print("Your connection's upload speed is:", st.upload())
        speak("Your connection's upload speed is:" + str(st.upload()))

    elif "check battery percentage" in query:
        battery = psutil.sensors_battery()
        percent = str(battery.percent)
        print("Your battery is running on "+percent+"% battery level")
        speak("Your battery is running on "+percent+"% battery level")

    elif "open obs" in query:
        os.startfile("C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe")

    elif 'open canva' in query:
        os.startfile("C:\\Users\\Dinesh\\AppData\\Local\\Programs\\Canva\\Canva.exe")

    else:
        pass
