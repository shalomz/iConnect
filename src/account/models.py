from django.db import models
from django.conf import settings
import datetime
from django.core.cache import cache


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    joined = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def last_seen(self):
        return cache.get('seen_%s' % self.user.username)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > self.last_seen() + datetime.timedelta(
                         seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
