from django.contrib.auth.models import User

from game.celery import app

from .models import Item


@app.task
def give_gift():
    for user in User.objects.iterator():
        item = Item.objects.create(
            name='Gift for {}'.format(user.username), weight=0)
        user.inventory.items.add(item)
