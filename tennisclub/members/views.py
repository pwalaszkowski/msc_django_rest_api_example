from django.http import HttpResponse
from django.template import loader
from .models import Member


def main(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def member(request):
  members = Member.objects.all().values()
  template = loader.get_template('members.html')
  context = {
    'members': members,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  members = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'members': members,
  }
  return HttpResponse(template.render(context, request))


def testing(request):
  template = loader.get_template('testing.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))