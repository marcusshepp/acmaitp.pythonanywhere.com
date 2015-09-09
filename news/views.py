from django.views.generic import View
from django.shortcuts import render

from .models import Update, Link


class UpdateFeed(View):

    template_name = 'news/updates.html'

    def get(self, request, *a, **kw):
        context = {}
        updates = Update.objects.all()[:5]
        links = Link.objects.all()[:5]
        context["updates"] = updates
        context["links"] = links
        return render(request, self.template_name, context)
