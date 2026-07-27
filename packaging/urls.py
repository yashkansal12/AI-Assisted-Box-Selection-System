from django.urls import path
from .views import *

urlpatterns = [

    path("products/", ProductListCreateView.as_view()),
    path("boxes/", BoxListCreateView.as_view()),
    path("orders/", OrderCreateView.as_view()),
    path("orders/<int:pk>/recommend/",RecommendBoxView.as_view()),
]