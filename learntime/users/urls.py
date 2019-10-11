from django.urls import path

from learntime.users.views import (
    login_view, logout_view, register_view, AdminList)

app_name = "users"
urlpatterns = [
    path("login/", view=login_view, name='login'),
    path('logout/', view=logout_view, name='logout'),
    path('register/', view=register_view, name='register'),

    path('admins/', view=AdminList.as_view(), name='admins'),

]
