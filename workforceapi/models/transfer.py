"""Module for for Transfers"""
from django.db import models


class Transfer(models.Model):
    """Model class for Transfers"""
    employee = models.ForeignKey("Employee", on_delete=models.DO_NOTHING)
    department = models.ForeignKey("Department", on_delete=models.DO_NOTHING, related_name="employees")
    responsible_staff_member = models.ForeignKey("StaffMember", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("transfer")
        verbose_name_plural = ("transfers")
