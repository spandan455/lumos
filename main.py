import speech_recognition as sr
import os
import win32com.client
import webbrowser
import openai



# creating function for talking of LUMOS
def say(text):
    # Generating Voice
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    # speaking given text
    speaker.Speak(text)


# taking voice input from user
def takeCommand():
    # creating voice recognizer
    r = sr.Recognizer()

    # Changing voice settings
    with sr.Microphone() as source:
        r.energy_threshold = 1200

        # Recognizing text
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio , language="en-in")
            print("User Input : " + query)
            return query
        except Exception as e:
            say("Some Error Occurred")

 # setting up Chatgpt in Lumos
def openMode():
    say("ai mode enabled ")
    print("Listening...")
    command = takeCommand()
    # keep this key secret
    openai.api_key = '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'
    # generating response
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=command,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # printing response
    print(response["choices"][0]["text"])

if __name__ == '__main__':
    say("Hello I am Lumos")
    print("Listening...")
    # listening commmand
    text = takeCommand()
    # websites to display on browser
    sites = [["Youtube" , "https://youtube.com"] ,
             ["Google" , "https://google.com"] ,
             ["codingame" , "https://codingame.com"] ,
             ["Wikipedia" , "https://wikipedia.org"] ,
             ["Chat GPT" , "https://chat.openai.com"],
             ["github" , "https://github.com"]]
    for site in sites:
        if f"open {site[0]}".lower() in text.lower():
            say(f"Opening {site[0]}")
            webbrowser.open_new_tab(site[1])
    # musics to play in the device
    musics = [["Think", "C:/Users/DELL/Music/think.mp3"],
             ["Solution", "C:/Users/DELL/Music/intense-solution.mp3"],
             ["Work", "C:/Users/DELL/Music/work.mp3"]]
    for music in musics:
        if f"play {music[0]}".lower() in text.lower():
            say(f"Playing  {music[0]}")
            webbrowser.open_new_tab(music[1])
    # projects must open in vs code
    setups = [
        ["Python Course" , "C:/Users/DELL/Downloads/sp-temp/python-course"],
        ["Tic Tac Toe", "C:/Users/DELL/Downloads/sp-temp/TicTacToe"]
    ]

    for setup in setups:
        if f"set up {setup[0]}".lower() in text.lower():
            say(f"Setting up  {setup[0]}")
            os.system(f"cd {setup[1]} & code .")
    # enabling access to chatGPT
    if "enable bright".lower() in text.lower():
        openMode()