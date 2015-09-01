from django.contrib.syndication.views import Feed

from .models import Update


class UpdateFeed(Feed):

    title = "ACM/AITP Updates"
    description_template = 'news/updates.html'
    link = "/"

    def items(self):
        return Update.objects.order_by("-datetime")[:3]

    def item_title(self, item):
        return "{0}: {1}".format(item.where, item.when)

    def item_description(self, item):
        return item.what
