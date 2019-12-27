from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import RequestContext
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem, Order
from customer.models import Customer
from django.conf import settings
from django.utils import timezone
from artefacts.models import Artefact
import stripe

# Create your views here.
# Taken & Adpated From Code Institute Course Notes

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request, id):
    """get customer object for current user"""
    customer_object = get_object_or_404(Customer, pk=id)
    """initialise order and makepayment forms"""
    order_form = OrderForm(request.POST)
    payment_form = MakePaymentForm(request.POST)

    if request.method == "POST":
        """ if both order form and payment forms are valid """
        if order_form.is_valid() and payment_form.is_valid():
            """save order information with date and customer info"""
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.customer_id = customer_object
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                """Total order amount"""
                artefact = get_object_or_404(Artefact, pk=id)
                total += quantity * artefact.price
                order_line_item = OrderLineItem(
                    order=order,
                    artefact=artefact,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                """try charging customer card/address details with amount due"""
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                """ on exception prompt user that card was declined"""
                messages.error(request, "Your card was declined!")

            if customer.paid:
                """ on successful payment, prompt user that they have paid """
                messages.error(request, "You have successfully paid")
                
                for id,quantity in cart.items():
                    """ for artefacts in cart, mark as sold when payment is successful """
                    artefact = get_object_or_404(Artefact, pk=id)
                    artefact.sold = True
                    artefact.save()
                    request.session['cart'] = {}
                return redirect(reverse('for_sale_artefacts'))
            else:
                """ if payment did not go through prompt user that it was not successful """
                messages.error(request, "Unable to take payment")
        else:
            """ if payment/customer forms are not valid, prompt user"""
            print(payment_form.errors)
            messages.error(
                request, "We were unable to take a payment with that card!")
    else:
        """ Initialising paymemnt form to User Customer Details adapted from code at StackOverFlow.com"""
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        data = {'delivery_full_name': customer_object.full_name, 'delivery_street_address1': customer_object.street_Address1, 
                'delivery_street_address2': customer_object.street_Address2, 'delivery_town_or_city': customer_object.town_or_city, 
                'delivery_county': customer_object.county, 'delivery_country': customer_object.country, 
                'delivery_postcode': customer_object.postcode, 'delivery_phone_number' : customer_object.phone_number, 
                'delivery_email': customer_object.email }
        order_form = OrderForm(initial=data)

    return render(request, "checkout.html", {"order_form": order_form, "user": request.user, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
