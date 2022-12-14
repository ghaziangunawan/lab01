from django.urls import path
from wishlist.views import show_wishlist, show_wishlistajax
from wishlist.views import show_xml
from wishlist.views import show_json_by_id
from wishlist.views import register
from wishlist.views import login_user
from wishlist.views import logout_user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('wishlist_ajax', show_wishlistajax, name='show_wishlistajax'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_xml, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
]
