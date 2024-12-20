from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from django import forms

class MemberForm(forms.ModelForm):
  class Meta:
    model = Member
    fields = ['firstname', 'lastname', 'email', 'phone', 'joined_date']


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


def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()  # Save to DB
            return redirect('success_member_registration')  # Redirect to success page
    else:
        form = MemberForm()
    return render(request, 'create_member.html', {'form': form})


def delete_members(request):
    if request.method == 'POST':
        # Get the selected members for deletion
        member_ids = request.POST.getlist('members')  # List ID
        Member.objects.filter(id__in=member_ids).delete()  # Delete Members
        return redirect('members')  # Redirect to members site

    # Przy pierwszym wejściu wyświetl listę członków
    members = Member.objects.all()
    return render(request, 'delete_members.html', {'members': members})