"""View module for handling requests about employees"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from workforceapi.models import Employee, Department

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for employees
    Arguments:
        serializers
    """

    class Meta:
        model = Employee
        url = serializers.HyperlinkedIdentityField(
            view_name='employee',
            lookup_field='id'
        )
        # fields = (fill in with the appropriate columns)


class Employees(ViewSet):
    """Employees of Bangazon"""

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized Employee instance
        """
        pass

    def retrieve(self, request, pk=None):
        """Handle GET requests for single employee
        Returns:
            Response -- JSON serialized employee instance
        """
        pass

    def update(self, request, pk=None):
        """Handle PUT requests for an Employee
        Returns:
            Response -- Empty body with 204 status code
        """
        pass

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single employee
        Returns:
            Response -- 200, 404, or 500 status code
        """
        pass

    def list(self, request):
        """Handle GET requests to employee resource
        Returns:
            Response -- JSON serialized list of employees
        """
        pass
