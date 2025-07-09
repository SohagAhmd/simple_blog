from django.http import HttpResponse

# Create your views here.
def students(request):
    students = [
        {"name": "Alice", "age": 20},
        {"name": "Bob", "age": 22},
        {"name": "Charlie", "age": 23},
        {"name": "David", "age": 21},
        {"name": "Eve", "age": 19}
    ]
    return HttpResponse(students)