from rest_framework import generics
from apps.cards.serializers import CardSerializer
from apps.cards.models import Cards


class CreateCard(generics.ListCreateAPIView):
        queryset = Cards.objects.all()
        serializer_class = CardSerializer

        def perform_create(self, serializer):
            serializer.save()



class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Cards.objects.all()
    serializer_class = CardSerializer