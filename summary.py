import sys
import os
from vosk import Model, KaldiRecognizer
import wave
import subprocess
import json
from vosk import Model, KaldiRecognizer


def transcribe_audio(file_path):
    model = Model("./vosk-model")
    rec = KaldiRecognizer(model, 16000)
    
    # Use FFmpeg to process audio on-the-fly
    process = subprocess.Popen(
        ["ffmpeg", "-i", file_path, "-ar", "16000", "-ac", "1", "-f", "wav", "-"],
        stdout=subprocess.PIPE
    )

    text=""
    
    while True:
        data = process.stdout.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            print(json.loads(rec.Result())["text"])
    
    # Final partial result
    print(json.loads(rec.FinalResult())["text"])

transcribe_audio("./speed.wav")