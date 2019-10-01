"""Module for for Departments"""
from django.db import models


class Department(models.Model):
    """Model class for Department"""
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("department")
        verbose_name_plural = ("deparments")

    def __str__(self):
        return self.name
