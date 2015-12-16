from swampdragon.serializers.model_serializer import ModelSerializer


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = 'players.Player'
        publish_fields = ('position_x', 'position_y')
        update_fields = ('position_x', 'position_y')
