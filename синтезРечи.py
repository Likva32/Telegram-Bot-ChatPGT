import torch
import sounddevice as sd
import time
import soundfile as sf

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'baya'
put_accent = True
put_yo = True
device = torch.device('cpu')
text = 'Артур ани роца отха меод'


model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models', model='silero_tts', language=language, speaker=model_id)

model.to(device)

audio = model.apply_tts(text=text, speaker=speaker, sample_rate=sample_rate, put_accent=put_accent, put_yo=put_yo)

print(text)
output_file = "output2.mp3"
sf.write(output_file, audio, sample_rate)

sd.play(audio, samplerate=sample_rate)
time.sleep(len(audio) / sample_rate)
sd.stop()

