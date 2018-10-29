from django.shortcuts import render

posts = [
    {
        'author': 'MartinezMangement',
        'title': 'Blog Post 1 ',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'MartinezMangement',
        'title': 'Blog Post 2 ',
        'content': 'Second post content',
        'date_posted': 'August 30, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
