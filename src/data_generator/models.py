from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

class Schema(models.Model):
    """ Model Schema """

    class Status(models.TextChoices):
        """ status enum type"""
        New = 'N'
        Processing = 'P'
        Ready = 'R'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    column_separator = models.CharField(max_length=1)
    character_string = models.CharField(max_length=1)
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.New)
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
            return self.name

    class Meta:
        db_table = 'schemas'
        verbose_name = "Schema"
        verbose_name_plural = "Schemas"


class Type(models.Model):
    """ Model Type """

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'types'
        verbose_name = "Type"
        verbose_name_plural = "Types"


class Column(models.Model):
    """ A Column for Schema """

    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    range = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'columns'
        verbose_name = "Column"
        verbose_name_plural = "Columns"


class FakeData(models.Model):
    """ Model FakeData for Schema """

    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    data = models.CharField(max_length=200)

    class Meta:
        db_table = 'fake_datas'
        verbose_name = "Fake Data"
        verbose_name_plural = "Fake Datas"