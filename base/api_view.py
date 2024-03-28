# views.py
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET'])
def get_students(request):
    students = Student.objects.all().order_by('-id')
    serializer = StudentSerializer(students, many=True)
    return JsonResponse(serializer.data, safe=False)
