"""SOS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    user_view,                  # User Panel
    submitted_view,              # End of submission message.
    test,
    register_view,
    login_view,
    logout_view,
    panel_view,
    reg_done
    )
from rescuemap.views import (
    map_select,                 # User rescue plea submission.
    map_select_2,
    map_view                    # Admin user distribution viewer

    )

urlpatterns = [
    path('map_me/', map_select),
    path('map_other/', map_select_2),
    path('rescue/', map_view),
    path('admin/', admin.site.urls),
    path('', user_view),
    path('done/', submitted_view),
    path('test/', test),
    path('register/', register_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('panel/', panel_view),
    path('reg_done/', reg_done),
]
