from ekatalog_alternative.apps.base.services.parse_wb import ParseWb
from django.shortcuts import redirect


def parse_wb_view(request):
    try:
        ParseWb(10, 'phones').start_service()
        ParseWb(10, 'laptops').start_service()
        return redirect('admin:index')
    except Exception as ex:
        raise Exception(f"Ошибка: {ex}")