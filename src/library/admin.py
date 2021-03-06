from django.contrib import admin
from . import models

from adminsortable2.admin import SortableInlineAdminMixin


class ModuleLessonInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.BaseLesson
    extra = 1

    def get_queryset(self, request):
        return self.model.objects.select_subclasses()


class ModuleAdmin(admin.ModelAdmin):
    inlines = (ModuleLessonInline,)


class WorkshopModuleInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.WorkshopModule
    extra = 1


class WorkshopAdmin(admin.ModelAdmin):
    inlines = (WorkshopModuleInline,)


class TrackWorkshopInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.TrackWorkshop
    extra = 1


class TrackAdmin(admin.ModelAdmin):
    inlines = (TrackWorkshopInline,)


admin.site.register(models.MarkdownLesson)
admin.site.register(models.QuizLesson)
admin.site.register(models.VideoLesson)
admin.site.register(models.Module, ModuleAdmin)
admin.site.register(models.WorkshopModule)
admin.site.register(models.Workshop, WorkshopAdmin)
admin.site.register(models.TrackWorkshop)
admin.site.register(models.Track, TrackAdmin)
admin.site.register(models.Profile)
