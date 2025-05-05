from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import ContextMixin

# 1. LoginRequiredMixin 
class LoginRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# 2. StaffRequiredMixin
class StaffRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("Доступ дозволений лише для персоналу.")
        return super().dispatch(request, *args, **kwargs)

# 3. SuccessMessageMixin
class SuccessMessageMixin:
    success_message = ""

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.success_message:
            messages.success(self.request, self.success_message)
        return response

# 4. AuthorRequiredMixin (доступ тільки для автора)
class AuthorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            return HttpResponseForbidden("Ви не автор цього об'єкта.")
        return super().dispatch(request, *args, **kwargs)

# 5. RedirectAuthenticatedUserMixin (редірект авторизованих користувачів)
class RedirectAuthenticatedUserMixin:
    redirect_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)

# 6. FormErrorsToMessagesMixin (відображення помилок через messages)
class FormErrorsToMessagesMixin:
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)

# 7. GroupRequiredMixin
class GroupRequiredMixin:
    group_required = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name=self.group_required).exists():
            return HttpResponseForbidden("Недостатньо прав доступу.")
        return super().dispatch(request, *args, **kwargs)

# 8. AjaxRequiredMixin
class AjaxRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return HttpResponseForbidden("Доступ лише через AJAX.")
        return super().dispatch(request, *args, **kwargs)

# 9. ContextTitleMixin (додає заголовок в контекст)
class ContextTitleMixin(ContextMixin):
    page_title = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context

# 10. ObjectOwnerOrStaffMixin
class ObjectOwnerOrStaffMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user and not request.user.is_staff:
            return HttpResponseForbidden("Доступ заборонено.")
        return super().dispatch(request, *args, **kwargs)