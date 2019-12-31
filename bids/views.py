from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.utils import timezone
from decimal import *
from .models import Bids
from artefacts.models import Artefact
from customer.models import Customer
from .forms import BidsForm
from artefacts.views import for_sale_artefacts

def make_bid(request, pk):
    """ Allows Customer To Make A bid On An Artefact """
    
    """Get artefact, which user is bidding on"""
    artefact_bid = get_object_or_404(Artefact, pk=pk) if pk else None
    """get current user's information"""
    user = request.user
    """get current user's customer information"""
    customer = get_object_or_404(Customer, pk=user.customer.id) if pk else None
    
    try:
        """find the highest bid for the current artefact"""
        highest_bid = Bids.objects.filter(artefact_id=pk).latest('bid').bid
    except Bids.DoesNotExist:
        """if there are no bids, set the bid to zero"""
        highest_bid = 0.00

    form = BidsForm(request.POST, request.FILES)
  
    if request.method == "POST":
        """if the form input is valid"""
        if form.is_valid():
            """if the bid made is greater than the current one"""
            if (form.cleaned_data["bid"] > highest_bid) and (form.cleaned_data["bid"] > 0):
                """save the new highest bid with the customer and artefact info"""
                form = form.save(commit=False)
                form.customer_id = customer
                form.artefact_id = artefact_bid
                form.save()
                return redirect(for_sale_artefacts)
            else:
                """if bid is not greater than highest bid or zero/negative, then prompt user of this"""
                if (form.cleaned_data["bid"] <= highest_bid):
                    form.add_error(None, "Your bid must be greater than the current highest bid!")

                if (form.cleaned_data["bid"] <= 0):
                    form.add_error(None, "Your bid cannot be zero or negative!")
        else:
            form = BidsForm()
            return redirect(for_sale_artefacts)
            
    return render(request, "make_bid.html", {'form': form, 'highest_bid': highest_bid, 'artefact': artefact_bid})
