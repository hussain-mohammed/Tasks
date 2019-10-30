from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.profile.as_view()),
    path('register/', views.register.as_view()),
    path('loandetails/', views.Detail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]