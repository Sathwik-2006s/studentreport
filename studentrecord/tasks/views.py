from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from rest_framework import viewsets, filters
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'student_class', 'marks']  # Changed grade to marks here
    ordering_fields = ['marks', 'student_class']
    ordering = ['-marks']  # Default: max to min marks

def student_list(request):
    students = Student.objects.all()

    # Filters from GET request
    name = request.GET.get('filter_name')
    student_class = request.GET.get('filter_class')
    marks = request.GET.get('filter_marks')  # Changed filter_grade to filter_marks

    if name:
        students = students.filter(name__icontains=name)
    if student_class:
        students = students.filter(student_class__icontains=student_class)
    if marks:
        students = students.filter(marks__icontains=marks)  # Changed grade to marks

    return render(request, 'tasks/student_list.html', {'students': students})


def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        student_class = request.POST.get('student_class')
        age = request.POST.get('age')
        roll_num = request.POST.get('roll_num')
        marks = request.POST.get('marks')  # Using marks instead of grade
        Student.objects.create(
            name=name,
            student_class=student_class,
            age=age,
            roll_num=roll_num,
            marks=marks
        )
        return redirect('tasks:student_list')
    return render(request, 'tasks/student_create.html')


def student_update(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.student_class = request.POST.get('student_class')
        student.age = request.POST.get('age')
        student.roll_num = request.POST.get('roll_num')
        student.marks = request.POST.get('marks')  # Using marks instead of grade
        student.save()
        return redirect('tasks:student_list')
    return render(request, 'tasks/student_update.html', {'student': student})


def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('tasks:student_list')
    return render(request, 'tasks/student_delete.html', {'student': student})
