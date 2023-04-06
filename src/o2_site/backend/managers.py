from django.contrib.auth.base_user import BaseUserManager

from backend import models


class UserManager(BaseUserManager):

    def create_user(self, username: str, email: str, password: str):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()
