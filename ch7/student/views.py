from student.models import Student
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def all_data(req):
    students = list(Student.objects.all().values())
    stu = Student.objects.get(pk=1)
    print(stu.name)
    print(list(Student.objects.all().values()))
    # print(students)
    return JsonResponse(students,safe=False)