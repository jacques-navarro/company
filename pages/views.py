from django.shortcuts import render

from django.views.generic import TemplateView

def home_page_view(request):
  context = {
    "inventory_list": ["widget 1", "widget 2", "widget 3"],
    "greeting": "ThAnk YoU fOr ViSiTinG.",
  }
  return render(request, "home.html", context)

class AboutPageView(TemplateView):
  template_name = "about.html"
