from django.shortcuts import render,HttpResponse,redirect
from django import forms
from django.forms import ModelForm
from my_app import models
from my_app.models import Student
from my_app.models import Score

# Create your views here.
class StuForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = "__all__"

def stu_add(request):
    if request.method=="GET":
            form=StuForm()
            return render(request, "stu_add.html" , {"form": form})
        
    form=StuForm(data=request.POST)
    if form.is_valid():
        form.save()
        #print("提交成功")
        return render(request, "stu_add.html" , {"form": form})
    else:
        print(form.errors)
        
def list_stu(request):

    queryset=models.Student.objects.all()
    return render(request,'list_.html',{"queryset": queryset})


class ScoreForm(forms.ModelForm):
    class Meta:
        model = models.Score
        fields = "__all__"
        
def add_score(request):
    if request.method=="GET":
            form=ScoreForm()
            return render(request, "add_score.html" , {"form": form})
        
    form=ScoreForm(data=request.POST)
    if form.is_valid():
        form.save()
        #print("提交成功")
        return render(request, "add_score" , {"form": form})
    else:
        print(form.errors)

class TeaForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = "__all__" 

def add_tea(request):
    if request.method=="GET":
            form=TeaForm()
            return render(request, "add_tea.html" , {"form": form})
        
    form=TeaForm(data=request.POST)
    if form.is_valid():
        form.save()
        #print("提交成功")
        return render(request, "add_tea.html" , {"form": form})
    else:
        print(form.errors)

class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = "__all__" 
        
def add_cour(request):
    if request.method=="GET":
            form=CourseForm()
            return render(request, "add_course.html" , {"form": form})
        
    form=CourseForm(data=request.POST)
    if form.is_valid():
        form.save()
        #print("提交成功")
        return render(request, "add_course.html" , {"form": form})
    else:
        print(form.errors)
        
def look_score(request):
    if request.method=="GET":
        sf=models.Student.objects.all()
        scf=models.Score.objects.all()
        return render(request, "look_score.html" , {"sf": sf, "scf" : scf})

def search(request):
    data_dict={}
    value=request.GET.get('q')
    if value:
        data_dict['course__contains']=value
    queryset=models.Course.objects.filter(**data_dict)

    return render(request,'search.html',{"queryset":queryset})

def login(request):
    return render(request,'login_.html')