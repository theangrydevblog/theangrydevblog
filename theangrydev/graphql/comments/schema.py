import graphene

from graphene_django.types import DjangoObjectType

from theangrydev.models import (
    User,
    Comment  
)

class AuthorType(DjangoObjectType):
    class Meta:
        model = User

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ('author','text')

class Query(graphene.ObjectType):
    comments = graphene.List(CommentType, post_id=graphene.Int())

    def resolve_comments(self, info, post_id):
        return Comment.objects.filter(post__id=post_id)