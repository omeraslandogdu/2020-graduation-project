from django.contrib import admin
from applications.core.admin import RelatedObjectLinkMixin
from applications.recognition.models.user import User, UserToken, UserType
from applications.recognition.models.entity_type import EntityType
from django.contrib.auth.admin import UserAdmin
from .forms import UserAdminChangeForm, UserAdminCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class BaseModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(BaseModelAdmin, self).get_queryset(request)
        if request.user.admin:
            return qs.filter(deleted_at=None)

        return qs.filter(user=request.user.id)


@admin.register(UserToken)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')
    fields = ('user', 'key',)

    def get_queryset(self, request):
        qs = super(TokenAdmin, self).get_queryset(request)
        if request.user.admin:
            return qs

        return qs.filter(id=request.user.id)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = \
        (
            'id',
            'email',
            'admin',
            'fullname',
            'entity_type'
        )
    list_filter = ('admin', 'active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if request.user.admin:
            return qs

        return qs.filter(id=request.user.id)


@admin.register(UserType)
class UserTypeAdmin(RelatedObjectLinkMixin, BaseModelAdmin):
    list_display = (
        'id',
        'title',
        'user',
        'entity_type_link',
        'created_at',
        'updated_at',
        'status',
    )
    change_links = ('entity_type',)


@admin.register(EntityType)
class EntityTypeAdmin(RelatedObjectLinkMixin, BaseModelAdmin):
    list_display = (
        'id',
        'title',
        'key',
        'created_at',
        'updated_at',
        'status',
    )
    change_links = ('entity_type',)
