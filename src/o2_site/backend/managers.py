from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, username: str, email: str, password: str):
        if not username:
            raise ValueError(_('Логин обязателен'))
        if not email:
            raise ValueError(_('Почта обязательна'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
