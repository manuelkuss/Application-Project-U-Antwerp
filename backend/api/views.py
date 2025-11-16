import csv
import os

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Note, Sequence, MgfFile
from .serializers import NoteSerializer, SequenceSerializer, MgfFileSerializer
from .utils.dataProcessing import read_mgf_file_and_return_first_n_spectra, data_processing_for_coding_task, get_plotly_data_for_sequence
from rest_framework.decorators import api_view

CSV_FILE = 'api/utils/sequence_metadata.csv'

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class ChartDataView(APIView):
    def get(self, request):

        data = read_mgf_file_and_return_first_n_spectra(mgf_file_path="../resources/sample_preprocessed_spectra.mgf", n=3)

        return Response(data)


@api_view(['GET'])
def sequence_get_plotly_data(request, id):
    return Response(get_plotly_data_for_sequence(
        mgf_file_path="../resources/sample_preprocessed_spectra.mgf",
        mztab_file_path="../resources/casanovo_20251029091517.mztab",
        id=id))

@api_view(['GET'])
def sequence_get(request, id):
    # try:
    #     sequence = Sequence.objects.get(id=id)
    # except Sequence.DoesNotExist:
    #     return Response({'error': 'Sequence not found'}, status=status.HTTP_404_NOT_FOUND)
    #
    # serializer = SequenceSerializer(sequence)
    # return Response(serializer.data)


    if not os.path.exists(CSV_FILE):
        data_processing_for_coding_task(mgf_file_path="../resources/sample_preprocessed_spectra.mgf",
                                        mztab_file_path="../resources/casanovo_20251029091517.mztab",
                                        sequence_metadata_csv_file_path="assets/sample_preprocessed_spectra/sample_preprocessed_spectra.csv",
                                        output_plot_path="media/output_plots/")

        if not os.path.exists(CSV_FILE):
            return Response({'error': 'Metadata file not found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Read CSV and search for the ID
    with open(CSV_FILE, mode='r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if str(row['id']) == str(id):  # CSV fields are strings
                return Response(row)
                # return Response({'id': int(row['id']), 'title': row['title'], 'sequence': row['sequence'], 'metadata': row})

    # If ID not found
    return Response({'error': 'Sequence not found'}, status=status.HTTP_404_NOT_FOUND)

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
                                        output_plot_path="media/output_plots/")

    if not os.path.exists(mgf_info_file):
        return Response({'error': 'Csv file not found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    with open(mgf_info_file, mode='r', newline='') as f:
        info_csv_file = csv.DictReader(f)
        rows = list(info_csv_file)
    print("response: ", len(rows))
    # print("response: ", rows[1])
    return Response(rows)
