from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class BaseModelViewSet(ModelViewSet):
    queryset = []
    serializers = {'default': None}
    http_method_names = ['get', 'post', 'put', 'delete']
    instance = None
    swagger_fake_view = None

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        instance = self.get_model_object()
        serializer = self.get_serializer_class()(
            data=request.data, instance=instance, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        self.perform_destroy(instance=self.get_model_object())

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_model_object(self, model=None, pk=None):
        try:
            match self.instance:
                case None if pk:
                    self.instance = model.objects.get(pk=pk)
                case None if not pk:
                    self.instance = self.get_object()
        except model.DoesNotExist:
            raise NotFound()

    def raise_list_permission_denied(self):
        if self.swagger_fake_view:
            return self.queryset
        raise PermissionDenied()
