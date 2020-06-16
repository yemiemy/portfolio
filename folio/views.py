from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import Blog, Comment, Contact, Recommendation, Project, Tag
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import ListView
# Create your views here.
def index(request):
    try:
        posts = Blog.objects.filter(featured=True).order_by('-id')
        recommends = Recommendation.objects.filter(active=True).order_by('-id')
        projects = Project.objects.all()
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            date_stamp = datetime.now()
            
            contact_me = Contact.objects.create(name=name, email=email, subject=subject, message=message, date_stamp=date_stamp)
            contact_me.save()
            messages.success(request, 'Your message has been successfully sent! Thanks for reaching out.')
            context = {
                'name':name,
                'email':email,
                'message':message,
            }
            body = render_to_string('folio/contact_form.txt', context)
            send_mail('Contact Form: {}'.format(subject), body, 'rasholayemi@gmail.com', ['rasholayemi@gmail.com'])

            # Send back an automated email to contact
            contexts = {
                'name':name,
            }
            reply = render_to_string('folio/reply.txt', contexts)
            send_mail('Rash Olaoluwayemi Contact Form: {}'.format(subject), reply, 'rasholayemi@gmail.com', [email])
        title = 'Olaoluwayemi Rasheed'
    except Exception as e:
         return render(request, 'folio/error.html', {'e':e, 'year':datetime.now().year})
    return render(request, 'folio/index.html', {
        'posts':posts,
        'title':title, 
        'year':datetime.now().year, 
        'recommends':recommends,
        'projects':projects
        })


class PostListView(ListView):
    model = Blog
    template_name = 'folio/blog.html'
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 4
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'objects': Blog.objects.all().order_by('-date_stamp')[:5],
            'year':datetime.now().year,
            'tags': Tag.objects.all() 
        })  
        return context
    

class TagPostListView(ListView):
    model = Blog
    template_name = 'folio/tag_post.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'objects': Blog.objects.all().order_by('-date_stamp')[:5],
            'year':datetime.now().year,
            'tags': Tag.objects.all() 
        })  
        return context

    def get_queryset(self):
        tag = get_object_or_404(Tag, name=self.kwargs.get('name'))
        return Blog.objects.filter(tag=tag).order_by('-id')



def single(request, pk, slug):
    try:
        post = Blog.objects.get(slug=slug)
        posts = Blog.objects.all()[:5]
        comments = post.comments.all()
        count = 0
        for com in comments:
            if com.active:
                count+=1
        if request.method == 'POST':
            writer = request.POST['name']
            email = request.POST['email']
            website = request.POST['web']
            body = request.POST['message']

            comment = Comment.objects.create(
                post=post,
                writer=writer,
                email=email,
                website=website,
                body=body,
                published = datetime.now()
                )
            comment.save()
        title = 'Olaoluwayemi Rasheed'
    except Exception as e:
        return render(request, 'folio/error.html', {'e':e})
    return render(request, 'folio/blog-single.html', {
        'post':post,
        'posts':posts,
        'comments':comments,
        'title':title,
        'tags': Tag.objects.all(), 
        'count':count, 
        'year':datetime.now().year,})

def search_view(request):
	query = request.GET['query']
	posts = Blog.objects.filter(title__icontains=query)|Blog.objects.filter(body__icontains=query)
	
	return render(request, 'folio/search.html', {'posts':posts, 'query':query, 'year':datetime.now().year,})

def recommend(request):
    if request.method == 'POST':
        name = request.POST['name']
        recommend = request.POST['recommend']

        recommendation = Recommendation.objects.create(
            name=name,
            recommendation=recommend,
            active = False
        )
        if request.FILES:
            image = request.FILES['image']
            recommendation.image = image
            recommendation.save()
            messages.success(request, 'Your recommendation has been successfully sent! Thanks for recommending me.')
        return redirect('index')
    return render(request, 'folio/recommend.html', {})
