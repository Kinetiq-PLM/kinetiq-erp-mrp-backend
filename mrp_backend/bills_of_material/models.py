from django.db import models
import datetime
from django.utils.translation import gettext as _

class BOM(models.Model):
    order_no = models.CharField(max_length=100)

    type = models.CharField(max_length=15, default="Project")

    details = models.TextField(blank=True, null=True)

    date = models.DateField(_("Date"), default=datetime.date.today)

    def __str__(self):
        return self.order_no

    def saveOrder(self):
        self.save()