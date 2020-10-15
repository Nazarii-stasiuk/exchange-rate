from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password, identify_hasher
from django.db.models import (EmailField, CharField, BooleanField, DateTimeField)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, name=None, full_name=None,
                    is_active=True, is_staff=None, is_admin=None, is_bitcoin=None,
                     is_ethereum=None, is_litecoin=None, is_ripple=None):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('Пользователь должен иметь и-мэйл адрес')
        if not password:
            raise ValueError('Пользователь должен ввести пароль')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.bitcoin = is_bitcoin
        user.ethereum = is_ethereum
        user.litecoin = is_litecoin
        user.ripple = is_ripple
        user.active = is_active
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, name=None):
        user = self.create_user(email, name=name, password=password,
                    is_staff=True, is_admin=True, is_ripple=True, is_bitcoin=True,
                    is_ethereum=True, is_litecoin=True)
        return user
    
    def create_staffuser(self, email, password=None, name=None):
        user = self.create_user(email, name=name, password=password,
                    is_staff=True, is_admin=False, is_ripple=True, is_bitcoin=True,
                    is_ethereum=True, is_litecoin=True)
        return user


class User(AbstractBaseUser):
    email = EmailField(unique=True, max_length=255)
    name = CharField(max_length=255, blank=True, null=True)
    full_name = CharField(max_length=255, blank=True, null=True)
    staff = BooleanField(default=False)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)
    bitcoin = BooleanField(default=False)
    ethereum = BooleanField(default=False)
    litecoin = BooleanField(default=False)
    ripple = BooleanField(default=False)
    timestamp = DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        if self.name:
            return self.name
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.admin:
            return True 
        return self.staff
    
    @property
    def is_active(self):
        if self.admin:
            return True 
        return self.active

    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_ripple(self):
        if self.admin:
            return True 
        return self.ripple

    @property
    def is_bitcoin(self):
        if self.admin:
            return True
        return self.bitcoin

    @property
    def is_ethereum(self):
        if self.admin:
            return True 
        return self.ethereum

    @property
    def is_litecoin(self):
        if self.admin:
            return True 
        return self.litecoin

    def save(self, *args, **kwargs):
        try:
            _alg = identify_hasher(self.password)
        except ValueError:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)