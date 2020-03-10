from __future__ import unicode_literals
import csv, io
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .models import bank_details
from .forms import IFSC_Form, BNAME_BCITY_Form
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.core import serializers


from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework import generics, viewsets
from rest_framework import status


class upload_view(APIView):
    
    def post(self, request):
        data = {}
        csv_file = request.FILES["file"]
        file_data = csv_file.read().decode("utf-8")
        io_string = io.StringIO(file_data)
        next(io_string)
        for column in csv.reader(io_string, delimiter = ",", quotechar = "|"):
            _, created = bank_details.objects.update_or_create(
                ifsc = column[0],
                bank_id = column[1],
                branch = column[2],
                address = column[3],
                city = column[4],
                district = column[5],
                state = column[6],
                bank_name = column[7]
            )
        return render(request, './homepage.html')    


def show_ifsc(request):
    if request.method == 'POST':
        form = IFSC_Form(request.POST)
        if form.is_valid():
            ifsc = form.cleaned_data['ifsc_field']
            bank_branch = bank_details.objects.filter(ifsc__icontains = ifsc)
 #           bank_branch = serializers.serialize("json",bank_details.objects.filter(ifsc__icontains = ifsc))
        return render(request, './show_data.html', {'banks':bank_branch})
    else:
        form = IFSC_Form()
        return render(request, './ifsc_form.html', {'form': form})


def show_bname_bcity(request):
    if request.method == 'POST':
        form = BNAME_BCITY_Form(request.POST)
        if form.is_valid():
            bname = form.cleaned_data['bname_field']
            bcity = form.cleaned_data['bcity_field']
            bank_branch = bank_details.objects.filter(city__icontains = bcity).filter(bank_name__icontains = bname)          
        return render(request, './show_data.html', {'banks':bank_branch})
    else:
        form = BNAME_BCITY_Form()
        return render(request, './bname_bcity_form.html', {'form': form})

def show_branch(request):
        bank_branch = bank_details.objects.all()          
        return render(request, './show_data.html', {'banks':bank_branch})

def homepage(request):
    return render(request, "./homepage.html")

def upload_page(request):
    return render(request, './upload.html')