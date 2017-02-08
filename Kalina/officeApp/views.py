# from django.shortcuts import render
from .models import OfficeItem
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView


# class OfficeView(DetailView):
#     # Return detail data
#     model = OfficeItem
#     context_object_name = 'office'
#     template_name = 'office_item.html'
#
# #    def get_context_data(self, **kwargs):
# #        context = super(PostDetail, self).get_context_data(**kwargs)
# #        context['comments'] = Comment.objects.filter(post=self.object, is_delete=False).order_by('-created_at')
# #        return context
#
#
# class OfficeList(ListView):
#     model = OfficeItem
#     context_object_name = 'offices'
#     template_name = 'svg_five.html'
#     success_url = '/offices/'
