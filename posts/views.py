from django.contrib.auth.mixin import LoginRequiredMixinx
from django.url import reverse_lazy
from django.views import generic
from braces.views import SelectRelatedMixin
from django.http import Http404

from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()


class PostList(SelectRelatedMixin,generic.ListView):

    model = models.Post
    select_related = ('user','group')

class UserPosts(generic.ListView):

    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post.user = User.objects.prefetch_related('post').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class PostDetail(SelectRelatedMixin,generic.DetailView):

    model = models.Post
    select_related = ('user','group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixinx,SelectRelatedMixin,generic.CreteView):

    model = models.Post
    fields = ('message','group')

    def form_valid(self):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixinx,SelectRelatedMixin,generic.DetailView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        self.queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete(*args,**kwargs) 
