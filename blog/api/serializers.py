from rest_framework import  serializers
from blog.models import Blog, BlogCategory

class BlogCategoryApi(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"

class BlogApi(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='blog_category.blog_category_name')

    class Meta:
        model = Blog
        fields = "__all__"



