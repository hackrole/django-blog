from polls.models import Poll,Choice
from django.contrib import admin


class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class PollsAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['question']}),
            ('Date information',{'fields':['pub_date']}),
            ]
    inlines = [ChoiceInline]
admin.site.register(Poll, PollsAdmin)
admin.site.register(Choice)
