from django.urls import path
from .views import ProductListView, ManagerOnlyView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('manager/', ManagerOnlyView.as_view(), name='manager-only'),
]
