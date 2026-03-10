from crispy_forms.helper import FormHelper
from allauth.account.forms import (
    LoginForm,
    SignupForm,
    ChangePasswordForm,
    ResetPasswordForm,
    ResetPasswordKeyForm,
    SetPasswordForm,
)

from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields["login"].widget = forms.TextInput(
            attrs={
                "class": "form-control mb-2",
                "placeholder": "Enter Username or Email",
                "id": "username",
            }
        )
        self.fields["password"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control mb-2",
                "placeholder": "Enter Password",
                "id": "password",
            }
        )
        self.fields["remember"].widget = forms.CheckboxInput(
            attrs={"class": "form-check-input"}
        )


class UserRegistrationForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields["email"].widget = forms.EmailInput(
            attrs={
                "class": "form-control mb-1",
                "placeholder": "Enter Email",
                "id": "email",
            }
        )
        self.fields["email"].label = "Email"
        self.fields["username"].widget = forms.TextInput(
            attrs={
                "class": "form-control mb-1",
                "placeholder": "Enter Username",
                "id": "username1",
            }
        )
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control mb-1",
                "placeholder": "Enter Password",
                "id": "password1",
            }
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control mb-1",
                "placeholder": "Enter Confirm Password",
                "id": "password2",
            }
        )
        self.fields["password2"].label = "Confirm Password"


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")


class PasswordChangeForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields["oldpassword"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control mb-2",
                "placeholder": "Enter currunt password",
                "id": "password3",
            }
        )
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control mb-2",
                "placeholder": "Enter new password",
                "id": "password4",
            }
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control mb-2",
                "placeholder": "Enter confirm password",
                "id": "password5",
            }
        )
        self.fields["password2"].label = "Confirm Password"


class PasswordResetForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields["email"].widget = forms.EmailInput(
            attrs={
                "class": "form-control mb-2",
                "placeholder": " Enter Email",
                "id": "email1",
            }
        )
        self.fields["email"].label = "Email"


class PasswordResetKeyForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetKeyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control mb-2",
                "placeholder": "Enter new password",
                "id": "password6",
            }
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control mb-1",
                "placeholder": "Enter confirm password",
                "id": "password7",
            }
        )
        self.fields["password2"].label = "Confirm Password"


class PasswordSetForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(PasswordSetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control mb-2",
                "placeholder": "Enter new password",
                "id": "password8",
            }
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter confirm password",
                "id": "password9",
            }
        )
        self.fields["password2"].label = "Confirm Password"
