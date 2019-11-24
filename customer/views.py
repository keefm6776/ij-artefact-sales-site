from django.shortcuts import render
from django.views.generic import DetailView, FormView
from django.db import models
from customer.models import Customer
from .forms import CustomerForm
from accounts.forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Extending User Model with Customer Model adapted from code at Simpleisbetterthancomplex.com
@login_required
@transaction.atomic
def customer_profile(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, instance=request.user)
        customer_form = CustomerForm(request.POST, instance=request.user.customer)

        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            messages.success(request, _('Your Profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserRegistrationForm(instance=request.user)
        customer_form = CustomerForm(instance=request.user.customer)
    return render(request, 'profiles/profile.html', {
        'user_form' : user_form,
        'customer_form' : customer_form
    })