# Generated by Django 4.2.1 on 2023-06-23 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("std_stn", models.IntegerField(verbose_name="学号")),
                ("std_name", models.CharField(max_length=32, verbose_name="学生姓名")),
                (
                    "std_sex",
                    models.SmallIntegerField(
                        choices=[(1, "男"), (2, "女")], verbose_name="学生性别"
                    ),
                ),
                ("std_academy", models.CharField(max_length=32, verbose_name="学院")),
                ("std_level", models.CharField(max_length=32, verbose_name="年级")),
                ("std_class", models.CharField(max_length=32, verbose_name="班级")),
            ],
        ),
    ]
