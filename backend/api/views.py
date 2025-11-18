import csv
import os
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Note, MgfFile
from .serializers import NoteSerializer, MgfFileSerializer
from .utils.dataProcessing import read_mgf_file_and_return_first_n_spectra, data_processing_for_coding_task
from rest_framework.decorators import api_view

RESOURCES_PATH = "../resources/"
ASSETS_PATH = "assets/"
MEDIA_PATH = "media/"
MGF_FILE_SUFFIX = ".mgf"
MZTAB_FILE_SUFFIX = ".mztab"
CSV_FILE_SUFFIX = ".csv"

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class MgfFileViewSet(viewsets.ModelViewSet):
    queryset = MgfFile.objects.all()
    serializer_class = MgfFileSerializer

@api_view(['GET'])
def mgf_file_get_info(request, name):
    assets_folder_mfg_file_name = ASSETS_PATH + name + "/"
    mgf_info_file_path = assets_folder_mfg_file_name + name + CSV_FILE_SUFFIX

    try:
        if not os.path.exists(mgf_info_file_path):
            mgfFile: MgfFile = MgfFile.objects.all().filter(name__exact=name).first()
            casanovo_file_name = mgfFile.casanovo_file_name

            mgf_file_path = RESOURCES_PATH + name + MGF_FILE_SUFFIX
            casanovo_file_path = RESOURCES_PATH + casanovo_file_name + MZTAB_FILE_SUFFIX
            csv_info_file_path = mgf_info_file_path
            iplots_output_path = MEDIA_PATH + "output_iplots/" + name + "/"

            if not os.path.exists(iplots_output_path):
                os.mkdir(iplots_output_path)

            data_processing_for_coding_task(mgf_file_path=mgf_file_path,
                                            mztab_file_path=casanovo_file_path,
                                            info_csv_file_path=csv_info_file_path,
                                            output_plot_path=iplots_output_path)
    except Exception:
        return Response({'error': 'CSV file does not exist and could not be generated.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    with open(mgf_info_file_path, mode='r', newline='') as f:
        info_csv_file = csv.DictReader(f)
        rows = list(info_csv_file)
    return Response(rows)

class ChartDataView(APIView):
    def get(self, request):
        mgfFileName = MgfFile.objects.all().first().name
        mgfFilePath = RESOURCES_PATH + mgfFileName + MGF_FILE_SUFFIX

        data = read_mgf_file_and_return_first_n_spectra(mgf_file_path=mgfFilePath, n=3)

        return Response(data)
