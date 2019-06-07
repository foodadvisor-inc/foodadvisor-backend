import coreapi
import coreschema
from rest_framework.schemas import AutoSchema


class CurrentUserCategorySchema(AutoSchema):

    def get_manual_fields(self, path, method):

        extra_fields = []

        if method == 'POST' or method == 'PUT':
            extra_fields = [
                coreapi.Field(
                    "categories",
                    required=True,
                    location="form",
                    example="['peanut', 'sugar', 'milk', 'egg']",
                    description="List of added categories: ['peanut', 'sugar', 'milk', 'egg']",
                    schema=coreschema.Array(items=coreschema.String())
                ),
            ]

        if method == 'DELETE':
            extra_fields = [
                coreapi.Field(
                    "categories",
                    required=True,
                    location="form",
                    description="List of deleted category_id: ['peanut', 'sugar', 'milk', 'egg']",
                    schema=coreschema.Array(items=coreschema.String())
                ),
            ]

        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class CurrentUserIngredientSchema(AutoSchema):

    def get_manual_fields(self, path, method):

        extra_fields = []

        if method == 'POST' or method == 'PUT':
            extra_fields = [
                coreapi.Field(
                    "ingredients",
                    required=True,
                    location="form",
                    description="List of added ingredients: [{id:1,rate:100}]",
                    schema=coreschema.Array(items=coreschema.Object(properties={'id': 1, 'rate': 0}),
                                            description="List of ingredients", )
                ),
            ]

        if method == 'DELETE':
            extra_fields = [
                coreapi.Field(
                    "ingredients",
                    required=True,
                    location="form",
                    description="List of deleted ingredient_id: [1,2,4]",
                    schema=coreschema.Array(items=coreschema.Integer(), description="List of id", )
                ),
            ]

        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class CurrentUserGoalSchema(AutoSchema):

    def get_manual_fields(self, path, method):
        extra_fields = []

        if method == 'POST' or method == 'PUT':
            extra_fields = [
                coreapi.Field(
                    "goal",
                    required=True,
                    location="form",
                    description="Goal id",
                    schema=coreschema.Integer(minimum=1, default=1),
                ),
            ]

        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class CurrentUserProfileSchema(AutoSchema):

    def get_manual_fields(self, path, method):
        extra_fields = []

        if method == 'POST' or method == 'PATCH':
            extra_fields = [
                coreapi.Field(
                    "gender",
                    required=False,
                    location="form",
                    description="0 - male, 1 -  female, 2 - not specified",
                    schema=coreschema.Integer(minimum=0, default=1)
                ),
                coreapi.Field(
                    "weight",
                    required=False,
                    location="form",
                    description="In grams",
                    schema=coreschema.Integer(minimum=10000)
                ),
                coreapi.Field(
                    "height",
                    required=False,
                    location="form",
                    description="In centimeter",
                    schema=coreschema.Integer(minimum=50)
                ),
                coreapi.Field(
                    "birth_date",
                    required=False,
                    location="form",
                    description="Like 1998-05-08",
                    schema=coreschema.String()
                ),

            ]

        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields
