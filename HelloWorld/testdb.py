# -*- coding: utf-8 -*-

from django.http import HttpResponse
from TestModel.models import Test


# 数据库操作
def insert(request):
    test1 = Test(name='wangy')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


def query(request):
    response = ""
    response1 = ""

    list = Test.objects.all()

    response2 = Test.objects.filter(id=1)

    response3 = Test.objects.get(id=1)

    Test.objects.order_by('name')[0:2]

    Test.objects.order_by('id')

    Test.objects.filter(name='wangy').order_by('id')

    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


def update(request):
    test1 = Test.objects.get(id=1)
    test1.name = 'wangzihan'
    test1.save()

    # Test.objects.filter(id=1).update(name='hanxiaona')

    return HttpResponse("<p>修改成功</p>")


def delete(request):
    test1 = Test.objects.get(id=1)
    test1.delete()

    return HttpResponse("<p>删除成功</p>")
