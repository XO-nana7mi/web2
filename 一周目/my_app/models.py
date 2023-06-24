from django.db import models

# Create your models here.
class Student(models.Model):
    '学生表'
    std_stn=models.IntegerField(verbose_name="学号")
    def __str__(self):
        return str(self.std_stn)
    std_name=models.CharField(verbose_name="学生姓名",max_length=32)
    std_choice=(
        (1, "男"),
        (2, "女"),
    )
    std_sex=models.SmallIntegerField(verbose_name="学生性别",choices=std_choice)
    std_academy=models.CharField(verbose_name="学院",max_length=32)
    std_level=models.CharField(verbose_name="年级",max_length=32)
    std_class=models.CharField(verbose_name="班级",max_length=32)
    
class Teacher(models.Model):
    "教师表"
    tea_name=models.CharField(verbose_name="教师姓名",max_length=32)
    def __str__(self):
        return self.tea_name
    tea_choice=(
        (1, "男"),
        (2, "女"),
    )
    tea_sex=models.SmallIntegerField(verbose_name="教师性别",choices=tea_choice)
    tea_num=models.IntegerField(verbose_name="教师电话")
    
class Course(models.Model):

    cour_name=models.CharField(verbose_name="课程名",max_length=32)
    def __str__(self):
        return str(self.cour_name)
    cour_semester=models.IntegerField(verbose_name="学期")
    cour_credit=models.IntegerField(verbose_name="学时")
    cour_chour=models.IntegerField(verbose_name="学分")
    tea_name=models.ForeignKey('Teacher',on_delete=models.CASCADE,verbose_name="教师姓名")

    
class Score(models.Model):
    std_stu = models.ForeignKey('Student',on_delete=models.CASCADE,verbose_name="学号")
    cour_name=models.ForeignKey('Course',on_delete=models.CASCADE,verbose_name="课程名")
    scores=models.IntegerField(verbose_name="分数")