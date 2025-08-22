from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import Clip
from core.tasks import pipeline  # import the full pipeline

def dashboard(request):
    if request.method == "POST":
        # Run the full pipeline
        try:
            pipeline.run_pipeline()  # call a function that orchestrates everything
            messages.success(request, "Pipeline executed successfully!")
        except Exception as e:
            messages.error(request, f"Error running pipeline: {e}")
        return redirect('dashboard')

    clips = Clip.objects.all().order_by('-created_at')
    return render(request, 'core/dashboard.html', {'clips': clips})
