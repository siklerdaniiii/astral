from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Blog, BlogCategory
from blog.api.serializers import BlogApi, BlogCategoryApi



@api_view(['GET',])
def api_blog_view(request):
    try:
        blog = Blog.objects.all()#filter(blog_status = 1)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogApi(blog, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET',])
def api_blog_details_view(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogApi(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET',])
def api_blog_by_category_view(request, pk):
    try:
        blog_by_category = Blog.objects.filter(blog_category = pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogApi(blog_by_category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET',])
def api_blog_categories_view(request):
    try:
        categories = BlogCategory.objects.all()
    except BlogCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogCategoryApi(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




