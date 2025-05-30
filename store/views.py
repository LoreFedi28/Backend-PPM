from django.views.generic import ListView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'

class ManagerOnlyView(UserPassesTestMixin, TemplateView):
    template_name = 'store/manager_only.html'

    def test_func(self):
        return self.request.user.groups.filter(name='Manager').exists()
