from django.views.generic import TemplateView

from celeryapp.tasks import hello_world, send_email_task


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        hello_world.delay('Donnald Duck')
        send_email_task.delay()
        return context
