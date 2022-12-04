# Generated by Django 3.2.15 on 2022-10-24 16:56

import AAS.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='ImagesAttendance')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=191, null=True)),
                ('coursecode', models.TextField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191, null=True)),
                ('Reg', models.TextField(max_length=50, null=True)),
                ('father_name', models.CharField(max_length=191)),
                ('dob', models.TextField(max_length=191)),
                ('gender', models.TextField(max_length=50)),
                ('ph', models.TextField(max_length=50)),
                ('email', models.TextField(max_length=50)),
                ('cnic', models.TextField(max_length=50)),
                ('nationality', models.TextField(max_length=50)),
                ('status', models.TextField(max_length=50)),
                ('bgroup', models.TextField(max_length=50)),
                ('address', models.TextField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to=AAS.models.filepath)),
            ],
        ),
    ]