from django.shortcuts import render
from django.http import HttpResponse
from gensim.models import Word2Vec

# Create your views here.
def index(request):
    context = {'a':'Hello'}
    return render(request,'index.html',context)
    #return HttpResponse()
def predictMPG(request):
 #   print(context)
    if request.method ==  'POST':
       # print(request.POST.dict())
        model = Word2Vec.load('./models/model.bin')
        chr = request.POST.get('cylinderVal')
        topten = [i[0] for i in model.wv.most_similar(str(chr))]
        context = {
            'cylinderVal':str(chr),
            'topsimilar':topten}
       # print(topten)
    return render(request,'index.html',context)