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


def select_member_to_edit(request):
    members = Member.objects.all()  # # Get all members
    return render(request, 'select_member_to_edit.html', {'members': members})


def edit_member(request, id):
    member = get_object_or_404(Member, id=id)  # Get user or return 404 in case member do not exist
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)  # Link Form with user
        if form.is_valid():
            form.save()  # Save to DB
            return redirect('select_member_to_edit')  # Return back to select member to edit page
    else:
        form = MemberForm(instance=member)  # Display form with member data

    return render(request, 'edit_member.html', {'form': form, 'member': member})


def delete_members(request):
    if request.method == 'POST':
        # Get the selected members for deletion
        member_ids = request.POST.getlist('members')  # List ID
        Member.objects.filter(id__in=member_ids).delete()  # Delete Members
        return redirect('members')  # Redirect to members site

    # At first visit, display the members list
    members = Member.objects.all()
    return render(request, 'delete_members.html', {'members': members})