from django.contrib import admin
from applications.core.admin import RelatedObjectLinkMixin
from applications.recognition.models.user import User, UserToken, UserType
from applications.recognition.models.entity_type import EntityType
from django.contrib.auth.admin import UserAdmin
from .forms import UserAdminChangeForm, UserAdminCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from applications.recognition.models.models import Course, Student
from applications.recognition.models.user import Attendance


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
        if request.user.entity_type == 7:
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
        ('Personal info', {'fields': ('entity_type', 'fullname')}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'fullname','password1', 'password2', 'entity_type')}
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

    def get_queryset(self, request):
        qs = super(UserTypeAdmin, self).get_queryset(request)
        if request.user.admin:
            return qs

        return qs.filter(id=request.user.id)


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

    def get_queryset(self, request):
        qs = super(EntityTypeAdmin, self).get_queryset(request)
        if request.user.admin:
            return qs


@admin.register(Student)
class StudentAdmin(RelatedObjectLinkMixin, BaseModelAdmin):
    list_display = (
        'id',
        'user',
        'student_id',
        'phone',
        'created_at',
        'updated_at',
        'status',
    )
    change_links = ('user')

    def get_queryset(self, request):
        qs = super(StudentAdmin, self).get_queryset(request)
        if request.user.admin:
            return qs
        
        return qs.filter(request.user.id)


@admin.register(Course)
class CourseAdmin(RelatedObjectLinkMixin, BaseModelAdmin):
    list_display = (
        'id',
        'code',
        'title',
        'date',
        'user',
        'created_at',
        'updated_at',
        'status',
    )
    change_links = ('user')

    def get_queryset(self, request):
        qs = super(CourseAdmin, self).get_queryset(request)
        if request.user.admin:
            return qs
        
        return qs.filter(request.user.id)


@admin.register(Attendance)
class AttandanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'conf')