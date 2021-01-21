from django.contrib import admin
from .models import User,Record


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'current_credits', 'mail_id', 'Phone_num']

admin.site.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['Name_Of_Sender', 'Name_Of_Receiver', 'Transfer_Amount', 'Sender_Updated_Balance', 'Receiver_Updated_Balance']