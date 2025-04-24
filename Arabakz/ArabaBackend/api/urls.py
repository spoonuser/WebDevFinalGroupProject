from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
   path('api/cars/', views.car_list),
   path('api/cars/<int:car_id>/', views.car_detail),
   path('api/categories/', views.CategoryListAPIView.as_view()),
   path('api/categories/<int:category_id>/', views.CategoryDetailAPIView.as_view()),
   path('api/categories/<int:category_id>/cars/', views.CategoryCarListAPIView.as_view()),
   path('api/login/', TokenObtainPairView.as_view()),
   path('api/registration/', views.registration),
   path('api/user/', views.get_user),
   path('api/likes/', views.LikeAPIView.as_view()),
   path('api/likes/<int:like_id>/', views.LikeDetailAPIView.as_view()),
   path('api/accessories/', views.accessory_list),
   path('api/charging/', views.charging_station_list),
   path('api/articles/', views.article_list),
   path('api/articles/<int:pk>/', views.article_detail)
]
