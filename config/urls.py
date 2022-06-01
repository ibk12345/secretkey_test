from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('apps.product.urls')),
    path('account/', include('apps.account.urls')),
    path('category/', include('apps.category.urls')),
    # path('order/', include('apps.order.urls')),

]
