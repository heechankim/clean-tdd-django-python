from django.shortcuts import render, redirect
from lists.models import Item, List

# Create your views here.
# DONE: 22.01.10 : Feat: 모든 요청에 대한 비어 있는 요청은 저장하지 않는다.
# DONE: 22.01.10 : Feat: 테이블에 아이템 여러개 표시하기
# DONE: 22.01.10 : Feat: 하나 이상의 목록 지원하기


def home_page(request):
    return render(request, 'home.html')


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))