from django.contrib import admin

# Register your models here.
from .models import Question, Choise

#admin.site.register(Question)
#admin.site.register(Choise)
class ChoinInline(admin.TabularInline):
    model = Choise

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines =[ChoinInline]