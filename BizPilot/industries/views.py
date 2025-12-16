"""
from rest_framework import generics
from .models import Industry
from .serializers import IndustrySerializer

class IndustryListView(generics.ListAPIView):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer

"""
