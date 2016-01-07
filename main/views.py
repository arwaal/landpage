from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Landpage, Users
from main.forms import UserSignup
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.template import RequestContext



# Create your views here.

def home_view(request): 
    trial = Landpage.objects.all()
    context = {}
    context['trial'] = trial
    return render(request, 'landpage.html', context)

def signup(request):
    context = {}
    form = UserSignup()
    context['form'] = form
    if request.method == 'POST':
        form = UserSignup(request.POST)
        context['form'] = form
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            mobile = form.cleaned_data['mobile']
            # gender = form.cleaned_data['gender']
            # date_of_birth = form.cleaned_data['date_of_birth']
            # password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            # the_user = User.objects.create_user(first_name, last_name, email)
            # the_user.last_name = last_name
            # the_user.save()
            regular_user, created = Users.objects.get_or_create(first_name=first_name, last_name=last_name, mobile=mobile, email=email)
            regular_user.save()
            return HttpResponse ('Thank You! We Will Contact You Soon')

    elif request.method == 'GET':
        context['valid'] = form.errors 

    else:
        HttpResponse('Error')

    return render_to_response('signup.html', context, context_instance=RequestContext(request))
