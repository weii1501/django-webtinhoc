from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_list_category_api_view, name='category-list'),
    # path('<slug:category_slug>/', views.category_detail, name='cate-detail'),
    path('detail/', views.category_detail, name='category-detail'),
    # get all categories
    path('list/', views.list_category_topic, name='category-list-api'),
    # Other user-related URLs for the app
]
