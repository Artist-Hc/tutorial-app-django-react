from django.shortcuts import render
from .models import Tutorial
from .serializers import TutorialSerializer
from rest_framework.viewsets import ModelViewSet


class TutorialVeiw(ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
    
