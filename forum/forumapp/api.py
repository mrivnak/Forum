from .models import User, Category, Board, Post, Comment
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, CategorySerializer, BoardSerializer, PostSerializer, CommentSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	permission_classes = [
		permissions.AllowAny  # TODO: Add proper permissions
	]
	serializer_class = UserSerializer
	
class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	permission_classes = [
		permissions.AllowAny  # TODO: Add proper permissions
	]
	serializer_class = CategorySerializer
	
class BoardViewSet(viewsets.ModelViewSet):
	queryset = Board.objects.all()
	permission_classes = [
		permissions.AllowAny  # TODO: Add proper permissions
	]
	serializer_class = BoardSerializer
	
class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	permission_classes = [
		permissions.AllowAny  # TODO: Add proper permissions
	]
	serializer_class = PostSerializer
	
class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	permission_classes = [
		permissions.AllowAny  # TODO: Add proper permissions
	]
	serializer_class = CommentSerializer