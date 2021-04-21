from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from django.db.models import Q

from posts.models import Post, PostCategory, PostOwner
from memberships.models import Plan, Member
from posts.api.serializers import PostApi, PostCategoryApi, PostOwnerApi
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend


@api_view(['GET',])
def api_posts_view(request):
    try:
        post = Post.objects.all().exclude(post_status = 0)#filter(post_status = 1)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostApi(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET',])
def api_post_paid_view(request, uid):
    try:
        member = Member.objects.filter(Q(member_uid = uid) and Q(member_status = 1)).order_by('member_since').first()  #rendezve a legutolsó előfizetés szerint
        is_member = Member.objects.filter(member_uid = uid).last()
        #ha member akkor lekérem azt, hogy aktiv e
        if is_member and is_member.member_status == 1:
            print('Ő member és aktív is')
            #ha aktív akkor lekérem a hozzá tartozó cikkeket, ha nem akkor ingynees tartalmat jeleniti meg neki
            member_plan = is_member.member_plan.plan_slug #aktuális tagság
            print(member_plan)
            posts = Post.objects.filter(Q(post_plan__plan_slug = member_plan) or Q(post_plan__plan_slug = 'free')).distinct() #ide majd egy exlude draft maitt
            print(posts)
        else:
            print('Nem member vagy nem aktiv')
            posts = Post.objects.filter(post_plan__plan_slug = 'free')
            print('Ingyenes psoztok:',posts)
    except Member.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
   

    if request.method == 'GET':
        serializer = PostApi(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class BookmarkList(ListAPIView):
    serializer_class = PostApi
    def get_queryset(self):
        # Get URL parameter as a string, if exists 
        ids = self.request.query_params.get('ids', None)
        # Get snippets for ids if they exist
        if ids is not None:
            # Convert parameter string to list of integers
            ids = [ int(x) for x in ids.split(',') ]
            # Get objects for all parameter ids 
            queryset = Post.objects.filter(id__in=ids).exclude(post_status = 0)
        else:
            # Else no parameters, return all objects
            queryset = Post.objects.all()
        return queryset

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
        post_by_category = Post.objects.filter(post_category = pk).exclude(post_status = 0)
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


#ezt majd törölni
@api_view(['POST',])
def api_post_create_view(request):
    if request.method == 'POST':
        serializer = PostApi(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



