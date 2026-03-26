import speech_recognition as sr # as is use to suppose speechrec as sr its only a short form.
import webbrowser
import pyttsx3
import musicLibrary
import requests
import time


recognizer = sr.Recognizer() # helps to recognize or a class helps to speech recognization funtionality.
engine = pyttsx3.init() # Use to initialize pyttsx3 module.
url = "https://newsapi.org/v2/everything?q=india&sortBy=publishedAt&apiKey=6d27ad6753de411c904c8043b2a1c6a1"


def speak(text):
  engine.say(text)
  engine.runAndWait()
def proccessCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif "open facebook" in c.lower():
      webbrowser.open("https://facebook.com")
   elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")
   elif "open linkedin" in c.lower():
      webbrowser.open("https://linkedin.com")
   elif "open flipkart" in c.lower():
      webbrowser.open("https://flipkart.com")
   elif "open discord" in c.lower():
    webbrowser.open("https://discord.com")
   elif "open discord" in c.lower():
    webbrowser.open("https://discord.com")
   elif "open slack" in c.lower():
        webbrowser.open("https://slack.com")
   elif "open zoom" in c.lower():
        webbrowser.open("https://zoom.us")
   elif "open skype" in c.lower():
        webbrowser.open("https://skype.com")
   elif "open puma" in c.lower():
        webbrowser.open("https://puma.com")
   elif "open myntra" in c.lower():
        webbrowser.open("https://myntra.com")
   elif "open ajio" in c.lower():
        webbrowser.open("https://ajio.com")
   elif "open nykaa" in c.lower():
        webbrowser.open("https://nykaa.com")
   elif "open tatacliq" in c.lower():
        webbrowser.open("https://tatacliq.com")
   elif "open snapdeal" in c.lower():
        webbrowser.open("https://snapdeal.com")
   elif "open shopify" in c.lower():
        webbrowser.open("https://shopify.com")
   elif "open etsy" in c.lower():
        webbrowser.open("https://etsy.com")
   elif "open aliexpress" in c.lower():
        webbrowser.open("https://aliexpress.com")
   elif "open alibaba" in c.lower():
        webbrowser.open("https://alibaba.com")
   elif "open flipboard" in c.lower():
        webbrowser.open("https://flipboard.com")
   elif "open feedly" in c.lower():
        webbrowser.open("https://feedly.com")
   elif "open pocket" in c.lower():
        webbrowser.open("https://getpocket.com")
   elif "open instapaper" in c.lower():
        webbrowser.open("https://instapaper.com")
   elif "open calendly" in c.lower():
        webbrowser.open("https://calendly.com")
   elif "open timeanddate" in c.lower():
        webbrowser.open("https://timeanddate.com")
   elif "open world clock" in c.lower():
        webbrowser.open("https://worldclock.com")
   elif "open dictionary" in c.lower():
        webbrowser.open("https://dictionary.com")
   elif "open thesaurus" in c.lower():
        webbrowser.open("https://thesaurus.com")
   elif "open grammarly" in c.lower():
        webbrowser.open("https://grammarly.com")
   elif "open reword" in c.lower():
        webbrowser.open("https://reword.co")
   elif "open deepl" in c.lower():
        webbrowser.open("https://deepl.com")
   elif "open translate" in c.lower():
        webbrowser.open("https://translate.google.com")
   elif "open tts" in c.lower():
        webbrowser.open("https://ttsmp3.com")
   elif "open 10fastfingers" in c.lower():
        webbrowser.open("https://10fastfingers.com")
   elif "open monkeytype" in c.lower():
        webbrowser.open("https://monkeytype.com")
   elif "open keybr" in c.lower():
        webbrowser.open("https://keybr.com")
   elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
   elif c.lower().startswith("play"):
       song = c.lower().split(" ")[1] # DOt split is use to split the name in list ex., skyfall = sky fall 
       link = musicLibrary.music[song] 
       webbrowser.open(link)    
   elif "news" in c.lower():
    speak("Fetching latest news...")

    try:
        r = requests.get(url)

        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])

            if not articles:
                speak("No news found.")
                return

            speak("Here are the top headlines")

            for i, article in enumerate(articles[:4], start=1):
                title = article.get('title')
                if title:
                    print(f"{i}. {title}")
                    speak(title)

        else:
            speak("Sorry, I could not fetch news.")

    except Exception as e:
        print("Error:", e)
        speak("Something went wrong while fetching news.")
       

if __name__ == "__main__":
  speak("Initializing Jarvis....")
  while True:
    # Listen for the wake word "Jarvis"
    # Obtain audio from the microphone
    r = sr.Recognizer()


    print("recognizing...")
    # recognize speech using google instead of sphinx cause sphinx not giving me proper voice recognition as a required.
    try:
        with sr.Microphone() as source:
          print("Listening the wake word ...!")
          audio = r.listen(source, timeout=5, phrase_time_limit=5)# timeout is use to do speech recognization faster.
        word = r.recognize_google(audio)
        if(word.lower() == "jarvis"):
           speak("Yes Sir...!") 
          #  Listen for a command
           with sr.Microphone() as source:
             speak("Yes Sir...!") 
             print("Jarvis Actived Now...!")
             print("Give me the command : SIR..!")
             audio = r.listen(source)
             command = r.recognize_google(audio)

             proccessCommand(command)
    
    
    except Exception as e:
       print("Error; {0}".format(e))


   
      