import os
import django

# Setup Django environment for standalone scripts
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cnbc_monitor.settings")
django.setup()

from core.models import Keyword, Transcript

def detect_keywords(transcript_obj: Transcript):
    """
    Scan a Transcript object for keywords in the database.
    Returns a list of matched Keyword objects.
    """
    text = transcript_obj.text.lower()
    matched_keywords = []

    for keyword in Keyword.objects.all():
        if keyword.word.lower() in text:
            matched_keywords.append(keyword)
            print(f"[INFO] Found keyword: {keyword.word}")

    return matched_keywords

# Example usage
if __name__ == "__main__":
    from core.models import Transcript

    # Pick the latest transcript for demo
    latest_transcript = Transcript.objects.latest('created_at')
    matched = detect_keywords(latest_transcript)
    print(f"[INFO] Keywords found: {[k.word for k in matched]}")
