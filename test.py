import os
import requests
from huggingface_hub import InferenceClient

# API keys
weather_api_key = os.getenv("OPENWEATHER_API_KEY", "")
hf_token = os.getenv("HF_API_KEY", "")

client = InferenceClient(api_key=hf_token)

def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={weather_api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()
    print("Weather API Response:", data)  # Debug print

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

def ask_jarvis_ai(prompt):
    try:
        apiurl = "https://router.huggingface.co/hf-inference/models/deepseek-ai/DeepSeek-V3.2"
        headers = {"Authorization": f"Bearer {hf_token}", "Content-Type": "application/json"}
        payload = {"inputs": prompt, "parameters": {"max_new_tokens": 100}}
        response = requests.post(apiurl, headers=headers, json=payload)
        print("AI Response status:", response.status_code)
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
        print("Status code:", response.status_code if 'response' in locals() else "No response")
        return "Sorry Sir, AI is having trouble thinking right now."

# Test weather
print("Testing Weather API:")
weather_result = get_weather("London")
print(weather_result)

# Test AI
print("\nTesting Hugging Face AI:")
ai_result = ask_jarvis_ai("What is the capital of France?")
print(ai_result)