from django.shortcuts import render
from artefacts.models import Artefact

def do_search_for_sale(request):
    """find artefacts that are for sale, that meet search criteria between centuries stated
        with the given name and era"""
    artefacts = Artefact.objects.filter(sold=False, despatched=False, century__gte=request.GET['low_artefact_century'], century__lte=request.GET['high_artefact_century'], name__icontains=request.GET['artefact_name'], era__icontains=request.GET['artefact_era'])
    return render(request, "artefacts.html", {"artefacts": artefacts})

def do_search_sold(request):
    """find artefacts that are sold, that meet search criteria between centuries stated
        with the given name and era"""
    artefacts = Artefact.objects.filter(sold=True, despatched=False, century__gte=request.GET['low_artefact_century'], century__lte=request.GET['high_artefact_century'], name__icontains=request.GET['artefact_name'], era__icontains=request.GET['artefact_era'])
    return render(request, "artefacts_sold.html", {"artefacts": artefacts})

def do_search_despatched(request):
    """find artefacts that are sold & despatached, that meet search criteria between centuries stated
        with the given name and era"""
    artefacts = Artefact.objects.filter(sold=True, despatched=True, century__gte=request.GET['low_artefact_century'], century__lte=request.GET['high_artefact_century'], name__icontains=request.GET['artefact_name'], era__icontains=request.GET['artefact_era'])
    return render(request, "artefacts_despatched.html", {"artefacts": artefacts})   