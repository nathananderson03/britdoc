from django.contrib import admin

# Register your models here.

# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
# from django.contrib.admin.filters import DateFieldListFilter

from core.models import(
    Film,
    FilmImage,
    PurchaseLink,
    ShareLink,
    Goodpitch,
    Fund,
    Subject,
    Crew,
    Review,
    Laurel,
    Staff,
    Resource,
    ResourceCategory,
)

# class UserProfileInline(admin.StackedInline):
#     model = UserProfile

# class UserAdmin(AuthUserAdmin):
#     inlines = [UserProfileInline]

# # unregister old user admin
# admin.site.unregister(User)
# # register new user admin
# admin.site.register(User, UserAdmin)


class GoodpitchInline(admin.TabularInline):
    model = Goodpitch.films.through
    extra = 1


class LaurelInline(admin.TabularInline):
    model = Laurel
    extra = 1


class FilmImageInline(admin.TabularInline):
    model = FilmImage
    extra = 1


class PurchaseLinkInline(admin.TabularInline):
    model = PurchaseLink
    extra = 1


class ShareLinkInline(admin.TabularInline):
    model = ShareLink
    extra = 1


class CrewInline(admin.TabularInline):
    model = Crew.films.through
    extra = 1


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class FundInline(admin.TabularInline):
    model = Fund.films.through
    extra = 1


class SubjectInline(admin.TabularInline):
    model = Subject.films.through
    extra = 1


class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'stage', 'year', 'status', 'featured']
    list_filter = ['stage', 'year', 'status', 'featured']
    inlines = [SubjectInline, FilmImageInline, PurchaseLinkInline, ShareLinkInline, CrewInline, GoodpitchInline, FundInline, ReviewInline, LaurelInline]

admin.site.register(Film, FilmAdmin)

# class FilmImageAdmin(admin.ModelAdmin):
# 	list_display = ['film', 'image', 'width', 'height', 'primary', 'status',]

# admin.site.register(FilmImage, FilmImageAdmin)


class GoodpitchAdmin(admin.ModelAdmin):
    list_display = ['slug', 'title', 'status']

admin.site.register(Goodpitch, GoodpitchAdmin)


class FundAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['slug', 'name', 'image_name', 'status']

admin.site.register(Fund, FundAdmin)


class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['slug', 'name', 'status']

admin.site.register(Subject, SubjectAdmin)


class CrewAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['slug', 'role', 'name', 'status']

admin.site.register(Crew, CrewAdmin)

class StaffAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['slug', 'role', 'name', 'involvement']

admin.site.register(Staff, StaffAdmin)


class ResourceCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['slug', 'name', 'status']

admin.site.register(ResourceCategory, ResourceCategoryAdmin)

class ResourceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['slug', 'name', 'status']

admin.site.register(Resource, ResourceAdmin)

# class PaymentAdmin(admin.ModelAdmin):
#     list_display = ["user", "festival", "submission", "source", "processed", "refunded", "amount", "fee_amount", "settled_amount"]
#     list_filter = ("festival", "processed", "refunded", "source", ('settlement_date', DateFieldListFilter))
