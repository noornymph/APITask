"""
This module contains the serializers of the respective models.
"""

from rest_framework import serializers

from companyapi.models import Company, Employee


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer of the Company model.
    """

    class Meta:
        """
        Structure of Company serializer.
        """

        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer of the Employee model.
    """

    class Meta:
        """
        Structure of Employee serializer.
        """

        model = Employee
        fields = "__all__"
