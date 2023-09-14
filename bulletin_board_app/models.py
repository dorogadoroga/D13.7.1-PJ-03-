from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    tanks = 'TA'
    healers = 'HI'
    damage_dealers = 'DD'
    traders = 'TR'
    guild_master = 'GM'
    quest_givers = 'QG'
    blacksmiths = 'BS'
    leather_workers = 'LW'
    potion_makers = 'PM'
    spell_masters = 'SM'

    CATEGORIES = [
        (tanks, 'Tanks'),
        (healers, 'Healers'),
        (damage_dealers, 'Damage Dealers'),
        (traders, 'Traders'),
        (guild_master, 'Guild Master'),
        (quest_givers, 'Quest Givers'),
        (blacksmiths, 'Blacksmiths'),
        (leather_workers, 'Leatherworkers'),
        (potion_makers, 'Potion Makers'),
        (spell_masters, 'Spell Masters')
    ]

    # name = models.CharField(max_length=2, choices=CATEGORIES, verbose_name='Категория')
    slug = models.SlugField(max_length=2, choices=CATEGORIES, verbose_name='Category')

    def __str__(self):
        return self.get_slug_display()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255, verbose_name='Title')
    text = models.TextField(verbose_name='Text')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Image')
    media_content = models.FileField(upload_to='other_media/', null=True, blank=True, verbose_name='Media')

    def get_absolute_url(self):
        return f'/{self.id}'

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    text = models.TextField(verbose_name='Text')
    is_accepted = models.BooleanField(default=False)
