import os
import subprocess
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cnbc_monitor.settings")
django.setup()

from core.models import Clip, Keyword, Transcript
from django.utils import timezone

# Folder to save clips
CLIPS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "media", "clips")
os.makedirs(CLIPS_DIR, exist_ok=True)

def create_clip(recording_path: str, keyword: Keyword, transcript_obj: Transcript, start_seconds=0, duration_seconds=120):
    """
    Create a clip of given duration from the recording starting at start_seconds.
    """
    # Clip filename
    clip_filename = f"{os.path.splitext(os.path.basename(recording_path))[0]}_{keyword.word}.mp4"
    clip_path = os.path.join(CLIPS_DIR, clip_filename)

    print(f"[INFO] Creating clip for keyword '{keyword.word}'...")
    command = [
        "ffmpeg",
        "-y",
        "-i", recording_path,
        "-ss", str(start_seconds),
        "-t", str(duration_seconds),
        "-c", "copy",
        clip_path
    ]
    subprocess.run(command)

    # Save to DB
    clip_obj = Clip.objects.create(
        keyword=keyword,
        transcript=transcript_obj,
        file_path=clip_path,
        created_at=timezone.now()
    )
    print(f"[INFO] Clip saved: {clip_path}")
    return clip_obj

# Example usage
if __name__ == "__main__":
    from core.models import Transcript, Keyword

    # Take latest transcript
    latest_transcript = Transcript.objects.latest("created_at")
    keywords = Keyword.objects.all()[:1]  # demo: take first keyword

    for kw in keywords:
        create_clip(
            recording_path=latest_transcript.recording.file_path,
            keyword=kw,
            transcript_obj=latest_transcript
        )
