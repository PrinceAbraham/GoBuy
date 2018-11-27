from django.conf.urls import url
from cart import views

app_name = 'cart'

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    # add parameter object or you'll have error for no pattern matched
    # url(r'^add-to-cart/(?P<item_id>[-\w]+)/', views.add_to_cart, name='add_to_cart'),
     url(r'^remove_from_cart/(?P<item_id>[-\w]+)/', views.remove_from_cart, name='remove_from_cart'),
     url(r'^place_order/', views.place_order, name='place_order'),
]
