import csv
import os
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Note, MgfFile
from .serializers import NoteSerializer, MgfFileSerializer
from .utils.dataProcessing import read_mgf_file_and_return_first_n_spectra, data_processing_for_coding_task
from rest_framework.decorators import api_view

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class MgfFileViewSet(viewsets.ModelViewSet):
    queryset = MgfFile.objects.all()
    serializer_class = MgfFileSerializer

@api_view(['GET'])
def mgf_file_get_info(request, name):
    assets_folder_mfg_file_name = "assets/" + name + "/"
    mgf_info_file = assets_folder_mfg_file_name + name + "_info.csv"

    print(mgf_info_file)

    if not os.path.exists(mgf_info_file):
        data_processing_for_coding_task(mgf_file_path="../resources/sample_preprocessed_spectra.mgf",
                                        mztab_file_path="../resources/casanovo_20251029091517.mztab",
                                        sequence_metadata_csv_file_path="assets/sample_preprocessed_spectra/sample_preprocessed_spectra_info.csv",
                                        output_plot_path="media/output_iplots/")

    if not os.path.exists(mgf_info_file):
        return Response({'error': 'Csv file not found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    with open(mgf_info_file, mode='r', newline='') as f:
        info_csv_file = csv.DictReader(f)
        rows = list(info_csv_file)
    return Response(rows)

class ChartDataView(APIView):
    def get(self, request):

        data = read_mgf_file_and_return_first_n_spectra(mgf_file_path="../resources/sample_preprocessed_spectra.mgf", n=3)

        return Response(data)
