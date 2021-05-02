from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.login_user,name='login_user'),
    path('register/',views.register_page,name='register_page'),
    path('save_details/',views.save_details,name='save_details'),
    path('login_success_or_not/',views.login_success_or_not,name='login_success_or_not'),
    path('show/',views.items,name='items'),
    path("<int:receipe_id>/",views.detail,name='detail'),
    path('create_receipe/',views.create_page,name='create_page'),
    path('save_receipe/',views.save_receipe,name='save_receipe'),
    path('delete_receipe/<int:receipe_id>/',views.delete_receipe,name='delete_receipe'),
    path('logout_page/',views.logout_page,name='logout_page'),
]

