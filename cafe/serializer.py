from rest_framework import serializers


class OrderResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    cafe_id = serializers.IntegerField()
    customer_id = serializers.IntegerField()
