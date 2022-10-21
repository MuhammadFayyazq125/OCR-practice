from django.urls import path
from .views import index, output
urlpatterns = [
    path("", index, name="PDF to image and text"),
    path("Output_pdf/", output, name="PDF"),
]