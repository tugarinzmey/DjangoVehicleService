# Generated by Django 3.0.5 on 2022-12-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0011_delete_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('Обрабатывается', 'Обрабатывается'), ('Подтверждена', 'Подтверждена'), ('В ремонте', 'В ремонте'), ('Ремонт завершен', 'Ремонт завершен'), ('Готово!', 'Готово!')], default='Обрабатывается', max_length=50, null=True),
        ),
    ]