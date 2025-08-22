from django.contrib import admin
from .models import Keyword, Recording, Transcript, Clip

admin.site.register(Keyword)
admin.site.register(Recording)
admin.site.register(Transcript)
admin.site.register(Clip)
