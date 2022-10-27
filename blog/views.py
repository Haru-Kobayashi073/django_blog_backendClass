from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
  return HttpResponse("Hello world.")

def index(request):
    return render(request, "blog/index.html")

def detail(request):
    return HttpResponse("detail page")
class AccountCreateView(View):
    def get(self, request):
        return render(request, "blog/register.html")
    def post(self, request):
        # ユーザー情報を保存する
        User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password"],
        )
        return render(request, "blog/register_success.html")
class AccountLoginView(LoginView):
    """ログインページのテンプレート"""
    template_name = 'blog/login.html'
    def get_default_redirect_url(self):
        """ログインに成功した時に飛ばされるURL"""
        return "/blog"
class MypageView(View):
    def get(self, request):
        return render(request, "blog/mypage.html")
class MypageView(LoginRequiredMixin, View):
    # ログインしていない場合に飛ばすページの設定
    login_url = '/blog/login'
    def get(self, request):
        return render(request, "blog/mypage.html")