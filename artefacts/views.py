from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from bids.models import Bids
from artefacts.models import Artefact
from checkout.models import OrderLineItem, Order
from .forms import ArtefactForm
from weasyprint import HTML
from operator import itemgetter

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def for_sale_artefacts(request):
    """ Finds all unsold artefacts in the database and displays them,
        newest first """
    artefacts = Artefact.objects.filter(sold=False).order_by('-id')

    """initiate paginator"""
    page = request.GET.get('page', 1)
    paginator = Paginator(artefacts, 10)

    try:
        artefacts = paginator.page(page)
    except PageNotAnInteger:
        artefacts = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, "artefacts.html", {"artefacts": artefacts})


def sold_artefacts(request):
    """ Finds all sold artefacts (not despatched) in the database and displays them,
        newest first"""
        
    artefacts = Artefact.objects.filter(sold=True, despatched=False).order_by('-id')

    """inititate paginator"""
    page = request.GET.get('page', 1)
    paginator = Paginator(artefacts, 10)

    try:
        artefacts = paginator.page(page)
    except PageNotAnInteger:
        artefacts = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, "artefacts_sold.html", {"artefacts": artefacts})


def despatched_artefacts(request):
    """ Finds all sold artefacts that have been despatched in the 
    database and displays them """
    artefacts = Artefact.objects.filter(despatched=True).order_by('-id')

    """initiate paginator"""
    page = request.GET.get('page', 1)
    paginator = Paginator(artefacts, 10)

    try:
        artefacts = paginator.page(page)
    except PageNotAnInteger:
        artefacts = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, "artefacts_despatched.html", {"artefacts": artefacts})


def artefact_detail(request, pk):
    """ Displays all the details of the selected artefact to the user """
    artefact = get_object_or_404(Artefact, pk=pk)
    return render(request, "artefact_detail.html", {"artefact": artefact})


def add_artefact(request):
    """ Allows Site Owner To Add New Artefact To Sell """
    form = ArtefactForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            """If century and price are valid, ie not zero or -ve"""
            if ((form.cleaned_data["century"] > 0) and (form.cleaned_data["price"] > 0) and (form.cleaned_data["name"] != '')):
                form.save()
                return redirect(for_sale_artefacts)
            else:
                if (form.cleaned_data["century"] <= 0):
                    form.add_error(None, "The Century Cannot be negative or zero!")
                if (form.cleaned_data["price"] <= 0):
                    form.add_error(None, "The Price Set Cannot be negative or zero!")      
                if (form.cleaned_data["name"] == ''):
                    form.add_error(None, "The name field cannot be left blank!")
                         
        else:
            form = ArtefactForm()
            return redirect(for_sale_artefacts)
    return render(request, "add_artefact.html", {'form': form})


def edit_artefact_detail(request, id):
    """ Displays the selected Artefact to the Site Owner for editing """
    artefact = get_object_or_404(Artefact, pk=id)
    """create form with selected artefact's details displayed"""
    form = ArtefactForm(instance=artefact)

    if request.method == "POST":
        form = ArtefactForm(request.POST, instance=artefact)
        if form.is_valid():
            """If century and price are valid, ie not zero or -ve"""
            if ((form.cleaned_data["century"] > 0) and (form.cleaned_data["price"] > 0) and (form.cleaned_data["name"] != '') and (form.cleaned_data["description"] != '') and (form.cleaned_data["history"] != '') and ((form.cleaned_data["era"] == 'AD') or (form.cleaned_data["AD"] == 'BC'))):
                form.save()
                return redirect(for_sale_artefacts)
            else:
                if (form.cleaned_data["century"] <= 0):
                    form.add_error(None, "The Century Cannot be negative or zero!")
                if (form.cleaned_data["price"] <= 0):
                    form.add_error(None, "The Price Set Cannot be negative or zero!")
                if (form.cleaned_data["name"] == ''):
                    form.add_error(None, "The name field cannot be left blank!")
                if (form.cleaned_data["description"] == ''):
                    form.add_error(None, "The description field cannot be left blank!") 
                if (form.cleaned_data["history"] == ''):
                    form.add_error(None, "The history field cannot be left blank!") 
                if ((form.cleaned_data["era"] != 'AD') and (form.cleaned_data["era"] != 'BC')):
                    form.add_error(None, "The era can only be AD (Anno Domini) or BC (Before Christ)!")
    else:
        form = ArtefactForm(instance=artefact)

    return render(request, "edit_artefact_detail.html", {'form': form})


def despatch_artefact(request, id):
    """ Marks the artefact as despatched, with despatched date """
    """ Sending html to a pdf file adapted from code at Simpleisbetterthancomplex.com"""

    artefact = get_object_or_404(Artefact, id=id)
    """set despatched to true"""
    artefact.despatched = True
    """mark the despatched date as today"""
    artefact.despatch_date = timezone.now()
    artefact.save()

    """find the order line which includes the despatching artefact"""
    order_line_info = OrderLineItem.objects.filter(artefact__pk=id)
    """find the order details for this artefact"""
    order_id = Order.objects.filter(orderlineitem=order_line_info)
    """get the delivery details for this artefact"""
    delivery = get_object_or_404(Order, pk=order_id)

   
    """Create despatch note in pdf format, for printing/daving"""
    artefact_info = {"name": artefact.name,
                     "price": artefact.price, "order": delivery}
    html_string = render_to_string(
        '../templates/despatch_template.html', {'artefact_info': artefact_info})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/despatch note.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('despatch note.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="despatch note.pdf"'
        return response

    artefacts = Artefact.objects.filter(despatched=True)
    return render(request, "artefacts_despatched.html", {"artefacts": artefacts})


def delete_artefact(request, id):
    """ Allows the Site Owner to delete the current artefact """
    Artefact.objects.filter(id=id).delete()
    return redirect(for_sale_artefacts)

def past_orders(request):
    """ Allows the Customer to view their previous orders """
    current_user=request.user
    user_orders = Order.objects.filter(customer_id=current_user.id)
    past_orders = OrderLineItem.objects.filter(order_id__in=list(user_orders))
    
    no_of_orders = len(list(past_orders))

    return render(request, "past_orders.html", {"artefacts": past_orders, "no_or_orders": no_of_orders})