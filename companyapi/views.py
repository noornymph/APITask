# pylint: disable=all
"""
This module contains views of our application.
"""

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from companyapi.models import Company, Employee
from companyapi.serializers import CompanySerializer, EmployeeSerializer


# Views for handling company and employee API endpoints
class CompanyViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Company model.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # companies/{companyId}/employees
    @action(detail=True, methods=["get"])
    def employees(self, request, pk=None):
        """
        Retrieve the list of employees for a specific company.
        """
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company_name=company)
            emps_serializer = EmployeeSerializer(
                emps, many=True, context={"request": request}
            )
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({"message": "Company might not exist! Error"})


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Employee model.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
