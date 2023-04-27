from django.shortcuts import render
import requests

def index(request):
    url = "https://betfair-sportsbook.p.rapidapi.com/live-matches-by-sport"

    querystring = {"sport":"football","lang":"en"}

    headers = {
        "content-type": "application/octet-stream",
        "X-RapidAPI-Key": "45f8a18f79mshccd21ee1f0378ffp141a67jsn83a1a0cfa075",
        "X-RapidAPI-Host": "betfair-sportsbook.p.rapidapi.com"
    }

    req = requests.get(url, headers=headers, params=querystring)
    res = req.json()

    dic = {}
    for i, value in enumerate(res):
        dic[i] = value

    context = {
        "jogos": dic
    }

    return render(request, 'consumer/index.html', context)