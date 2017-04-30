from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Post
from .forms import PostModelForm


def save_post_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            posts = Post.objects.all()
            data['html_post_list'] = render_to_string('posts/includes/partial_post_list.html', {
                'posts': posts
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def post_create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
    else:
        form = PostModelForm()
    return save_post_form(request, form, 'posts/includes/partial_post_create.html')
