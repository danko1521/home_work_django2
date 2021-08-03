import csv
import urllib

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

rows = []


def index(request):
    return redirect(reverse(bus_stations))


def read_cvs(file_name):
    rows = []
    with open(file_name, 'r', encoding="cp1251") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows


def bus_stations(request):
    CONTENT = read_cvs('data-398-2018-08-30.csv')

    paginator = Paginator(CONTENT, 10)
    page_number = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(page_number)
    current_page = page_obj.number

    prev_page_url=None
    next_page_url=None

    url = f'{reverse(bus_stations)}?'
    if page_obj.has_previous():

       prev_page_url = url+urllib.parse.urlencode({'page': page_obj.previous_page_number()})
    if page_obj.has_next():

        next_page_url = url+urllib.parse.urlencode({'page':page_obj.next_page_number()})


    return render(request, 'index.html', context={
        'bus_stations': page_obj,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,})