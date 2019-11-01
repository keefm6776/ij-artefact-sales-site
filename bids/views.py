from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm


def get_bids(request):
    """
    Create a view that will return a list
    of Relevant Bids For The Artefact
    and render them to the 'bids.html' template
    """
    bids = Bids.objects.filter(published_date__lte=timezone.now()).order_by('-date')
    return render(request, "bids.html", {'bids': bids})

def create_bid(request, pk=None):
    """
    Create a view that allows us to create
    a bid on the current Artefact
    """
    bids = get_object_or_404(Bids, pk=pk) if pk else None
    if request.method == "POST":
        form = BidsForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            bid = form.save()
            return redirect(bids, post.pk)
    else:
        form = BidsForm(instance=post)
    return render(request, 'bids.html', {'form': form})
