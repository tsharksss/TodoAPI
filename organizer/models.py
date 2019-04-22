from django.db import models


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=120)
    pub_date = models.DateField('Publication date', null=True, blank=True)
    marked = models.BooleanField()

    def __str__(self):
        return self.text + ' - ' + str(self.pub_date)
