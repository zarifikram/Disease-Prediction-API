from django.db import models

class approvals(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    dependants = models.IntegerField()
    applicantIncome = models.IntegerField()


    def __str__(self):
        return self.firstname
