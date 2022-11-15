from django.views.generic import View, ListView
from django.shortcuts import render, redirect

from myapp.forms import ContactForm
from myapp.models import Student

class StudentDetails(View):
    
    def get(self, request):
        form = ContactForm() # Unbound Instantiation
        return render(request, "myapp/student.html", {"form": form})
    
    def post(self, request):
        form = ContactForm(request.POST, request.FILES) 
        if form.is_valid():
            instance = form.save()
            return render(request, "myapp/record.html", {"data": instance})
        else:
            return render(request, "myapp/student.html", {"form": form})

class StudentListView(ListView):
    template_name = "myapp/detail-list.html"
    context_object_name = "records"
    queryset = Student.objects.all()

class StudentUpdateView(View):

    def get(self, request, id):
        form = ContactForm(instance=Student.objects.get(id=id))
        return render(request, "myapp/student.html", {"form": form})
    
    def post(self, request, id):
        form = ContactForm(request.POST, request.FILES, instance=Student.objects.get(id=id))
        if form.is_valid():
            instance = form.save()
            return redirect("list-student")
        else:
            return render(request, "myapp/student.html", {"form": form})
