from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 
from main.views import register, login_user, logout_user
from main.views import edit_itemnya, delete_itemnya
from main.views import get_items_json, add_item_ajax, create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-itemnya/<int:id>', edit_itemnya, name='edit_itemnya'),
    path('delete/<int:id>', delete_itemnya, name='delete_itemnya'),
    path('get-items/', get_items_json, name='get_items_json'),
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]