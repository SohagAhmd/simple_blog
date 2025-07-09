from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student

# Create your views here.
def studentsViews (request):
    students = Student.objects.all()
    print(students)
    sutudent_list = list(students.values())
    print(sutudent_list)
    return JsonResponse(sutudent_list, safe=False)