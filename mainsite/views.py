from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Board
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    return render(request, 'mainsite/index.html')

def newBoard(request):
    content = {}
    try:
        if request.method == 'POST' or 'FILES':
            title = request.POST.get('title')
            username = request.POST.get('username')
            contents = request.POST.get('contents')
            image = request.FILES['image']
            board = Board(
                title = title,
                username = username,
                contents = contents,
                image = image,
            )
            board.save()
            content = {'board': board}
        else:
            errMsg = "잘못된 접근입니다."
            content = {'errMsg': errMsg}
    except:
        errMsg = "서버 오류입니다."
        content = {'errMsg': errMsg}
    
    return redirect(reverse('listBoard'))

def listBoard(request):
    content={}
    try:
        boards = Board.objects.all()
        paginator = Paginator(boards, 5)
        page= request.GET.get('page')
        posts = paginator.get_page(page)
        content = {'boards':boards,'posts':posts}
    except:
        errMsg = "서버 오류입니다."
        content = {'errMsg': errMsg}
    return render(request, 'mainsite/boardList.html', content)

def viewBoard(request, id):
    content={}
    try:
        board = Board.objects.get(id=id)
        board.lookup += 1
        board.save()
        content = { 'board':board }
    except:
        errMsg = "서버 오류입니다."
        content = {'errMsg': errMsg}
    return render(request, 'mainsite/boardView.html', content)    

def updateDelete(request, id):
    content={}
    if request.POST.get('updateordelete'):
        board = Board.objects.get(id=id)

        title = request.POST.get('title')
        username = request.POST.get('username')
        contents = request.POST.get('contents')

        board.title = title
        board.username = username
        board.contents = contents
        board.save()

        content = { 'board': board }
        return render(request, 'mainsite/boardView.html', content)

    else:
        board = Board.objects.get(id=id)
        board.delete()

        return redirect('listBoard')

def updatepage(request, id):
    board = Board.objects.get(id=id)
    content={'board': board}
    return render(request, 'mainsite/update.html', content)

