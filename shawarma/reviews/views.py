from django.shortcuts import render
from.models import Reviews
from .forms import ReviewForm

# Create your views here.
def reviews(request):
    rev = Reviews.objects.all()
    form = ReviewForm()
    context = {
        "rev": rev,
        'form': form
    }

    return render(request, 'reviews/reviews.html', context)


