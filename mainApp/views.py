from rest_framework import viewsets
from .models import *
from .serializers import *
from django.views.generic import TemplateView
import pandas as pd
import io
from django.shortcuts import render

class StudentsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer
    queryset = Students.objects.all()

class CsvUploader(TemplateView):
    template_name = 'csv_uploader.html'

    def post(self, request):
        context = {
            'messages':[]
        }

        csv = request.FILES['csv']
        csv_data = pd.read_csv(
            io.StringIO(
                csv.read().decode("utf-8")
            )
        )

        for record in csv_data.to_dict(orient="records"):
            try:
                Students.objects.create(
                    first_name = record['first_name'],
                    last_name = record['last_name'],
                    marks = record['marks'],
                    roll_number = record['roll_number'],
                    section = record['section']
                )
            except Exception as e:
                context['exceptions_raised'] = e
                
        return render(request, self.template_name, context)