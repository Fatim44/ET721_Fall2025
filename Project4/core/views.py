from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    # Example context data (replace with real queries later)
    context = {
        'welcome_message': f"Welcome back, {request.user.username}!",
        'tasks_count': 5,      # Replace with Task.objects.filter(user=request.user).count()
        'notes_count': 12,     # Replace with Note.objects.filter(user=request.user).count()
        'posts_count': 3,      # Replace with Post.objects.filter(user=request.user).count()
    }
    
    return render(request, 'core/home.html', context)