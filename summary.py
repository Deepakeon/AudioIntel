import sys
import os
import wave
import subprocess
import json
from vosk import Model, KaldiRecognizer
from transformers import pipeline

summarizer = pipeline("text2text-generation", model="t5-small")

def transcribe_audio(file_path):
    # model = Model("./vosk-model")
    # rec = KaldiRecognizer(model, 16000)
    
    # # Use FFmpeg to process audio on-the-fly
    # process = subprocess.Popen(
    #     ["ffmpeg", "-i", file_path, "-ar", "16000", "-ac", "1", "-f", "wav", "-"],
    #     stdout=subprocess.PIPE
    # )

    # text=""
    
    # while True:
    #     data = process.stdout.read(4000)
    #     if len(data) == 0:
    #         break
    #     if rec.AcceptWaveform(data):
    #         text += json.loads(rec.Result())["text"]

    text="An airplane traveling 600 mph (965 km/h) would take 1 million years to travel a single light-year! If we could travel one light-year using a crewed spacecraft like the Apollo lunar module, the journey would take approximately 27,000 years, according to the BBC Sky at Night Magazine.Stars and other objects beyond our solar system lie anywhere from a few light-years to a few billion light-years away. And everything astronomers see in the distant universe is literally history. When astronomers study objects that are far away, they are seeing light that shows the objects as they existed at the time that light left them. This principle allows astronomers to see the universe as it looked after the Big Bang, which took place about 13.8 billion years ago. Objects that are 10 billion light-years away from us appear to astronomers as they looked 10 billion years ago — relatively soon after the beginning of the universe — rather than how they appear today."
    summary = summarizer("extract meaningful insights from the provided text:" + text, min_length=round(len(text)/2), max_length=len(text)-1)
    # print("\n\n", text, "\n\n")
    print("\n", summary, "\n")

transcribe_audio("./speed.wav")