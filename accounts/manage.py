from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations: True

    def create_user(self, email,password=None **extra_fields):
        if not email:
            raise ValueError('Email Required')
        email=self.normalize_email(email)
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # def create_superuser(self, email,password=None **extra_fields):
