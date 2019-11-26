from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from artefacts.models import Artefact
from checkout.models import OrderLineItem, Order
from .forms import ArtefactForm
from weasyprint import HTML
    
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
            if form.cleaned_data["century"] > 0:
                form.save()
                return redirect(for_sale_artefacts)
            else:
                form.add_error(None, "The Century Cannot be negative or zero!")
        else:
            form = ArtefactForm()
            return redirect(for_sale_artefacts)
    return render(request, "add_artefact.html", {'form': form})
          
def edit_artefact_detail(request, id):
    """ Displays the selected Artefact to the Site Owner for editing """
    artefact = get_object_or_404(Artefact, pk=id)
    form = ArtefactForm(instance=artefact)

    if request.method == "POST":
        form = ArtefactForm(request.POST, instance=artefact)
        if form.is_valid():
            if form.cleaned_data["century"] > 0:
                form.save()
                return redirect(for_sale_artefacts)
            else:
                form.add_error(None, "The Century Cannot be negative or zero!")          
    else:
        form = ArtefactForm(instance=artefact)

    return render(request, "edit_artefact_detail.html", {'form': form})

def despatch_artefact(request, id):
    """ Marks the artefact as despatched, with despatched date """
    """ Sending html to a pdf file adapted from code at Simpleisbetterthancomplex.com"""
    
    artefact = get_object_or_404(Artefact, id=id)
    artefact.despatched = True
    artefact.despatch_date = timezone.now()
    artefact.save()

    order_line_info = OrderLineItem.objects.filter(artefact__pk=id)
    order_id = Order.objects.filter(orderlineitem=order_line_info)
    delivery = get_object_or_404(Order, pk=order_id)
                    
    artefact_info = {"name": artefact.name, "price": artefact.price, "order": delivery}
    html_string = render_to_string('../templates/despatch_template.html', {'artefact_info': artefact_info})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/despatch note.pdf');

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
