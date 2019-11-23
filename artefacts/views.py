from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from artefacts.models import Artefact
from .forms import ArtefactForm

# Create your views here.

def for_sale_artefacts(request):
    """ Finds all unsold artefacts in the database and displays them """
    artefacts = Artefact.objects.filter(sold=False)
    return render(request, "artefacts.html", {"artefacts": artefacts})

def sold_artefacts(request):
    """ Finds all sold artefacts in the database and displays them """
    artefacts = Artefact.objects.filter(sold=True, despatched=False)
    return render(request, "artefacts_sold.html", {"artefacts": artefacts})

def despatched_artefacts(request):
    """ Finds all sold artefacts in the database and displays them """
    artefacts = Artefact.objects.filter(despatched=True)
    return render(request, "artefacts_despatched.html", {"artefacts": artefacts})

def artefact_detail(request, pk):
    """ Displays all the artefact details to the user """
    artefact = get_object_or_404(Artefact, pk=pk)
    return render(request, "artefact_detail.html", {"artefact": artefact})

def add_artefact(request):
    """ Allows Site Owner To Add New Artefact To Sell """
    form = ArtefactForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(all_artefacts)
        else:
            form = ArtefactForm()
            return redirect(all_artefacts)
    return render(request, "add_artefact.html", {'form': form})

def edit_artefact_detail(request, id):
    """ Displays the selected Artefact to the Site Owner for editing """
    artefact = get_object_or_404(Artefact, pk=id)
    form = ArtefactForm(instance=artefact)

    if request.method == "POST":
        form = ArtefactForm(request.POST, instance=artefact)
        if form.is_valid():
            form.save()
            return redirect(all_artefacts)
    else:
        form = ArtefactForm(instance=artefact)

    return render(request, "edit_artefact_detail.html", {'form': form})

def despatch_artefact(request, id):
    """ Makrs the artefact as despatched, with despatched date """
    artefact = get_object_or_404(Artefact, id=id)
    artefact.despatched = True
    artefact.despatch_date = timezone.now()
    artefact.save()

    #if request.method == "POST":
    #    form = ArtefactForm(request.POST, instance=artefact)
    #    if form.is_valid():
    #        form.save()
    #        return redirect(all_artefacts)
    #else:
    #    form = ArtefactForm(instance=artefact)
    
    artefacts = Artefact.objects.filter(despatched=True)
    return render(request, "artefacts_despatched.html", {"artefacts": artefacts})

def delete_artefact(request, pk):
    """ Allows the Site Owner to delete the current artefact """
    artefact = get_object_or_404(Artefact, pk=pk)
    return redirect(all_artefacts)
