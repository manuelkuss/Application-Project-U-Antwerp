from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class ChartDataView(APIView):
    def get(self, request):

        data = {
            "labels": ["January", "February", "March", "April"],
            "values": [10, 20, 15, 30],
            "metadata": {
                "generated_by": "ChartDataView",
                "status": "success"
            }
        }

        return Response(data)
