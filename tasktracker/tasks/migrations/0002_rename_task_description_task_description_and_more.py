# Generated by Django 5.1.3 on 2025-01-21 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='task',
            name='is_completed',
        ),
        migrations.RemoveField(
            model_name='task',
            name='reminder_type',
        ),
    ]
