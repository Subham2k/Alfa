from django.urls import path, include
from .import views

urlpatterns = [

    path('', views.home),
    path('tenants/<int:id>/<str:slug>/', views.Detail.as_view(), name='detail'),
    path('tenant_new/', views.Create.as_view(), name='createone'),
    path('tenants/<int:id>/<str:slug>/edit/', views.UpdateTenant.as_view(), name='update'),
    path('tenants/<int:id>/<str:slug>/delete/', views.Delete.as_view(), name='delete'),
]