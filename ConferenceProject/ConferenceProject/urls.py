"""ConferenceProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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


from ConfRooms import views as confrooms


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', confrooms.HomeView.as_view()),
    path('room/new/', confrooms.AddRoom.as_view()),
    path('room/list/', confrooms.ShowRooms.as_view()),
    path('room/delete/<int:room_pk>/', confrooms.DeleteRoom.as_view()),
    path('room/modify/<int:room_pk>/', confrooms.EditRoom.as_view()),
    path('room/reserve/<int:room_pk>/', confrooms.ReserveRoom.as_view()),
    path('room/details/<int:room_pk>/', confrooms.DetailsRoom.as_view()),
]
