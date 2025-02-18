# Generated by Django 4.2.11 on 2024-03-21 10:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_is_employee_customuser_is_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_parent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_hash',
            field=models.CharField(default=uuid.UUID('430545d0-c732-4a2b-a8d9-047f1518c9d1'), max_length=30, unique=True),
        ),
    ]
