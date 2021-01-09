from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

# Models
# ==============================
# Profile
# Item
# Place
# Session
# Storage
# Order
# OrderType

#========================================================================================
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, blank=True)
    second_name = models.CharField(max_length=40, blank=True)
    mobile_phone = models.CharField(max_length=20, blank=True, default='+375()')

    def __str__(self):
        return  self.user.username + " > " + self.first_name + " " + self.second_name

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Сотрудники'        

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

#========================================================================================
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'позиция'
        verbose_name_plural = 'Инвентарь'

#========================================================================================
class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    adres = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'заведение'
        verbose_name_plural = 'Заведения'

#========================================================================================
class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, default='1')
    place = models.ForeignKey('Place', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_created=True, auto_now_add=True)
    end_time = models.DateTimeField(default=now, blank=True)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.session_id.value_to_string()

    class Meta:
        verbose_name = 'смена'
        verbose_name_plural = 'Смены'

#========================================================================================
class Storage(models.Model):
    storage_id = models.AutoField(primary_key=True)
    place = models.ForeignKey('Place', on_delete=models.CASCADE)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.storage_id

    class Meta:
        verbose_name = 'инвентарь' 
        verbose_name_plural = 'Склад'

#========================================================================================
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    order_type = models.ForeignKey('OrderType', on_delete=models.CASCADE)

    def __str__(self):
        return self.order_id

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'

#========================================================================================
class OrderType(models.Model):
    order_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'кальян'
        verbose_name_plural = 'Кальяны'
