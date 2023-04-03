from rest_framework import viewsets
from .models import *
from django.views.generic import TemplateView
import pandas as pd
import io
from django.shortcuts import render
from .csv_proccesor import process_csv
import os
from django.http import HttpResponse


class CsvUploader(TemplateView):
    template_name = 'csv_uploader.html'

    def post(self, request):
        context = {
            'messages': []
        }
        csv = request.FILES['csv']
        print(csv)
        output = process_csv(csv, 'out.csv')
        # Save the new CSV file to a temporary file
        temp_file = 'temp.csv'
        output.to_csv(temp_file, index=False)

        # Open the temporary file and read its contents
        with open(temp_file, 'r') as f:
            csv_data = f.read()
            print(csv_data)

        # Delete the temporary file
        os.remove(temp_file)

        # Create an HttpResponse object with the new CSV data and content-disposition header
        response = HttpResponse(csv_data, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="my_data.csv"'
        return response

