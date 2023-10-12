import pyttsx3
import sys
from tkinter import *
from PIL import ImageTk, Image
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib
import ctypes
import pywhatkit
import datetime
from tkinter.messagebox import *
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate",150)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


root = Tk()             
root.geometry('700x500')
root.title('Virtual Assistant')

#terminal


#mic
photo = PhotoImage(file = r"D:\Mini_Project\Pics\Mic.jpg")
photoimage = photo.subsample(5,5)

#interface
frame = Frame(root, width=1500, height=1000)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open("D:\Mini_Project\Pics\As1.webp"))
label = Label(frame, image = img)
label.pack()

#Text Box
T1 = Text(root, height = 2, width = 25)
T1.pack()
T1.insert(INSERT,"How Can I Help You")

T = Text(root, height = 5, width = 52)
T.insert(INSERT,"Listening")
T.pack(side="bottom")

#clear text input
def clear(t):
   t.delete("1.0","end")

#insert text input
def insert(text,t):
    t.insert(INSERT,text)

def talk(text):
    engine.say(text)
    engine.runAndWait()

#taking audio input
def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source,duration=1)
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            #command = command.lower()
    except:
        pass
    return command

#email-ids
dict={'0':'mail1','1':'mail2'}

#sending mail
def send_email(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmail', 'password')
    server.sendmail('yourmail',dict[to],content)
    clear(T)
    insert("Mail sent successfully",T)
    talk('Mail sent successfully')
    print('Mail sent successfully')
    server.close()

#working for user commands
def run_alexa():
    command = take_command()
    clear(T1)
    insert(command,T1)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'hello' in command:
        talk('Hello nice to meet you')
    elif 'time' in command:
        tim = datetime.datetime.now().strftime('%I:%M %p')
        clear(T)
        insert(tim,T)
        talk('Current time is ' + tim)
    elif 'who is' in command:
        person = command.replace('You are searching for', '')
        info = wikipedia.summary(person, 1)
        clear(T)
        insert(info,T)
        talk(info)
    elif 'joke' in command:
        clear(T)
        jokes=pyjokes.get_joke()
        insert(jokes,T)
        talk(jokes)
        #return
    elif 'mail' in command:
        clear(T1)
        insert("Tell Mail Id",T1)
        talk('Tell mail id')
        to=take_command()
        #print(to)
        if to in dict.keys():
            clear(T1)
            insert("Say Content",T1)
            talk('Say content')
            content=take_command()
            #print(content)
            clear(T1)
            insert(command,T1)
            send_email(to,content)
        else:
            insert('Enter valid mail id',T)
            talk('Enter valid mail id')
    elif 'youtube' in command:
        clear(T)
        insert('Opening youtube..!',T)
        talk('Opening Youtube!!!')
        webbrowser.open("youtube.com")
    elif 'cricbuzz' in command:
        print('Opening cricbuzz..!')
        webbrowser.open("cricbuzz.com")
    elif 'whatsapp' in command:
        webbrowser.open("https://web.whatsapp.com/")
        insert('Opening Whatsapp....!',T)
        talk('Opening Whatsapp')
        #os.startfile(app)
        return
    elif 'lock window' in command:
        showwarning("Oops","Locking device")
        talk("locking the device")
        ctypes.windll.user32.LockWorkStation()
        return
    elif 'shutdown' in command:
        showwarning("Oops","Shutting Down")
        talk("Shutting down the device the device")
        talk("Hold On a Sec ! Your system is on its way to shut down")
        os.system("shutdown /s /t 1")
        return
    elif 'restart' in command:
        showwarning("Oops","Restarting")
        talk("Restarting the device")
        talk("Hold On a Sec ! Your system is on its way to restart")
        os.system("shutdown /r")
        return
    elif 'what is my name' in command:
        clear(T1)
        insert("What is my name",T1)
        clear(T)
        insert("your name is "+name,T)
        talk('your name is '+name)
    elif 'quit' in command:
        talk('Good Bye')
        exit()
    elif 'search' in command:
        talk('what do you want to search for?')
        search=take_command()
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        clear(T)
        insert(search,T)
        talk('Here what i found')
    elif 'find me' in command:
        talk('What is your current location?')
        location = take_command()
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        clear(T)
        insert(location,T)
        talk('Here is location' + location)
    elif 'who are you' in command:
        clear(T)
        insert("I am Virtual Assistant",T)
        talk('I am Virtual Assistant')
    elif 'How are You'in command:
        clear(T)
        insert("Fine What About You!!")
        talk('Fine What About You!!')
    else:
        clear(T)
        insert("Please say the command again.",T)
        talk('Please say the command again.')
        #run_alexa()

def say_name():
    talk('Say name')
    global name
    name=take_command()
    return name


def on_true():
    run_alexa()

def on_false():
    clear(T)
    insert('Good Bye',T)
    talk('good bye')
    sys.exit()

talk('How Can I Help You')
btn0 = Button(root,text='name',command = say_name)
btn0.pack(side='left')
btn1 = Button(root,image=photoimage,compound=LEFT,borderwidth=5,command = on_true)
btn1.pack(side='bottom')
btn2= Button(root, text = 'Stop!',command =on_false)
btn2.pack(side ='top')
root.mainloop()   
