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
                    location="application/json",
                    description="List of added category_id: [1,2,4]",
                    schema=coreschema.Array(items=coreschema.Integer(minimum=1, default=1), description="List of id", )
                ),
            ]

        if method == 'DELETE':
            extra_fields = [
                coreapi.Field(
                    "categories",
                    required=True,
                    location="application/json",
                    description="List of deleted category_id: [1,2,4]",
                    schema=coreschema.Array(items=coreschema.Integer(minimum=1, default=1), description="List of id", )
                ),
            ]

        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields