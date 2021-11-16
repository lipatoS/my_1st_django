from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from currency.form import RegForms
from currency.models import Registrator


def hello_world(request):
    return HttpResponse("+++++++++")


def index(request):
    return render(request, "index.html")


def r_create(request):
    if request.method == 'POST':
        form = RegForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/r_read/')
    elif request.method == "GET":
        forms = RegForms()
    text = {"form": forms}
    return render(request, "r_create.html", context=text)


def r_read(request):
    regs = Registrator.objects.all()
    text = {"message": regs}
    return render(request, "r_read.html", context=text)


def r_update(request, reg_id):
    reg = get_object_or_404(Registrator, id=reg_id)
    if request.method == 'POST':
        form = RegForms(request.POST, instance=reg)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/r_read/')
    elif request.method == "GET":
        forms = RegForms(instance=reg)
    text = {"form": forms}

    return render(request, "r_update.html", context=text)


def r_details(request, reg_id):
    reg = get_object_or_404(Registrator, id=reg_id)
    text = {"object": reg}
    return render(request, "r_details.html", context=text)


def r_delete(request, reg_id):
    reg = get_object_or_404(Registrator, id=reg_id)
    if request.method == 'POST':
        reg.delete()
        return HttpResponseRedirect('/r_read/')
    text = {"object": reg}

    return render(request, "r_delete.html", context=text)
