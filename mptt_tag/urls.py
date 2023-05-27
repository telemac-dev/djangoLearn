from django.urls import path
from mptt_tag.views import tag_list, tag_create, tag_update, tag_delete

urlpatterns = [
    path('', tag_list, name='tag_list'),
    path('create/', tag_create, name='tag_create'),
    path('update/<int:pk>/', tag_update, name='tag_update'),
    path('delete/<int:pk>/', tag_delete, name='tag_delete'),
]
