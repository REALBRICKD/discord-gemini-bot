from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

"""
#Set up API subclass for Google Gemini
class GoogleGeminiClient():
    chat = None

    def __init__(self):
        super().__init__(API_KEY)
        self.client = genai.Client(api_key=API_KEY)
        self.chat = self.client.chats.create(model = "gemini-2.5-pro")
    
    def respond(self, prompt):
        history = {} # reset history 
        while True:
            response = self.chat.send_message(prompt["parts"])
            if prompt["parts"].lower() == "quit":
                break
            print(response.text)
            print()
            user_input = input()
            prompt = {"role": "user", "parts": user_input} # get new prompt
"""
class geminiClient():
    client = None
    def __init__(self):
        self.client = genai.Client(api_key=API_KEY)
        # self.chat = self.client.chats.create(model = "gemini-2.5-pro")
    
    def respond(self, prompt):
        history = {} # reset history 
        while True:
            response = self.chat.send_message(prompt["parts"])
            if prompt["parts"].lower() == "quit":
                break
            print(response.text)
            print()
            user_input = input()
            prompt = {"role": "user", "parts": user_input} # get new prompt
