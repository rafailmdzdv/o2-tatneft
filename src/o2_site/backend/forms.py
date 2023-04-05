from django import forms

from backend import error_messages, models


class RegistrationForm(forms.Form):

    username = forms.CharField(max_length=40,
                               error_messages=error_messages.USERNAME_MESSAGES)
    email = forms.EmailField(error_messages=error_messages.EMAIL_MESSAGES)
    password = forms.CharField(error_messages=error_messages.PASSWORD_MESSAGES)

    def save(self):
        user = models.User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        return user


class UpdateCredentialsForm(forms.ModelForm):

    username = forms.CharField(max_length=40, required=False,
                               error_messages=error_messages.USERNAME_MESSAGES)
    email = forms.EmailField(required=False,
                             error_messages=error_messages.EMAIL_MESSAGES)

    class Meta:
        model = models.User
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data['email']
        if email and models.User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                error_messages.EMAIL_MESSAGES['unique'],
                code='unique'
            )
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if username and models.User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                error_messages.USERNAME_MESSAGES['unique'],
                code='unique'
            )
        return username

    def clean(self):
        cleaned_data = super().clean()
        if not any(cleaned_data.values()):
            raise forms.ValidationError('Данное поле необходимо')
        else:
            filtered_by_empty = filter(
                lambda field: self.cleaned_data[field] == '',
                cleaned_data.keys()
            )
            empty_field = list(filtered_by_empty)[0]
            del cleaned_data[empty_field]
        return cleaned_data


class PasswordChangeForm(forms.Form):

    password = forms.CharField(error_messages=error_messages.PASSWORD_MESSAGES)

    def __init__(self, user: models.User, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        password = self.cleaned_data['password']
        if commit:
            self.user.set_password(password)
            self.user.save()
        return self.user
