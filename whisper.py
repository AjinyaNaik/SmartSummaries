import whisper
from IPython.display import Audio

model= whisper.load_model("base")
print(model.device)

Audio("matrix.mp3")

# For matrix audio file

audio= whisper.load_audio("matrix.mp3")

audio = whisper.pad_or_trim(audio)

mel = whisper.log_mel_spectrogram(audio).to(model.device)

_,probs= model.detect_language(mel)

print("Detected Language",{max(probs,key=probs.get)})

options= whisper.DecodingOptions()

result = whisper.decode(model, mel, options)
print(result.text)

# For a Bollywood Movie dialogue

audio= whisper.load_audio("wanted.mp3")

audio = whisper.pad_or_trim(audio)

mel = whisper.log_mel_spectrogram(audio).to(model.device)

_,probs= model.detect_language(mel)

print("Detected Language",{max(probs,key=probs.get)})

options= whisper.DecodingOptions()

result = whisper.decode(model, mel, options)
print(result.text)