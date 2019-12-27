from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
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
    current_user = request.user
    return render(request, "index.html")

def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))

def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        """ initiate login form to take username/email & password """
        user_form = UserLoginForm(request.POST)
        """ If the user form is filled in a valid way """
        if user_form.is_valid():
            """authenticate the user"""
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            """ if user stated exists"""
            if user:
                """log in the user"""
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                """if user does not exist of password is not correct, prompt user"""
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)

@login_required
def profile(request, id):
    """A view that displays the profile page of a logged in user"""

    """get USer object for the user currently logged in """
    customer = get_object_or_404(Customer, pk=id)
    """create a customer form, pre-filled with the current user's info"""
    form = CustomerForm(instance=customer)
     
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            """If form is valid, save it"""
            form = form.save()
            """return to the profile page with the current user info displayed"""
            return redirect(profile, id)
        else:
            form = CustomerForm(instance=customer)
    return render(request, "profile.html", {'form': form})

@transaction.atomic
def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        """create form for the user object and the customer object"""
        user_form = UserRegistrationForm(request.POST)
        customer_form = CustomerForm(request.POST)
        
        if user_form.is_valid():
            """if the user from information is valid, save it and authenticate user"""
            user_form.save()
            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))
            
            if user:
                """if user is valid log them in and update their user profile from 
                    registration information"""
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
                """if there is an error in information/logging prompt user that they
                    cannot be logged in"""
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()
        customer_form = CustomerForm()

    args = {'user_form': user_form, 'customer_form' : customer_form}
    """pass user form informtion and customer form information to the registration to the register.html"""
    return render(request, 'register.html', args)

class CustomerDetailView(DetailView):
    model=Customer
