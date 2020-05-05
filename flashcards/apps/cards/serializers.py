from rest_framework import serializers
from apps.cards.models import Cards


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cards
        fields = ('id', 'question', 'answer', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')