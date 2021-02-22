from django.contrib import admin
from tank.models import Tank
# Register your models here.

class TankAdmin(admin.ModelAdmin):
    """图书类型模型管理类"""

    # 数据分页，每页10条
    list_per_page = 10

    # 后台显示的属性（字段）
    list_display = ['id', 'name', 'country', 'start', 'end', 'costume']
    search_fields = ['id', 'name', 'country', 'start', 'end']
    list_filter = ['name', 'country', 'start', 'end']


admin.site.register(Tank,TankAdmin)
