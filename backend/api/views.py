import csv
import os

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Note, Sequence
from .serializers import NoteSerializer, SequenceSerializer
from .utils.dataProcessing import read_mgf_file_and_return_first_n_spectra, data_processing_for_coding_task
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
                                        sequence_metadata_csv_file_path="api/utils/sequence_metadata.csv",
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