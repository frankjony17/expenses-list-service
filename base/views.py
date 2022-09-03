from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class BaseModelViewSet(ModelViewSet):
    queryset = []
    serializers = {'default': None}
    pagination_class = None
    http_method_names = ['get', 'post', 'put', 'delete']

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
        instance = self.get_object()
        serializer = self.get_serializer_class()(
            data=request.data, instance=instance, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance=instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
