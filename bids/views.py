from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Bids
from .forms import BidsForm
from artefacts.views import all_artefacts


#def get_bids(request):
#    """
#    Create a view that will return a list
#    of Relevant Bids For The Artefact
#    and render them to the 'bids.html' template
#    """
#    bids = Bids.objects.get()
#    return render(request, "make_bid.html", {'bids': bids})

def make_bid(request):
    """ Allows Customer To Make A bid On An Artefact """
    form = BidsForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(all_artefacts)
        else:
            form = BidsForm()
            return redirect(all_artefacts)
    return render(request, "make_bid.html", {'form': form})