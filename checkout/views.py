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
# Taken From Code Institute Course Notes

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request, id):
    customer = get_object_or_404(Customer, pk=id)
    order_form = OrderForm(request.POST)
    payment_form = MakePaymentForm(request.POST)

    if request.method == "POST":
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                artefact = get_object_or_404(Artefact, pk=id)
                total += quantity * artefact.price
                order_line_item = OrderLineItem(
                    order=order,
                    artefact=artefact,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                artefact.sold = True
                artefact.save()
                return redirect(reverse('artefact'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(
                request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        data = {'delivery_full_name': customer.full_name, 'delivery_street_address1': customer.street_Address1, 'delivery_street_address2': customer.street_Address2, 'delivery_town_or_city': customer.town_or_city, 'delivery_county': customer.county, 'delivery_country': customer.country, 'delivery_postcode': customer.postcode, 'delivery_phone_number': customer.phone_number, 'delivery_email':customer.email }
        order_form = OrderForm(initial=data)

    return render(request, "checkout.html", {"order_form": order_form, "user": request.user, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
