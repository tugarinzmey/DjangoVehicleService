# Generated by Django 3.0.5 on 2022-12-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0009_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='mechanic',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='request',
            name='category',
        ),
        migrations.RemoveField(
            model_name='request',
            name='vehicle_brand',
        ),
        migrations.RemoveField(
            model_name='request',
            name='vehicle_model',
        ),
        migrations.AlterField(
            model_name='request',
            name='problem_description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('Обрабатывается', 'Обрабатывается'), ('Подтверждена', 'Подтверждена'), ('В ремонте', 'В ремонте'), ('Ремонт завершен', 'Ремонт завершен'), ('Готов!', 'Готово!')], default='Обрабатывается', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='vehicle_no',
            field=models.CharField(max_length=6),
        ),
    ]
