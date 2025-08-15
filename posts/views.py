from django.shortcuts import render
from rest_framework import generics, permissions


from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAdminUser, )


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    # permission_classes = (permissions.IsAdminUser, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
