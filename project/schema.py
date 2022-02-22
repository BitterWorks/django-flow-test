import strawberry
from strawberry_django_plus import gql, optimizer, directives
from typing import List

from fruits.api import types, resolvers

@gql.type
class Query:
    fruits: List[types.Fruit] = gql.django.field()
    fruit: types.Fruit = strawberry.field(resolver=resolvers.fruit)

@gql.type
class Mutation:

    create_fruit: types.Fruit = strawberry.mutation(
        resolver=resolvers.create_fruit
    )
    update_fruit: types.Fruit = strawberry.mutation(
        resolver=resolvers.update_fruit
    )
    delete_fruit: types.Fruit = strawberry.mutation(
        resolver=resolvers.delete_fruit
    )

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        optimizer.DjangoOptimizerExtension,
        directives.SchemaDirectiveExtension
    ]
)