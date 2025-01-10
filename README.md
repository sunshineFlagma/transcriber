# Simple Transcriber
The program creates subtitles from your MP3 file. 
Supports many languages.

## How does it work?
The program divides your MP3 audio file into segments, then recognizes words depending on the selected language. As a result, you get a .srt file that can be edited or immediately uploaded to YouTube.

## Installation and usage
git clone https://github.com/sunshineFlagma/transcriber.git<br />
cd transcriber<br />
pip install -r requirements.txt<br />

Move your MP3 file to the project root folder and rename it to audio.mp3<br />

python main.py<br />

In a few minutes you will receive an .srt file.\
