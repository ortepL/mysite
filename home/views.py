from django.shortcuts import render

# Create your views here.
def index(requst):
    return render(requst, 'home.html')

def contact(requst):
    return render(requst, 'basic.html', {'values': ['Звоните мне', '(067) xxx-xx-xx']})

def posts_list(requst):
    return render(requst, 'blog/index.html')