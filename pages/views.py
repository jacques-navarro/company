from django.shortcuts import render

def home_page_view(request):
  context = {
    "inventory_list": ["widget 1", "widget 2", "widget 3"],
    "greeting": "ThAnk YoU fOr ViSiTinG.",
  }
  return render(request, "home.html", context)


