from django.http import HttpResponse

from .models import Document

from django.shortcuts import render


def index(request):
    document_list = Document.objects.order_by('-title')[:5]
    context = {'document_list': document_list}
    return render(request, 'documents/index.html', context)
