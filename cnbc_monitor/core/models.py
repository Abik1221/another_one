from django.db import models

class Keyword(models.Model):
    word = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.word

class Recording(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    file_path = models.CharField(max_length=255)

    def __str__(self):
        return f"Recording {self.id} - {self.created_at}"

class Transcript(models.Model):
    recording = models.ForeignKey(Recording, on_delete=models.CASCADE, related_name="transcripts")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transcript {self.id} ({self.created_at})"

class Clip(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.SET_NULL, null=True)
    transcript = models.ForeignKey(Transcript, on_delete=models.CASCADE, related_name="clips")
    file_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Clip {self.id} - {self.keyword}"
