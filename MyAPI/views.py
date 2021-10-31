from django.shortcuts import render
from django.http import HttpResponse
from . import modelPredict
# Create your views here.


def index(request):
    return HttpResponse("index response")

def getPrediction(request):
    symptoms = []
    for i in range(100):
        symptom = request.GET.get(f"s{i}", "")
        if symptom == "" :
            break
        symptoms.append(symptom)

    return HttpResponse(modelPredict.predict(symptoms))
