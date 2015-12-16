from django.db import models
from swampdragon.models import SelfPublishModel
from django.contrib.auth.models import User

from .serializers import PlayerSerializer


class Player(SelfPublishModel, models.Model):
    serializer_class = PlayerSerializer
    user = models.ForeignKey(User)
    position_x = models.FloatField()
    position_y = models.FloatField()
