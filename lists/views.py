from django.shortcuts import render, redirect
from lists.models import Item

# Create your views here.
# DONE: 22.01.10 : Feat: 모든 요청에 대한 비어 있는 요청은 저장하지 않는다.
# TODO: 22.01.10 : Feat: 테이블에 아이템 여러개 표시하기
# TODO: 22.01.10 : Feat: 하나 이상의 목록 지원하기
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})