import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from mainapp.models import Kitchen


@csrf_exempt
def index(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode())
        kitchen_list = []

        for kitchen in body:
            kitchen_list.append(Kitchen(**kitchen))

        Kitchen.objects.bulk_create(kitchen_list)

    return render(request, 'index.html')
