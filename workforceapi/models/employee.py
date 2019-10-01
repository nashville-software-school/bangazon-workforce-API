"""Module for for Employees"""
from django.db import models


class Employee(models.Model):
    """Model class for Employee"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey("Department", on_delete=models.DO_NOTHING, related_name="employees")

    class Meta:
        verbose_name = ("employee")
        verbose_name_plural = ("employees")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
