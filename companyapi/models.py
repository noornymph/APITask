"""
This module contains the models of our application.
"""

from django.db import models


class Company(models.Model):
    """
    Django model representing company.
    """

    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    type = models.CharField(
        max_length=50,
        choices=(
            ("IT", "IT"),
            ("Distributor", "Distributor"),
            ("Manufacturer", "Manufacturer"),
        ),
        default="IT",
    )


class Employee(models.Model):
    """
    Django model representing employee.
    """

    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=50)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(
        max_length=20,
        choices=(
            ("Worker", "Worker"),
            ("Manager", "Manager"),
            ("Supervisor", "Supervisor"),
        ),
        default="Manager",
    )
