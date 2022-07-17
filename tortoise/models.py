from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Plans(models.Model):
    planId = models.AutoField(primary_key=True)
    planName = models.CharField(max_length=64, default="")
    amountOptions = models.CharField(max_length=64)
    tenureOptions = models.IntegerField()
    benefitPercentage = models.FloatField()
    benefitType = models.CharField(max_length=64,default="")

    def __str__(self):
        return str(self.planId)

class Promotions(models.Model):
    promotionId = models.AutoField(primary_key=True)
    promotionType = models.CharField(max_length=64,default="")
    promotionData = models.CharField(max_length=64,default="")
    planId = models.OneToOneField(Plans, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.promotionId)

class CustomerGoals(models.Model):
    goalId = models.AutoField(primary_key=True, unique= True)
    userId = models.IntegerField()
    planId = models.ForeignKey(Plans, on_delete=models.CASCADE)
    selectedAmount = models.IntegerField()
    selectedTenure = models.IntegerField()
    startDate = models.DateTimeField(auto_now_add=True)
    depositedAmount = models.IntegerField()

    def __str__(self):
        return str(self.goalId)




