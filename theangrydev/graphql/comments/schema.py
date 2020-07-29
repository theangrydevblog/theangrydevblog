import graphene

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

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
        interfaces = (graphene.relay.Node,)
        fields = ('author','text')

class CommentConnection(graphene.relay.Connection):
    class Meta:
        node = CommentType

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    comments = graphene.relay.ConnectionField(CommentConnection, post_id=graphene.Int())
    
    def resolve_comments(root, info, post_id):
        return Comment.objects.filter(post__id=post_id)