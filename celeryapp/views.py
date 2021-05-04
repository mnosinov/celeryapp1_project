from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from django_celery_results.models import TaskResult
from celery.result import AsyncResult

from celeryapp.tasks import hello_world_task, send_email_task, show_index_task,\
        AuthTask, AddTask

from celeryapp.celery import app as celery_app


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


class AuthView(View):

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        auth_task = AuthTask()
        auth_task.delay(username, password)
        return render(request, 'index.html')


class AddView(View):

    def post(self, request):
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        add_task = AddTask()
        task_id = add_task.delay(num1, num2)
        task_result = AsyncResult(task_id, app=celery_app)
        add_result = task_result.get()
        return render(request, 'index.html', {"add_result": add_result})
