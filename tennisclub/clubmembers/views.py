from django.http import HttpResponse
from django.template import loader
from .models import ClubMember


def main(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def clubmembers(request):
  members = ClubMember.objects.all().values()
  template = loader.get_template('clubmembers.html')
  context = {
    'members': members,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  members = ClubMember.objects.get(id=id)
  template = loader.get_template('memberdetails.html')
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