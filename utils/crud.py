from __future__ import absolute_import, unicode_literals
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .permissions import CustomObjectPermissions


# 新增数据Create
class CreateMixin(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    permission_classes = (IsAuthenticated, CustomObjectPermissions)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

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


# 读取数据Retrieve
# 单条
class RetrieveMixin(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    permission_classes = (IsAuthenticated, CustomObjectPermissions)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# 读取数据Retrieve
# 全部
class RetrieveListMixin(mixins.ListModelMixin,
                        generics.GenericAPIView):
    permission_classes = (IsAuthenticated, CustomObjectPermissions)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# 更新数据 Update
class UpdateMixin(mixins.UpdateModelMixin,
                  generics.GenericAPIView):
    permission_classes = (IsAuthenticated, CustomObjectPermissions)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# 删除数据 Delete
class DeleteMixin(mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    permission_classes = (IsAuthenticated, CustomObjectPermissions)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data=[], status=status.HTTP_200_OK)
