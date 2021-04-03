from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from posts.models import Post, PostCategory, PostOwner
from posts.api.serializers import PostApi, PostCategoryApi, PostOwnerApi



@api_view(['GET',])
def api_posts_view(request):
    try:
        post = Post.objects.all()#filter(post_status = 1)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostApi(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET',])
def api_post_details_view(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostApi(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET',])
def api_post_by_category_view(request, pk):
    try:
        post_by_category = Post.objects.filter(post_category = pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostApi(post_by_category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET',])
def api_post_by_owner_view(request, pk):
    try:
        post_by_owner = Post.objects.filter(post_owner = pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostApi(post_by_owner, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET',])
def api_post_categories_view(request):
    try:
        categories = PostCategory.objects.all()
    except PostCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostCategoryApi(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET',])
def api_post_owners_view(request):
    try:
        owners = PostOwner.objects.all()#filter(post_status = 1)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostOwnerApi(owners, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['POST',])
def api_post_create_view(request):
    if request.method == 'POST':
        serializer = PostApi(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



