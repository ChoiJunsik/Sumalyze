from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# from lexrankr import LexRank

def main(request):
    return render(request, 'sumalyze/main.html')

# def experiment(request):
#     if request.method == "POST":
#         lexrank = LexRank()  # can init with various settings
#         text = request.POST['content']
#         lexrank.summarize(text)
#         summaries = lexrank.probe(3)
#         return render(request, 'sumalyze/experiment.html',{'summaries':summaries},)
#     return render(request, 'sumalyze/experiment.html')