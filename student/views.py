from django.shortcuts import render
from student.models import Student
from student.form.StudentForm import StudentForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {'student_list': students}
    return render(request, 'student_list.html', context)


def student_detail(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        return render(request, 'not_found.html')

    context = {'student': student}
    return render(request, 'student_detail.html', context)


def edit_student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        return render(request, 'not_found.html')

    if request.method == 'GET':
        form = StudentForm(
            initial={'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age})

    elif request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            student.first_name = form.cleaned_data['first_name']
            student.last_name = form.cleaned_data['last_name']
            student.age = form.cleaned_data['age']

            student.save()

            return HttpResponseRedirect('/student/')

    context = {'student': student, 'form': form}

    return render(request, 'edit_student.html', context)


def delete_student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        return render(request, 'not_found.html')

    student.delete()

    return HttpResponseRedirect('/student/')


def add_student(request):
    if request.method == 'GET':
        form = StudentForm()

    elif request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']

            new_student = Student(first_name=first_name, last_name=last_name, age = age)
            new_student.save()

            return HttpResponseRedirect('/student/')

    context = {'form': form}

    return render(request, 'add_student.html', context)
