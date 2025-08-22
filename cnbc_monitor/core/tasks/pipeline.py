from core.tasks.recorder import record_stream
from core.tasks.transcriber import transcribe_recording
from core.tasks.keyword_detector import detect_keywords
from core.tasks.clipper import create_clip

FREE_STREAM = "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"

def run_pipeline():
    # Step 1: Record
    recording_file = record_stream(FREE_STREAM, duration_seconds=60)  # demo 1 min

    # Step 2: Transcribe
    transcript_obj = transcribe_recording(recording_file)

    # Step 3: Detect Keywords
    matched_keywords = detect_keywords(transcript_obj)

    # Step 4: Create clips
    for kw in matched_keywords:
        create_clip(
            recording_path=recording_file,
            keyword=kw,
            transcript_obj=transcript_obj,
            start_seconds=0,       # demo
            duration_seconds=120
        )

    print("[INFO] Pipeline completed!")
