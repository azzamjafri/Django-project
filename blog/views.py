from django.shortcuts import render

post = [
	{
		'author': 'Azzam jafri',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'August 27 , 2k19'
	},
	{
		'author': 'Randon Person',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'March 27 , 2k19'
	}
]

# Create your views here.

def home(request):
	context = {
		'posts': post
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})