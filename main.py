import speech_recognition as sr
from pydub import AudioSegment
import srt
from datetime import timedelta

def transcribe_audio_to_srt(audio_file):
    audio = AudioSegment.from_file(audio_file)
    audio = audio.set_channels(1).set_frame_rate(16000)

    recognizer = sr.Recognizer()
    duration = len(audio) / 1000
    segment_length = 10  # Segment length in seconds
    subtitles = []
    
    for i in range(0, int(duration), segment_length):
        start = i
        end = min(i + segment_length, duration)
        segment = audio[start*1000:end*1000]
        segment.export("temp.wav", format="wav")
        
        with sr.AudioFile("temp.wav") as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data, language="en-US") # <-- Here, you can change the lang
            except sr.UnknownValueError:
                text = "[Not recognized]"
        
        subtitle = srt.Subtitle(
            index=len(subtitles) + 1,
            start=timedelta(seconds=start),
            end=timedelta(seconds=end),
            content=text
        )
        subtitles.append(subtitle)
    
    with open("subtitles.srt", "w") as srt_file:
        srt_file.write(srt.compose(subtitles))

#use func
transcribe_audio_to_srt("audio.mp3")
