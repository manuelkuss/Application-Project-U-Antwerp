from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Note
from .serializers import NoteSerializer
from .utils.dataProcessing import read_mgf_file_and_return_first_n_spectra

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class ChartDataView(APIView):
    def get(self, request):

        data = read_mgf_file_and_return_first_n_spectra(3)

        return Response(data)
