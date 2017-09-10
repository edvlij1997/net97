from django.views.generic import TemplateView

from net97.post.models import Post

class HomePageView(TemplateView):

    template_name = "frontend/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        return context
