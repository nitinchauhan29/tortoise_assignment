from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Plans)
class PlanModelAdmin(admin.ModelAdmin):
    list_display = ['planId', 'planName', 'amountOptions','tenureOptions', 'benefitPercentage','benefitType']

@admin.register(Promotions)
class PlanModelAdmin(admin.ModelAdmin):
    list_display = ['promotionId', 'promotionType', 'promotionData','planId']


@admin.register(CustomerGoals)
class CustomersModelAdmin(admin.ModelAdmin):
    list_display = ['goalId', 'userId', 'planId','selectedAmount', 'selectedTenure','startDate','depositedAmount']