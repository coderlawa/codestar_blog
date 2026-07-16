from django.shortcuts import render
from .models import About
from .forms import CollaborateForm


def about_me(request):
    """
    Renders the About Page with the latest About information and a collaboration form.
    """

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )