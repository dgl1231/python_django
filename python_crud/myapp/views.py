from django.shortcuts import render, HttpResponse
import random
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

nextID = 4
topics = [
    {'id': 1, 'title': 'routing', 'body': 'routing'},
    {'id': 2, 'title': 'view', 'body': 'view'},
    {'id': 3, 'title': 'Model', 'body': 'Model'},
]


def HTMLTemplate(articleTag, id=None):
    global topics
    ol = ''
    contextUI = ''
    if id != None:
        contextUI = f'''
        <li>
            <form action="/delete/" method="POST">
                <input type="hidden" name="id" value={id}>
                <input type="submit" value="delete">
            </form>
        </li>
        <li>
            <a href="/update/{id}">update</a>
        </li>
        '''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'

    return f'''
        <html>
            <body>
                <h1><a href="/">Django</a></h1>
                <ul>
                    {ol}
                </ul>
                <ul>
                    <li><a href="/create/">create</a></li>
                    {contextUI}
                </ul>
                {articleTag}
            </body>
        <html>
    '''


def index(request):
    article = '''
    <h2>welcome</h2>
    Hello,Django
    '''
    return HttpResponse(HTMLTemplate(article))


def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article, id))


@csrf_exempt
def create(request):
    global nextID
    if request.method == 'GET':
        article = '''
        <form action="/create/" method="POST">
            <p><input type="text" name="title" placeholder="title"/></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"/></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {'id': nextID, 'title': title, 'body': body}
        topics.append(newTopic)
        url = '/read/'+str(nextID)
        nextID = nextID + 1
        return redirect(url)


@csrf_exempt
def update(request, id):
    global topics

    if request.method == 'GET':
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {
                    'title': topic['title'], 'body': topic['body']}
        article = f'''
        <form action="/update/{id}/" method="POST">
            <p><input type="text" name="title" placeholder="title" value={selectedTopic['title']} /></p>
            <p><textarea name="body" placeholder="body">{selectedTopic['body']}</textarea></p>
            <p><input type="submit"/></p>
        </form>'''
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}')


@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')
