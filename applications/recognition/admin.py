from django.contrib import admin
from applications.core.admin import RelatedObjectLinkMixin
from applications.recognition.models.user import Client, User, ClientToken, UserType


class BaseModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(BaseModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(deleted_at=None)

        return qs.filter(client=request.user.id, deleted_at=None)


@admin.register(ClientToken)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')
    fields = ('user', 'key',)

    def get_queryset(self, request):
        qs = super(TokenAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(id=request.user.id)


@admin.register(Client)
class ClientAdmin(BaseModelAdmin):
    list_display = (
        'id',
        'app_name',
        'app_id',
        'is_superuser',
        'is_active',
    )

    def get_queryset(self, request):
        qs = super(ClientAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(id=request.user.id)


@admin.register(User)
class UserAdmin(BaseModelAdmin):
    list_display = (
        'id',
        '__str__',
        'client',
        'created_at',
        'updated_at',
        'status',
    )
    search_fields = ['fullname', 'email']
    list_filter = (
        'client',
        'status',
    )


@admin.register(UserType)
class UserTypeAdmin(RelatedObjectLinkMixin, BaseModelAdmin):
    list_display = (
        'id',
        'title',
        'entity_type_link',
        'client',
        'created_at',
        'updated_at',
        'status',
    )
    change_links = ('entity_type',)
