from django.shortcuts import render
from artefacts.models import Artefact

# Create your views here.
def do_search(request):
    artefacts = Artefact.objects.filter(name__icontains=request.GET['q'])
    return render(request, "artefacts.html", {"artefacts": artefacts})