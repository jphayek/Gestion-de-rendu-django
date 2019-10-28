from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.http import Http404
from polls.models import Poll
from .forms import FileFieldForm
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def my_view(request):
    # ...
    if foo:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>')


def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'polls/detail.html', {'poll': p})


class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'base.html' 
    success_url = '...' 
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  
            return self.form_valid(form)
        else:
            return self.form_invalid(form)