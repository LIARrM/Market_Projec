

from django.contrib import admin
from .models import Store, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

class StoreAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Store, StoreAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import UserForm

class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    model = CustomUser
    list_display = ['username', 'email', 'avatar', 'phone_number']  # Отображаемые поля в списке пользователей

    # Убедитесь, что добавляете поле `avatar` в поле `fieldsets` и `add_fieldsets`
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('avatar', 'phone_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('avatar', 'phone_number')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)