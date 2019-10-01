"""View module for handling requests about departments"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from workforceapi.models import Department

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for departments
    Arguments:
        serializers
    """

    class Meta:
        model = Department
        url = serializers.HyperlinkedIdentityField(
            view_name='department',
            lookup_field='id'
        )
        # fields = ()


class Departments(ViewSet):
    """Departments in Bangazon"""

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized Department instance
        """
        pass

    def retrieve(self, request, pk=None):
        """Handle GET requests for single department
        Returns:
            Response -- JSON serialized department instance
        """
        pass

    def update(self, request, pk=None):
        """Handle PUT requests for a department
        Returns:
            Response -- Empty body with 204 status code
        """
        pass

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single department
        Returns:
            Response -- 200, 404, or 500 status code
        """
        pass

    def list(self, request):
        """Handle GET requests to department resource
        Returns:
            Response -- JSON serialized list of departments
        """
        pass
