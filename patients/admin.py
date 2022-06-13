from django.contrib import admin

from patients.models import Appointment, Patient

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', "age",  'address', 'city', 'state', 'zipcode', 'created_at', 'updated_at', "is_active", "slug")
    list_editable = ( "is_active", )
    list_filter = ('created_at',)
    search_fields = ('name', 'phone',  'state')
    ordering = ('-created_at',)
    prepopulated_fields= {'slug': ('name',)}
    list_per_page = 25

    fieldsets = (
        (None, {
            "fields": (
                ('name', 'email'), ("phone", "birthday" ),"is_active"  # to display multiple fields on the same line, wrap those fields in their own tuple
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("address", "city", "state", "zipcode", "slug"),
            'description' : "You can use this section for optionals settings"
        })
    )
# get age from model method
    def age(self, patient):
        return patient.get_age()

admin.site.register(Patient, PatientAdmin),
admin.site.register(Appointment)

admin.site.site_header = "Healthination Admin"
admin.site.site_title = "Healthination Admin Portal"
admin.site.index_title = "Welcome to Healthination Admin Portal"
admin.site.empty_value_display = '-empty-'

