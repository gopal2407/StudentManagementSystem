from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student


def student_form(request):
    template_name = 'student_app/student_form.html'
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_data_url')
    context = {'form': form}
    return render(request, template_name, context)


def student_data(request):
    template_name = 'student_app/student_data.html'
    records = Student.objects.all()
    print(records)
    context = {'records': records}
    return render(request, template_name, context)


def student_update(request, pk):
    template_name = 'student_app/student_form.html'
    obj = Student.objects.get(pk=pk)
    form = StudentForm(instance=obj)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            redirect('student_data_url')
    context = {'form': form}
    return render(request, template_name, context)


def student_delete(request, pk):
    obj = Student.objects.get(pk=pk)
    obj.delete()