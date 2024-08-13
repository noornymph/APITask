# Generated by Django 5.0.7 on 2024-08-02 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyapi', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='type',
            field=models.CharField(choices=[('IT', 'IT'), ('Distributor', 'Distributor'), ('Manufacturer', 'Manufacturer')], default='IT', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('Worker', 'Worker'), ('Manager', 'Manager'), ('Supervisor', 'Supervisor')], default='Manager', max_length=20),
        ),
    ]
