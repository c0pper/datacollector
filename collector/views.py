from django.shortcuts import render, redirect
from .models import Submission
from .forms import SubmissionForm
from django.utils import timezone


# Create your views here.
def submission_form(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.created_date = timezone.now()
            submission.save()
            return redirect('submission_list')
    else:
        form = SubmissionForm()
    return render(request, 'collector/submission_form.html', {'form': form})


def submission_list(request):
    submissions = reversed(Submission.objects.filter(created_date__lte=timezone.now()).order_by('created_date'))
    return render(request, 'collector/submission_list.html', {'submissions': submissions})
