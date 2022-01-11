from django.urls import path
from .views import PigLatinApiView

app_name = 'translator'

urlpatterns = [
    path('pig_latin', PigLatinApiView.as_view(), name="pig_latin")
]
