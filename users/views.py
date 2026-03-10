from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView


from .forms import UserUpdateForm


User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/employee/employee_detail_view.html"

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context["heading"] = "Profile"
        context["pageview"] = "Dashboard"
        return context


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = "users/user_update_view.html"
    form_class = UserUpdateForm
    success_message = "Your profile is updated successfully"
    success_url = reverse_lazy("users:user_update_view")

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context["heading"] = "Update Profile"
        context["pageview"] = "Dashboard"
        return context


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("dashboard")

    def get_context_data(self, **kwargs):
        context = super(UserRedirectView, self).get_context_data(**kwargs)
        context["heading"] = "Redirect"
        context["pageview"] = "Dashboard"
        return context
