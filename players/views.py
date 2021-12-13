from django.shortcuts import render
from .models import match , Squad
from Squadinfo.mixins import value_stored

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

# Create your views here.
def home_view(requests):
    # if requests.method == 'post':
    #     code = requests.POST.get('match_id')
    # if this is a POST request we need to process the form data
    if requests.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(requests.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            url = form.cleaned_data['your_name']
            value_stored(url)
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    squad = match.objects.all()
    con = {
        'mat': squad,
        'form': form
    }
    return render(requests,'home.html',con)

def Squad_view(requests):

    mat = Squad.objects.all()
    con = {
        'mat': mat
    }
    return render(requests,'home.html',con)


