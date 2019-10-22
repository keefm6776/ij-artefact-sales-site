from django.shortcuts import render, get_object_or_404
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