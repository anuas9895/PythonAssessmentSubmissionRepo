from django.shortcuts import render,redirect
from test_app.models import Repository
from django.http import HttpResponse
from github import Github
from pprint import pprint
import requests
from django.shortcuts import render
from github import Auth


#home page
def home(request):
    return render(request, "index.html")



def search_repo(request):

    g = Github()
    if request.method == 'POST':
        a = request.POST["name1"]
        for repo in g.search_repositories(a):
            # Save the search results into the model
                m=Repository(
                    full_name=repo.full_name,
                    description=repo.description,
                    created_at=repo.created_at,
                    stargazers_count=repo.stargazers_count,
                    forks=repo.forks_count
                )
                m.save()
        a = Repository.objects.all()

        return render(request, 'search_results.html', {'repo': a})



