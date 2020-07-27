from django.db import models

# Create your models here.
class User(models.Model):
	UserID = models.AutoField(primary_key=True)
	user_username = models.CharField(max_length=24)
	user_name = models.CharField(max_length=32)
	user_department = models.CharField(max_length=64, blank=True)
	user_email = models.EmailField()
	user_password = models.CharField(max_length=128)  # large max length to accomodate hashes
	user_avatar = models.ImageField(blank=True)
	user_signature = models.CharField(max_length=512, blank=True)
	user_is_admin = models.BooleanField(default=False)

	def __str__(self):
		return self.user_username

class Category(models.Model):
	CategoryID = models.AutoField(primary_key=True)
	category_title = models.CharField(max_length=64)

	def __str__(self):
		return self.category_title

class Board(models.Model):
	BoardID = models.AutoField(primary_key=True)
	board_title = models.CharField(max_length=64)
	Category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.board_title

class Post(models.Model):
	PostID = models.AutoField(primary_key=True)
	Board = models.ForeignKey(Board, on_delete=models.CASCADE)
	post_title = models.CharField(max_length=64)
	post_time = models.DateTimeField(auto_now=True)
	User = models.ForeignKey(User, on_delete=models.CASCADE)
	post_text = models.CharField(max_length=1024)

	def __str__(self):
		return self.post_title

class Comment(models.Model):
	CommentID = models.AutoField(primary_key=True)
	Post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment_time = models.DateTimeField(auto_now=True)
	User = models.ForeignKey(User, on_delete=models.CASCADE)
	comment_text = models.CharField(max_length=1024)

	def __str__(self):
		return 'Comment on ' + self.Post.post_title + ' from ' + self.User.user_username