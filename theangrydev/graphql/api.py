import graphene


from .comments import CommentQueries
from .comments import CommentMutations

class Query(CommentQueries):
    pass

class Mutation(CommentMutations):
    pass

schema = graphene.Schema(query=Query)