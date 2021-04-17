from rest_framework import  serializers
from blog.models import Blog, BlogCategory
from django.contrib.auth.models import User

class BlogCategoryApi(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"

class BlogApi(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='blog_category.blog_category_name')
    owner_name = serializers.ReadOnlyField(source='blog_owner.blog_owner_name')
    owner_meta = serializers.ReadOnlyField(source='blog_owner.blog_owner_meta')
    owner_image = serializers.ReadOnlyField(source='blog_owner.blog_owner_image.url')

    class Meta:
        model = Blog
        fields = "__all__"



