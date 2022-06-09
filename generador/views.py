from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View


class Index(View):
    def get(self, request):

        return render(request, 'principal.html')

    def post(self, request):
        '''if request.user.is_authenticated and request.POST.get('accion') == "comentarPost":
            usuario = request.user
            form = forms.CreateCommentForm(request.POST)
            if form.is_valid():
                post = Posts.objects.get(pk=request.POST.get('post_id'))
                txt_comentario = form.cleaned_data.get('comentario')
                Comentarios.objects.create(post=post, usuario=usuario, comentario=txt_comentario, popularidad=0)
                return redirect('/post/' + str(post.id))'''
        return redirect('inicio')


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def internal_error(request):
    return render(request, '500.html', status=500)