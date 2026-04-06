import os
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()
recognizer = sr.Recognizer()
engine = pyttsx3.init()
news_api_key = os.getenv("NEWS_API_KEY")
weather_api_key = os.getenv("OPENWEATHER_API_KEY")
hf_token = os.getenv("HF_API_KEY")

news_url = f"https://newsapi.org/v2/everything?q=india&sortBy=publishedAt&apiKey={news_api_key}"
client = InferenceClient(api_key=hf_token)

websites = {
    "google": "https://google.com",
    "facebook": "https://facebook.com",
    "youtube": "https://youtube.com",
    "linkedin": "https://linkedin.com",
    "flipkart": "https://flipkart.com",
    "discord": "https://discord.com",
    "slack": "https://slack.com",
    "zoom": "https://zoom.us",
    "skype": "https://skype.com",
    "puma": "https://puma.com",
    "myntra": "https://myntra.com",
    "ajio": "https://ajio.com",
    "nykaa": "https://nykaa.com",
    "tatacliq": "https://tatacliq.com",
    "snapdeal": "https://snapdeal.com",
    "shopify": "https://shopify.com",
    "etsy": "https://etsy.com",
    "aliexpress": "https://aliexpress.com",
    "alibaba": "https://alibaba.com",
    "flipboard": "https://flipboard.com",
    "feedly": "https://feedly.com",
    "pocket": "https://getpocket.com",
    "instapaper": "https://instapaper.com",
    "calendly": "https://calendly.com",
    "timeanddate": "https://timeanddate.com",
    "world clock": "https://worldclock.com",
    "dictionary": "https://dictionary.com",
    "thesaurus": "https://thesaurus.com",
    "grammarly": "https://grammarly.com",
    "reword": "https://reword.co",
    "deepl": "https://deepl.com",
    "translate": "https://translate.google.com",
    "tts": "https://ttsmp3.com",
    "10fastfingers": "https://10fastfingers.com",
    "monkeytype": "https://monkeytype.com",
    "keybr": "https://keybr.com",
    "whatsapp": "https://whatsapp.com"
}

def ask_jarvis_ai(prompt):
    try:
        apiurl = "https://router.huggingface.co/hf-inference/models/deepseek-ai/DeepSeek-V3.2"
        headers = {"Authorization": f"Bearer {hf_token}", "Content-Type": "application/json"}
        payload = {"inputs": prompt, "parameters": {"max_new_tokens": 100}}
        response = requests.post(apiurl, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                return data[0].get("generated_text", "AI returned an empty response.")
            else:
                return "AI returned an empty response."
        else:
            return "Sorry Sir, AI is having trouble thinking right now."
    except Exception as e:
        print("Hugging Face AI Error:", e)
        return "Sorry Sir, AI is having trouble thinking right now."


def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_city():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for city name...")
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    try:
        city = r.recognize_google(audio)
        print(f"City heard: {city}")
        return city
    except Exception as e:
        print("Error recognizing city:", e)
        return None

def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={weather_api_key}&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()

    if data.get("cod") == 200:
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temp = main["temp"]
        humidity = main["humidity"]
        
        report = (f"The temperature in {city_name} is {temp} degrees Celsius "
                  f"with {weather_desc}. The humidity is {humidity} percent.")
        return report
    else:
        return f"Sorry Sir, I couldn't find that city. Error: {data.get('message', 'Unknown error')}"

def processCommand(c):
    c_lower = c.lower()
    for site, url in websites.items():
        if f"open {site}" in c_lower:
            webbrowser.open(url)
            return
    if c_lower.startswith("play"):
        song = c_lower.replace("play", "").strip()
        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Sorry Sir, I couldn't find that song in the library.")
        return
    if "news" in c_lower:
        speak("Fetching latest news...")
        try:
            r = requests.get(news_url)
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
        return
    if "weather" in c_lower:
        speak("Please tell me the city name.")
        city = listen_city()
        if city:
            speak(f"Fetching weather for {city}")
            weather_report = get_weather(city)
            print(weather_report)
            speak(weather_report)
        else:
            speak("Sorry Sir, I could not hear the city name. Please try again.")
        return
    speak("Let me think...")
    ai_response = ask_jarvis_ai(c)
    print("Jarvis AI:", ai_response)
    speak(ai_response)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    
    while True:
        r = sr.Recognizer()
        print("recognizing...")
        
        try:
            with sr.Microphone() as source:
                print("Listening the wake word ...!")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            
            word = r.recognize_google(audio)
            
            if word.lower() == "jarvis":
                speak("Yes Sir...!") 
                with sr.Microphone() as source:
                    print("Jarvis Actived Now...!")
                    print("Give me the command : SIR..!")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        
        except Exception as e:
            print("Error:", e)