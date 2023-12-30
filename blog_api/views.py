from rest_framework import generics
from  blog.models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset =Post.postobjects.all()
    serializer_class = PostSerializer
    pass

class PostDetails(generics.RetrieveDestroyAPIView):
    queryset =Post.objects.all()
    serializer_class = PostSerializer
    pass 

