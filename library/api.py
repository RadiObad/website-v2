from rest_framework import generics

from . import serializers
from . import models


class LessonListAPIView(generics.ListAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer


class ModuleListAPIView(generics.ListAPIView):
    queryset = models.Module.objects.all()
    serializer_class = serializers.ModuleSerializer


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Module.objects.all()
    serializer_class = serializers.ModuleSerializer


# class ModuleLessonListAPIView(generics.ListAPIView):
#    queryset = models.ModuleLesson.objects.all()
#    serializer_class = serializers.ModuleLessonSerializer
#
#
# class ModuleLessonRetrieveAPIView(generics.RetrieveAPIView):
#    queryset = models.ModuleLesson.objects.all()
#    serializer_class = serializers.ModuleLessonSerializer


class WorkshopListAPIView(generics.ListAPIView):
    queryset = models.Workshop.objects.all()
    serializer_class = serializers.WorkshopSerializer

    def get_queryset(self):
        return self.queryset.filter(trackworkshop__track_id=self.kwargs.get('track_pk'))


class WorkshopRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Track.objects.all()
    serializer_class = serializers.WorkshopSerializer


class TrackListAPIView(generics.ListAPIView):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer


class TrackRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer


# class TrackWorkshopListAPIView(generics.ListAPIView):
#    queryset = models.TrackModule.objects.all()
#    serializer_class = serializers.TrackModuleSerializer
#
#
# class TrackWorkshopRetrieveAPIView(generics.RetrieveAPIView):
#    queryset = models.TrackModule.objects.all()
#    serializer_class = serializers.TrackModuleSerializer
