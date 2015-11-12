from django.shortcuts import render, get_object_or_404, redirect
from .models import Match
from .forms import MatchForm

# Create your views here.
def predict_Match(request):
    matches = Match.objects.order_by('-published_date')[:5]
    return render(request, 'rmprediction/base.html', {'matches': matches})

def match_Detail(request, pk):
    matches = Match.objects.order_by('-published_date')[:5]
    match = get_object_or_404(Match, pk=pk)
    return render(request, 'rmprediction/match_detail.html', {'match': match, 'matches': matches})

def match_new(request):
    matches = Match.objects.order_by('-published_date')[:5]
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            match = form.save(commit=False)
            match.author = request.user
            match.publish()
            return redirect('rmprediction.views.match_Detail', pk=match.pk)
    else:
        form = MatchForm()
    return render(request, 'rmprediction/match_edit.html', {'form': form, 'matches': matches})
