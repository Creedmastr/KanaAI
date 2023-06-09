import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from pydub import AudioSegment
import os

def record_audio(output, sample_rate, duration):
    print("INFO: Recording audio")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()

    with open('temp.wav', 'wb') as f:
        write(f, sample_rate, audio_data)

    input_file = 'temp.wav'

    audio = AudioSegment.from_file(input_file)
    audio.export(output, format="wav")

    os.remove('./temp.wav')
