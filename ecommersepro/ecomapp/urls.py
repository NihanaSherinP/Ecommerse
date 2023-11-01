from django.urls import path
from  . import views
app_name='ecomapp'
urlpatterns = [

  path('',views.allproductcat,name='allproductcat'),
  path('<slug:c_slug>/',views.allproductcat,name='prod_by_cat'),
  path('<slug:c_slug>/<slug:product_slug>/',views.proDetails,name='detailprod')
]