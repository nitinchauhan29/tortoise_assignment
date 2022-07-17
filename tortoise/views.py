from os import stat
from urllib import response
from webbrowser import get
from django.shortcuts import render
from requests import request
from rest_framework.decorators import APIView
from rest_framework import status, generics
from .serializers import *
from .models import * 
from rest_framework.response import Response

# Create your views here.

class GetCreatePlan(APIView):

    def get(self, request):

        get_plan = Plans.objects.all()
        serializers = PlanSe(get_plan, many = True)
        print(get_plan)
        return Response(serializers.data)


    def post(self, request):

        plan = PlanSe(data = request.data)
        if plan.is_valid():
            planName = plan["planName"].value
            amountOptions = plan["amountOptions"].value
            tenureOptions = plan["tenureOptions"].value
            benefitPercentage = plan["benefitPercentage"].value
            benefitType = plan["benefitType"].value

            create_plan = Plans.objects.create(planName = planName, amountOptions = amountOptions,
            tenureOptions=tenureOptions,benefitPercentage = benefitPercentage, benefitType=benefitType)

            create_plan.save()

            return Response({"Message":"Plan succesfully cretaed"},status=status.HTTP_200_OK)


class GetCreatePromotion(APIView):

    def get(self, request):

        get_promotions = Promotions.objects.all()
        print(get_promotions)
        serializers = PromotionsSe(get_promotions, many = True)
        return Response(serializers.data)


    def post(self, request):
        
        promotion = PromotionsSe(data = request.data)
        if promotion.is_valid():
            promotionType = promotion["promotionType"].value
            promotionData = promotion["promotionData"].value
            planId = promotion["planId"].value
            find_plan = Plans.objects.get(planId = planId)

            create_promotion = Promotions.objects.create(promotionType = promotionType, promotionData = promotionData, planId= find_plan)
            create_promotion.save()

            return Response({"Message": "Promotion on plan is successfully applied"},status=status.HTTP_200_OK)


class GetEnrollPlan(APIView):

    def get(self, request):

        get_enrolls = CustomerGoals.objects.all()
        serializers = CustomerGoalsSe(get_enrolls, many = True)
        return Response(serializers.data)

    def post(self, request):

        enroll = CustomerGoalsSe(data = request.data)
        if enroll.is_valid():
            userId = enroll["userId"].value
            planId = enroll["planId"].value
            selectedAmount = enroll["selectedAmount"].value
            selectedTenure = enroll["selectedTenure"].value
            depositedAmount = enroll["selectedAmount"].value
            
            get_plan = Plans.objects.get(planId = planId)

            enroll_user = CustomerGoals.objects.create(userId = userId, planId= get_plan, selectedAmount = selectedAmount, selectedTenure= selectedTenure, depositedAmount = depositedAmount)
            enroll_user.save()

            return Response({"Message":"User enroll successfully to the plan"},status = status.HTTP_200_OK)