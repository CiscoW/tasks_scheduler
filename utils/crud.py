from __future__ import absolute_import, unicode_literals
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response


class CRUD(mixins.RetrieveModelMixin,
           mixins.CreateModelMixin,
           mixins.ListModelMixin,
           mixins.UpdateModelMixin,
           mixins.DestroyModelMixin,
           generics.GenericAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        if args or kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # Override 单条和批量新增
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, dict):
            serializer = self.get_serializer(data=request.data)
        else:
            serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
