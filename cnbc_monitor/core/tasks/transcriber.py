import os
import whisper
from pathlib import Path
from django.utils import timezone
import django

# Setup Django environment for standalone scripts
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cnbc_monitor.settings")
django.setup()

from core.models import Recording, Transcript

# Folder for transcripts
TRANSCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "media", "transcripts")
os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)

# Load Whisper model
model = whisper.load_model("tiny")  # tiny = fast demo model

def transcribe_recording(recording_path: str):
    """
    Transcribe a video/audio file using Whisper and save transcript to DB and file
    """
    print(f"[INFO] Transcribing {recording_path}...")
    result = model.transcribe(recording_path)

    # Save text file
    filename = Path(recording_path).stem + ".txt"
    transcript_path = os.path.join(TRANSCRIPTS_DIR, filename)
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

    # Save to DB
    recording_obj, _ = Recording.objects.get_or_create(file_path=recording_path)
    transcript_obj = Transcript.objects.create(
        recording=recording_obj,
        text=result["text"],
        created_at=timezone.now()
    )

    print(f"[INFO] Transcript saved: {transcript_path}")
    return transcript_obj

# Example usage
if __name__ == "__main__":
    test_recording = os.path.join(os.path.dirname(__file__), "..", "..", "media", "recordings", "recording_20250822_090000.mp4")
    transcribe_recording(test_recording)
