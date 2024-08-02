"""
This module contains the application configurations of our applications.
"""

from django.apps import AppConfig


class CompanyapiConfig(AppConfig):
    """
    Configurations of company api applicaion.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "companyapi"
