from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.views.generic import DetailView, FormView
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from customer.models import Customer
from customer.forms import CustomerForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.db import transaction


# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


#@login_required
@transaction.atomic
def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        customer_form = CustomerForm(request.POST)
        
        if user_form.is_valid():
            user_form.save()
            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))
            
            if user:
                auth.login(request, user)
                user.customer.full_name = request.POST.get('full_name')
                user.customer.street_Address1 = request.POST.get('street_Address1')
                user.customer.street_Address2 = request.POST.get('street_Address2')
                user.customer.town_or_city = request.POST.get('town_or_city')
                user.customer.county = request.POST.get('county')
                user.customer.country = request.POST.get('country')
                user.customer.postcode = request.POST.get('postcode')
                user.customer.phone_number = request.POST.get('phone_number')
                user.save()
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()
        customer_form = CustomerForm()

    args = {'user_form': user_form, 'customer_form' : customer_form}
    return render(request, 'register.html', args)

class CustomerDetailView(DetailView):
    model=Customer
