# Generated by Django 4.2.1 on 2023-06-07 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_completed_task_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]