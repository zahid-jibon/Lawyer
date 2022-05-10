import statistics
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import (
		UserProfile,
        Statistic,
        Choose,
        Appointment,
        Testimonial,
        Blog,
        Contact,
        UserContact,
        Schedule
	)
from .forms import (
    UserContactForm,
)

from django.views import generic


# Create your views here.
def home(request):
    profile = UserProfile.objects.filter(is_active=True)
    statistics = Statistic.objects.filter(is_active=True)
    choose = Choose.objects.filter(is_active=True)
    appointment = Appointment.objects.filter(is_active=True)
    testimonial = Testimonial.objects.filter(is_active=True)
    blog = Blog.objects.filter(is_active=True)


    context = {'profile': profile, 'statistics': statistics, 'choose': choose, 'appointment': appointment, 'testimonial': testimonial, 'blog': blog}
    

    return render(request, 'portfolio/home.html', context)


def blog(request):
    blog = Blog.objects.filter(is_active=True)
    context = {'blog': blog}
    return render(request, 'portfolio/blog.html', context)


def blog_details(request, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)
	return render(request, "portfolio/blog-detail.html", {"id": blog})



def schedule(request):
    schedule = Schedule.objects.filter(is_active=True)
    context = {'schedule': schedule}

    return render(request, 'portfolio/schedule.html', context)



def contact(request):
    contact = Contact.objects.filter(is_active=True)

    context = {'contact': contact}

    return render(request, 'portfolio/contact.html', context)


class ContactView(generic.FormView):
	template_name = "portfolio/contact.html"
	form_class = UserContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)