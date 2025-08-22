# CNBC Livestream Keyword Clips Demo

This is a simple demo web app that records CNBC livestreams, detects keywords, and creates short clips with transcripts. The dashboard allows you to view clips and run the pipeline from the browser.

---

## Features

- Record live stream (demo stream used for free)
- Transcribe recordings using OpenAI Whisper
- Detect keywords from transcripts
- Create 2-minute clips around detected keywords
- Simple Django dashboard to view clips and transcripts
- Run the full pipeline with one button

---

## Tech Stack

- Python 3.13
- Django 5.x
- Whisper (OpenAI) for transcription
- ffmpeg for recording and clipping
- Docker + Docker Compose
- Frontend: Django templates

---

## Installation (Local)

1. Clone the repo:

```bash
git clone <your-repo-url>
cd cnbc_monitor


# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate


pip install -r requirements.txt


python manage.py migrate


python manage.py createsuperuser


python manage.py runserver


http://127.0.0.1:8000/



# Installing FFmpeg for the CNBC Livestream Demo

FFmpeg is required to record and clip the livestream videos.

---

## 1. Windows

1. Download FFmpeg:

[https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

2. Extract the zip file (e.g., to `C:\ffmpeg`)

3. Add FFmpeg to your system PATH:
   - Press `Win + S`, type `Environment Variables`, open **Edit the system environment variables**
   - Click **Environment Variables**
   - Under **System variables**, select `Path` → **Edit** → **New**
   - Add the path to `ffmpeg\bin` (e.g., `C:\ffmpeg\bin`)
   - Click **OK** to save

4. Verify installation:

```bash
ffmpeg -version
