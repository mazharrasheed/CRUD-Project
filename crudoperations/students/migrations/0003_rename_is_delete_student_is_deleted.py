# Generated by Django 4.2.9 on 2024-02-15 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_is_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='is_delete',
            new_name='is_deleted',
        ),
    ]
