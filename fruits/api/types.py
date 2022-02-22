import strawberry
from strawberry_django_plus import gql
from fruits import models
from strawberry.arguments import UNSET
from typing import List, Optional


@gql.django.type(models.Fruit)
class Fruit:
    id: gql.auto
    name: gql.auto
    color: 'Color'
    amount: gql.auto

@gql.django.type(models.Color)
class Color:
    id: gql.auto
    name: gql.auto
    fruits: List[Fruit]

@gql.django.input(models.Fruit)
class FruitInput:
    id: gql.auto
    name: gql.auto
    color: str
    amount: gql.auto

@gql.django.input(models.Fruit)
class CreateFruitInput:
    name: gql.auto
    color: str
    amount: gql.auto

@gql.django.input(models.Color)
class ColorInput:
    id: gql.auto
    fruits: gql.auto

@gql.django.input(models.Fruit)
class UpdateFruitInput:
    id: strawberry.ID
    name: Optional[str] = UNSET
    color: Optional[str] = UNSET
    amount: Optional[int] = UNSET

@gql.django.input(models.Fruit)
class DeleteFruitInput:
    id: strawberry.ID

@gql.django.input(models.Fruit)
class RetrieveFruitInput:
    id: strawberry.ID