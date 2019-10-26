from django.shortcuts import render, get_object_or_404, redirect
from artefacts.models import Artefact

# Create your views here.

def all_artefacts(request):
    """ Finds all artefacts in the database and displays them """
    artefacts = Artefact.objects.all()
    return render(request, "artefacts.html", {"artefacts": artefacts})

def artefact_detail(request, pk):
    """ Displays all the artefact details to the user """
    artefact = get_object_or_404(Artefact, pk=pk)
    return render(request, "artefact_detail.html", {"artefact" : artefact})

def add_artefact(request):
    """ Allows Site Owner To Add New Artefact To Sell """
    if request.method == "POST":
        new_artefact = Artefact()
        new_artefact.name = request.POST.get("name")
        new_artefact.history = request.POST.get("history")
        new_artefact.description = request.POST.get("description")
        new_artefact.century = request.POST.get("century")
        new_artefact.era = request.POST.get("era")
        new_artefact.image = request.POST.get("image")
        new_artefact.price = request.POST.get("price")
        new_artefact.save()
        return redirect(all_artefacts)

    return render(request, "add_artefact.html")