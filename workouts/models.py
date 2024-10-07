from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    is_premium = models.BooleanField(default=False)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    fat_percentage = models.FloatField(null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='workout_users',  # Изменено, чтобы избежать конфликта с auth.User
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='workout_users_permissions',  # Изменено, чтобы избежать конфликта с auth.User
        blank=True
    )

class Admin(User):
    pass

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length=100)
    exercises = models.ManyToManyField(Exercise)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class WorkoutSet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    weights = models.JSONField()
    repetitions = models.JSONField()

    def __str__(self):
        return f'{self.user.username} - {self.workout.name}'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'
