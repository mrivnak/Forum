from rest_framework import serializers
from .models import User, Category, Board, Post, Comment

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'

class BoardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Board
		fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'