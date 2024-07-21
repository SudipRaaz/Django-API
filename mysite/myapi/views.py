from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view 

from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from django.shortcuts import get_object_or_404

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    #delete all posts
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status.HTTP_204_NO_CONTENT)

#customized search with id
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"

class BlogPostRetrieveTitle(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "title"

class BlogPostRetrieve(APIView):
    def get(self, request, format= None):
        #get the tittle from the query parameters
        title = request.query_params.get('title', '')

        if title:
            blog_post = BlogPost.objects.filter(title=title)
        else:
            blog_post = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


@api_view(['POST'])
def Login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'details': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if not user.check_password(password):
        return Response({'details': 'Incorrect password'}, status=status.HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({'token': token.key, "data": serializer.data})

@api_view(['POST'])
def Signup(request, ):
    serializers = UserSerializer(data = request.data)
    if serializers.is_valid():
        serializers.save()
        user = User.objects.get(username=serializers.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, "data": serializers.data})
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Test_token(request,):
    return Response({'token':"loading_token"})


class userlistfetcher(APIView):
    def get(self, request, *args, **kwargs):
        query = User.objects.all()
        serializers = UserSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def delete(self, request, user_id, *args, **kwargs):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return Response({"message": f"User with ID {user_id} has been deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"error": f"User with ID {user_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)


# get update delete users
class ReadUpdateDeleteUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"