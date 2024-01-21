from rest_framework import serializers
from main.models import Events

from profiling.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class EventsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    object_info = ItemSerializer(source="object", read_only=True)
    user_receiver = serializers.SerializerMethodField()

    class Meta:
        model = Events
        fields = "__all__"

    def get_user(self, obj):
        user_data = {
            "id": obj.user.id,
            "username": obj.user.username,
            "first_name": obj.user.first_name,
            "avatar": obj.user.avatar.url,
        }
        return user_data

    def get_user_receiver(self, obj):
        user_receiver_data = {
            "id": obj.user_receiver.id,
            "username": obj.user_receiver.username,
            "first_name": obj.user_receiver.first_name,
        }
        return user_receiver_data
