from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	user_department = models.CharField(max_length=64, blank=True)
	user_avatar = models.ImageField(blank=True)
	user_signature = models.TextField()

	def __str__(self):
		return self.get_username()

class Board(models.Model):
	BoardID = models.AutoField(primary_key=True)
	board_title = models.CharField(max_length=64)

	def __str__(self):
		return self.board_title

class Category(models.Model):
	CategoryID = models.AutoField(primary_key=True)
	category_title = models.CharField(max_length=64)
	Board = models.ForeignKey(Board, on_delete=models.CASCADE)

	def __str__(self):
		return self.category_title

class Post(models.Model):
	PostID = models.AutoField(primary_key=True)
	Category = models.ForeignKey(Category, on_delete=models.CASCADE)
	post_title = models.CharField(max_length=64)
	post_time = models.DateTimeField(auto_now=True)
	User = models.ForeignKey(User, on_delete=models.CASCADE)
	post_text = models.TextField()

	def __str__(self):
		return self.post_title

class Comment(models.Model):
	CommentID = models.AutoField(primary_key=True)
	Post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment_time = models.DateTimeField(auto_now=True)
	User = models.ForeignKey(User, on_delete=models.CASCADE)
	comment_text = models.TextField()

	def __str__(self):
		return 'Comment on ' + self.Post.post_title + ' from ' + self.User.username