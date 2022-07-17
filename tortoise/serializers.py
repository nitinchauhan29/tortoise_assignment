from rest_framework import serializers

class PlanSe(serializers.Serializer):
    planName = serializers.CharField(max_length=64)
    amountOptions = serializers.CharField(max_length=64)
    tenureOptions = serializers.IntegerField()
    benefitPercentage = serializers.FloatField()
    benefitType = serializers.CharField(max_length=64)
    
class PromotionsSe(serializers.Serializer):
    promotionType = serializers.CharField(max_length=64)
    promotionData = serializers.CharField(max_length=64,)
    planId = serializers.CharField(max_length = 500)

class CustomerGoalsSe(serializers.Serializer):
    userId = serializers.IntegerField()
    planId = serializers.CharField(max_length = 500)
    selectedAmount = serializers.IntegerField()
    selectedTenure = serializers.IntegerField()
    depositedAmount = serializers.IntegerField()