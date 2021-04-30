from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from django_celery_results.models import TaskResult

from celeryapp.tasks import hello_world_task, send_email_task, show_index_task


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        show_index_task.delay()
        return context


class SayHelloView(View):

    def post(self, request):
        yourname = request.POST.get("yourname")
        hello_world_task.delay(yourname)
        return render(request, 'index.html')


class SendEmailView(View):

    def get(self, request):
        send_email_task.delay()
        return render(request, 'index.html')


class GetLast2minsTaskResultView(View):

    def get(self, request):
        last_result = TaskResult.objects.filter(
            task_name='celeryapp.tasks.every_2mins_beat').first()
        return render(request, 'index.html', {"last_result": last_result})
