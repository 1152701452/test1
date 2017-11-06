# encoding: utf-8
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # a = ['白夜追凶', '秦时明月', '天行九歌']
    a = []
    hot_file = {
        "first":"战狼2",
        "second": "魔兽",
        "third": "羞羞的铁拳",

    }

    return render(request, 'index.html', {"name_list": a, "hot_files": hot_file})