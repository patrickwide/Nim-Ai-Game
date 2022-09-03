from posixpath import split
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from django.urls import reverse
from .nim import train, play, Nim
import random
import json
import ast
# Create your views here.
ai = train(10055)


def index(req):
    return render(req, 'app/index.html')

@csrf_exempt
def help(req):
    return render(req, 'app/help.html', {
        "message":"Some message will go here"
    })

@csrf_exempt
def game(req):
    if req.method == "POST":
        a = str(req.body.decode("utf-8", "strict"))
        print(a)
        b = a.split(',')
        gameBoard = []
        for i in b:
            gamePile = int(i)
            gameBoard.append(gamePile)
        pile, count = ai.choose_action(gameBoard, epsilon=False)

        print(f"pile : {pile}, count : {count}")
        response = JsonResponse({'pile': f"{pile}", 'count': f"{count}"})
        return response

    return render(req, 'app/game.html', {
        "message": "Keep calm and game on."
    })

@csrf_exempt
def api(req):
    if req.method == 'POST':
        input = req.body.decode("utf-8", "strict")
        input = json.JSONDecoder().decode(input)
        gameBoard = input['state']
        gameBoard = ast.literal_eval(gameBoard)
        pile, count = ai.choose_action(gameBoard, epsilon=False)
        print(f"pile : {pile}, count : {count}")
        return JsonResponse({'pile': f"{pile}", 'count': f"{count}"})
    else:
        return HttpResponse("Hello world")

