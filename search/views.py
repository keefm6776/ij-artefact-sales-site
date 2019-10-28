from django.shortcuts import render
from artefacts.models import Artefact

# Create your views here.
def do_search(request):
    #artefacts = Artefact.objects.filter(name__icontains=request.GET['q'])
    artefacts = Artefact.objects.filter(century__gte=request.GET['low_artefact_century'], century__lte=request.GET['high_artefact_century'], name__icontains=request.GET['artefact_name'], era__icontains=request.GET['artefact_era'])

    return render(request, "artefacts.html", {"artefacts": artefacts})