# config/api_root.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.conf import settings


class APIRootView(APIView):
    """
    Links para todos os endpoints da aplicação.
    """

    def get(self, request, format=None):
        response_data = {
            "admin": reverse("admin:index", request=request),
            "accounts": reverse("users-list", request=request, format=format),
            "posts": reverse("posts-list", request=request, format=format),
            "likes": reverse("likes-list", request=request, format=format),
            "comments": reverse("comments-list", request=request, format=format),
            "followers": reverse("followers-list", request=request, format=format),
        }

        return Response(response_data)
