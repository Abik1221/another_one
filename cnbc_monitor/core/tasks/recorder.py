import subprocess
import os
from datetime import datetime

# Folder to save recordings
RECORDINGS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "media", "recordings")
os.makedirs(RECORDINGS_DIR, exist_ok=True)

def record_stream(url: str, duration_seconds: int = 3600):
    """
    Record livestream from `url` for `duration_seconds` (default 1 hour)
    and save to recordings folder with timestamped filename.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"recording_{timestamp}.mp4"
    filepath = os.path.join(RECORDINGS_DIR, filename)

    print(f"[INFO] Recording {url} for {duration_seconds} seconds...")
    command = [
        "ffmpeg",
        "-y",               # overwrite if file exists
        "-i", url,          # input stream URL
        "-t", str(duration_seconds),  # duration
        "-c", "copy",       # copy codec (faster)
        filepath
    ]

    subprocess.run(command)
    print(f"[INFO] Saved recording: {filepath}")
    return filepath

# Example usage
if __name__ == "__main__":
    # Free livestream URL (BBC News)
    free_stream_url = "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"
    record_stream(free_stream_url, duration_seconds=60)  # 1 minute for demo
