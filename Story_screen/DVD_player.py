import os
from google import genai
import pygame
from gtts import gTTS

dvd_img = pygame.image.load("dvd_disk.png")
dvd_img = pygame.transform.scale(dvd_img, (20, 30))


# to get ur own API key, enter this site: https://aistudio.google.com/api-keys and create your own.
# then create an enviroment variable with this command - "setx GEMINI_API_KEY "YOUR API KEY"
# restart pycharm and run the program.

client = genai.Client()
model_ai = "gemini-3.6-flash"

language = 'iw'
def get_summery(sub):
    res = client.interactions.create(
        model=model_ai,
        input=f"Write me a summery for the subject {sub}, in hebrew",
    )
    text_to_speech(res.output_text)

def text_to_speech(text):
    obj = gTTS(text=text, lang=language, slow=False)
    obj.save(f"summery.mp3")
    os.system(f"start summery.mp3")