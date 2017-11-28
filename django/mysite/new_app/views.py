from django.shortcuts import render
from django.views.generic import TemplateView


class ShowTemplateView(TemplateView):

    def get(self, request):
        return render(request, "template.html")
