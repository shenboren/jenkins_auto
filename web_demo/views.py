from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


index_view = IndexView.as_view()
