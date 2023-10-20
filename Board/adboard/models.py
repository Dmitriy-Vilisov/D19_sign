from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


tank = 'Танк'
healer = 'Хил'
damager = 'ДД'
guild_master = 'Гилдмастер'
quest_giver = 'Квестгивер'
smith = 'Кузнец'
tanner = 'Кожевник'
potion_maker = 'Зельевар'
spell_master = 'Мастер заклинаний'

CATEGORIES = [
    (tank, 'Танк'),
    (healer, 'Хил'),
    (damager, 'ДД'),
    (guild_master, 'Гилдмастер'),
    (quest_giver, 'Квестгивер'),
    (smith, 'Кузнец'),
    (tanner, 'Кожевник'),
    (potion_maker, 'Зельевар'),
    (spell_master, 'Мастер заклинаний'),
]


class Categories(models.Model):
    name = models.CharField(max_length=17, choices=CATEGORIES, default=tank)
    subscribers = models.ManyToManyField(User, blank=True, related_name='categories')

    def __str__(self):
        return self.name.title()

    # def __str__(self):
    #    return f'{self.name}'!!!!!!

    # def get_absolute_url(self):
    #    return reverse('post_category', args=[str(self.pk)])


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="Название")
    text = RichTextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #    return self.title
    # def __str__(self):
    #    return f'объявлению: "{self.title}" в категории "{self.category}" от {self.author}'
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Reply(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)



