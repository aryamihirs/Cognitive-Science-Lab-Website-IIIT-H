from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

#importing models from models and forms.
from .models import Post, Comment, About, Volunteer, Video, Gallery
from django.contrib.auth.models import User
from .models import CommentForm, VolunteerForm
from .forms import NameForm

from django.db.models import Q
   
from variables import *

#function to validate page numbers for posts and comments.
def validate_page_number(page_number, size, items_per_page):
	if page_number <= 1:
		return 1
	else:
		number_of_pages = size/items_per_page
		if size%items_per_page != 0:
			number_of_pages += 1
		if page_number > number_of_pages:
			page_number = number_of_pages
		return page_number


def validate_text(_string):
	for word in rmv_words:
		if word in _string:
			return 0
	return 1

#***********MAIN FUNCTIONS************#

#temporary for now.
def index(request):
	posts_list = Post.objects.order_by('-pub_date')[:5]
	context = {'posts_list': posts_list}
	return render (request, 'labs/index.html' ,context)


#gives answers to some of the frequently asked questions
def about(request):
	about_list = About.objects.order_by('-time_added')[::-1]
	context = {'about_list' : about_list}
	return render (request, 'labs/about.html', context)

#lists all the posts
def posts(request,page_number):
	form = NameForm()
	page_number = int(page_number)
	page_number = validate_page_number(page_number, Post.objects.count(), posts_per_page)
	start_post = posts_per_page * (page_number-1)
	posts_list = Post.objects.order_by ('-pub_date') [start_post : start_post + posts_per_page]

	for post in posts_list:
		if len(post.post_text) > 60:
			post.post_text = post.post_text[0:300] + '...'
	users = User.objects.all()
	for x in users :
		x = x.get_full_name()
	next_page = page_number + 1
	prev_page = page_number - 1
	context = {'posts_list' : posts_list, 'users' : users, 'form' : form,
	 'next_page' : next_page, 'prev_page' : prev_page}
	return render (request, 'labs/posts.html', context)
	
#if u type posts in url, u are redirected to page with 5 most recent of them.
def redirect_posts (request):
	return HttpResponseRedirect('/posts/1')
	

#this page shows details of the selected post.
def details (request, post_number):
	post_number = int(post_number)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			my_comment = form.save(commit = False)
			if validate_text(my_comment.comment_text) and validate_text(my_comment.name_of_person):
				my_comment.verified = 1
			else:
				my_comment.verified = 0
			my_post = get_object_or_404(Post, id = post_number)
			my_comment.post = my_post
			my_comment.save()
			return HttpResponseRedirect('/posts/details/' + str(post_number) + '/')
	else :
		my_post = get_object_or_404(Post, id = post_number)
		form = CommentForm()
		comments = my_post.comment_set.order_by('-time_posted').filter(verified = 1)
		image_list = []
		if my_post.photo:
			image_list.append(my_post.photo)
		context = {'my_post' : my_post, 'form' : form, 'comments' : comments, 'image_list' : image_list}
		return render(request, 'labs/details.html', context)


#page to search for a name in posts, has many issues.
def get_name(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			obj = request.POST.get('search_for')         #request.GET['section']
			posts_list = Post.objects.filter(Q(post_title__contains = obj)
					| Q(post_text__contains = obj)).order_by('pub_date')
			return render(request, 'labs/name.html', {'posts_list' : posts_list, 'form' : form, 'obj' : obj})
	else:
		form = NameForm()
	
	return render(request, 'labs/name.html',{'form':form})

def volunteer(request):
	if request.method == 'POST':
		form = VolunteerForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = VolunteerForm()
	return render(request, 'labs/volunteer.html', {'form' : form})
	
def contact(request):
	context = {'contact_number' : contact_number, 'contact_id' : contact_id, 'address' : address}
	return render (request, 'labs/contact.html', context)
	
def videos(request):
	video_list = Video.objects.order_by('-time_uploaded')
	context = {'video_list' : video_list}
	return render(request, 'labs/video.html', context)
	
def gallery(request):
	images_list = Gallery.objects.all().order_by('-upload_time')
	return render(request, 'labs/gallery.html', {'images_list' : images_list})	
	
def home(request):
	return render (request, 'labs/home.html',{})	
	
