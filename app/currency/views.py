from django.shortcuts import render
from currency.models import Registrator
from currency.form import RegForms
from currency.login_gen import log_gen, pass_gen, mails_gen
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import TemplateView


class RegIndexViews(TemplateView):
    template_name = "index.html"


class RegCreateViews(CreateView):
    model = Registrator
    form_class = RegForms
    template_name = "r_create.html"
    success_url = '/r_read'


class RegReadViews(ListView):
    model = Registrator
    template_name = "r_read.html"


class RegUpdateViews(UpdateView):
    model = Registrator
    form_class = RegForms
    template_name = "r_update.html"
    success_url = '/r_read'


class RegDeleteViews(DeleteView):
    model = Registrator
    template_name = "r_delete.html"
    success_url = '/r_read/'


class RegDetailsViews(DetailView):
    model = Registrator
    template_name = "r_details.html"


class RandomLoginsViews(TemplateView):
    template_name = "logins_gen.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        log = log_gen()
        result = Registrator.objects.create(
            login=log,
            passwords=pass_gen(),
            mails=mails_gen(log),
        )
        context["random_user"] = result
        return context


class ClearRegsViews(TemplateView):
    template_name = "delete_base.html"

    def get_context_data(self, **kwargs):
        Registrator.objects.all().delete()
