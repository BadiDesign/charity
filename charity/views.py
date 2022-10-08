from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from badi_utils.utils import LoginRequiredMixin


class IndexView(TemplateView):
    extra_context = {
        'title': 'صفحه اصلی'
    }

    def get(self, request, *args, **kwargs):
        return redirect('dashboard')


class DashboardView(LoginRequiredMixin, TemplateView):
    extra_context = {
        'title': 'Dashboard',
    }

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser and not request.user.is_admin:
            request.user.is_admin = True
            request.user.save()
        if not request.user.is_admin:
            return redirect('/')
        return super().get(request, *args, **kwargs)

    def get_template_names(self):
        return 'dashboard.html'


class NotFound404(TemplateView):
    template_name = '404.html'


def my_custom_page_not_found_view(request, *args, **argv):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response
