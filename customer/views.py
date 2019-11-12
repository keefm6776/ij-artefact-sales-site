from django.shortcuts import render
from django.views.generic import DetailView, FormView
from django.db import models
from customer.models import Customer
from accounts.forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

class CreateCustomerView(FormView):
    template_name = 'register.html'
    form_class = UserRegistrationForm

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(username=data['username'],
                                        password=data['password'],
                                        email=data['email'],
                                        )
        user.customer.full_name = data['full_name']
        user.customer.street_Address1 = data['street_Address1']
        user.customer.street_Address2 = data['street_Address2']
        user.customer.town_or_city = data['town_or_city']
        user.customer.county = data['county']
        user.customer.country = data['country']
        user.customer.postcode = data['postcode']
        user.customer.phone_number = data['phone_number']
        user.customer.email = data['email']
        user.save()
        user.customer.save()

        return HttpResponse('ok')

class CustomerDetailView(DetailView):
    model = Customer