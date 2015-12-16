from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter

from .models import Player
from .serializers import PlayerSerializer


class PlayerRouter(ModelRouter):
    route_name = 'player'
    serializer_class = PlayerSerializer
    model = Player

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()

route_handler.register(PlayerRouter)
