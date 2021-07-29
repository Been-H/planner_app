from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
import datetime

def landing_view(request, *args, **kwargs):
    return render(request, 'index.html')