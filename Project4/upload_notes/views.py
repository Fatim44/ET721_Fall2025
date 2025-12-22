from django.shortcuts import render, redirect
from .models import NoteImage
from .forms import NoteImageForm

def notes_list(request):
    notes = NoteImage.objects.order_by("-uploaded_at")
    form = NoteImageForm()

    if request.method == "POST":
        form = NoteImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("notes_list")

    return render(request, "upload_notes/notes_list.html", {"notes": notes, "form": form})
