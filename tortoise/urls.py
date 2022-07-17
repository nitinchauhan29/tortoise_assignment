from unicodedata import name
from django.urls import path, include
from .views import *

urlpatterns = [
    path('getcreateplan/',GetCreatePlan.as_view(),name="getcreateplan"),
    path('getcreatepromotion/',GetCreatePromotion.as_view(),name = "getcreatepromotions" ),
    path('getenrollusers/', GetEnrollPlan.as_view(), name="getenrolluser")
]
