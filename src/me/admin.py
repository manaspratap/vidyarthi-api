from django.contrib import admin

# Register your models here.
from me.models import CollaborateModel, ProjectModel, CourseModel, SuggestionModel

admin.site.register(CollaborateModel)
admin.site.register(ProjectModel)
admin.site.register(CourseModel)
admin.site.register(SuggestionModel)
