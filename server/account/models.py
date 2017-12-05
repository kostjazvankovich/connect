# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.db import models
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email, first name, last name,
        and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email, first name, last
        name, and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        # __unicode__ on Python 2
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # TODO: Set minimum value of 1 and maximum value of 5
    risk_score = models.IntegerField(default=0)

@receiver(models.signals.post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(models.signals.post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(models.signals.post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Create an authentication token for new users
    """
    if created:
        Token.objects.create(user=instance)

class Coin(models.Model):
    """
    All coins supported on Polyledger.
    """
    symbol = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True)
    portfolio = models.ManyToManyField('Portfolio', blank=True, through='Position', related_name='coins')

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    """
    A user's portfolio containing coins.
    """
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='portfolios')
    usd = models.FloatField(default=0)

    def __str__(self):
        return '{0}\'s portfolio'.format(self.user)

class Position(models.Model):
    """
    A position of a coin in a portfolio.
    """
    coin = models.ForeignKey('Coin')
    portfolio = models.ForeignKey('Portfolio', related_name='positions', null=True)
    amount = models.FloatField(default=0.0)

class Transaction(models.Model):
    """
    A crypto-crypto transaction in the portfolio
    """
    date = models.DateTimeField(auto_now_add=True)
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name='transactions')
    base = models.ForeignKey('Coin', related_name='base_transactions')
    quote = models.ForeignKey('Coin', related_name='quote_transactions')
