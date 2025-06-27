from django.shortcuts import redirect


class Redirector:
    @staticmethod
    def api_redirect(request):
        return redirect('/api/swagger/')


    @staticmethod
    def admin_redirect(request):
        return redirect('/admin/')
