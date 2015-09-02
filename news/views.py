from django.views.generic import View
from django.shortcuts import render

from .models import Update


class UpdateFeed(View):

    template_name = 'news/updates.html'

    def get(self, request, *a, **kw):
        context = {}
        updates = Update.objects.all()[:5]
        context["updates"] = updates
        return render(request, self.template_name, context)
