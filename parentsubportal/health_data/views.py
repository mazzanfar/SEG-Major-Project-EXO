from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import pdb


def scrape_webpage(request):
    print("im here")
    if request.method == 'GET':
        html = '''
        <form action="/your-name/" method="post">
            <label for="your_name">Your name: </label>
            <input id="your_name" type="text" name="your_name" value="{{ current_name }}">
            <input type="submit" value="OK">
        </form>
        '''
        return HttpResponse(html)