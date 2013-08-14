# Create your views here.
""" Views for the base application """

from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def dashboard(request):
    """ Default view for the root """
    return render(request, 'dashboard/dashboard.html')
