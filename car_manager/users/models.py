from django.db import models
from django.contrib.auth.models import User

from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(
        default="profile_pics/default.jpg", upload_to="profile_pics"
    )

    def __str__(self):
        return f"Profile of {self.user.username}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        pic = Image.open(self.picture.path)

        if pic.height > 300 or pic.width > 300:
            output_size = (300, 300)
            pic.thumbnail(output_size)
            pic.save(self.picture.path)
