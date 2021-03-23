from rest_framework import  serializers
from posts.models import Post, PostCategory, PostOwner

class PostCategoryApi(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = "__all__"

class PostOwnerApi(serializers.ModelSerializer):
    class Meta:
        model = PostOwner
        fields = "__all__"

class PostApi(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='post_category.post_category_name')
    owner_name = serializers.ReadOnlyField(source='post_owner.post_owner_name')

    class Meta:
        model = Post
        fields = "__all__"



