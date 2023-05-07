from django.shortcuts import render
from django.http import HttpResponse
# from transformers import pipeline
import openai

from django.http import JsonResponse
# Create your views here.
def index(request):
    return HttpResponse("this is the first dajngo that i build by my own")

def detail(request, question_id):
    return HttpResponse("this is the first detail view %s" %question_id)
def results(request, question_id):
    return HttpResponse("this is also the display for the result by the question id %s" %question_id)

def vote(request, question_id):
    return HttpResponse("this is also for the vote display with the question id %s" %question_id)
def display(request):
    return render(request, 'polls/chat.html')

def chat(request):
    message = request.POST.get("message")
    # generator = pipeline("text-generation")
    # new_message=generator(message)
    response = get_completion(message)    
    return JsonResponse(response, safe=False)
    
def get_completion(prompt, model="gpt-3.5-turbo"):
    openai.api_key = "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"
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]