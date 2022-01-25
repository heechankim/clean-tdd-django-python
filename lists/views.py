from django.shortcuts import render, redirect
from lists.models import Item

# Create your views here.
# DONE: 22.01.10 : Feat: 모든 요청에 대한 비어 있는 요청은 저장하지 않는다.
# DONE: 22.01.10 : Feat: 테이블에 아이템 여러개 표시하기
# DONE: 22.01.10 : Feat: 하나 이상의 목록 지원하기


def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')
