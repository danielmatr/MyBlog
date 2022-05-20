from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, generics
from .models import *
from .serializers import CategorySerializer, PostSerializer, PostImageSerializer

"""
views на функциях
"""


# @api_view(['GET', 'POST'])
# def categories(request):
#     if request.method == "GET":
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True) #many=True чтобы мог включать несколько обьектов
#         return Response(serializer.data)
#     else:
#         return Response({"message": "Попробуйте метод <GET>"})


"""
ApiView на классах
"""


# class PostListView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializers = PostSerializer(posts, many=True)
#         return Response(serializers.data)
#
#     def post(self, request):
#         post = request.data
#         serializer = PostSerializer(data=post) #many=true не указваем потому что будем создавать только один пост
#         if serializer.is_valid(raise_exception=True): #все поля заполнены
#             post_saved = serializer.save()
#         return Response(serializer.data)


"""
Views на generic
"""


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class PostView(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostUpdateDestroyView(generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetailView(generics.RetrieveAPIView): # чтение конкретной записи
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
class PostImageView(generics.ListAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}


"""
viewsets 
"""


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

