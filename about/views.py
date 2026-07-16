from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_me(request):
    """
    Renders the About Page with the latest About information and a collaboration form.
    """

    if request.method == "POST":
        print("Received a POST request from collaboration form")
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                "Collaboration request received! I try to respond within 2 working days.")

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
    print("Rendering the About page template with context data")

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )