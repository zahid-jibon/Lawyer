from datetime import date
from email import message
from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class UserProfile(models.Model):

    class Meta:
        verbose_name = 'User Profile'
    
    name = models.CharField(max_length=20, blank=True, null=True)
    tag_line = models.CharField(max_length=200, blank=True, null=True)
    btn_txt = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="profile_images")
    image_caption = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.name} {self.tag_line}'

    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return 



class Statistic(models.Model):
    class Meta:
        verbose_name_plural = 'Statistics'
        verbose_name = 'Statistic'


    number_one = models.IntegerField(default=0, verbose_name='Enter Number For Field One')
    field_one = models.CharField(max_length=50, blank=True, null=True, default="Total Case", verbose_name='Name of Field One')
    number_two = models.IntegerField(default=0, verbose_name='Enter Number For Field Two')
    field_two = models.CharField(max_length=50, blank=True, null=True,default="Active Case", verbose_name='Name of Field Two')
    number_three = models.IntegerField(default=0, verbose_name='Enter Number For Field Three')
    field_three = models.CharField(max_length=50, blank=True, null=True, default="Successful", verbose_name='Name of Field Three')
    number_four = models.IntegerField(default=0, verbose_name='Enter Number For Field Four')
    field_four = models.CharField(max_length=50, blank=True, null=True, default="Award Won", verbose_name='Name of Field Four')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.number_one} {self.number_two} {self.number_three} {self.number_four}'



class Choose(models.Model):
    class Meta:
        verbose_name_plural = 'Choose Us'
        verbose_name = 'Choose Us'

    heading = models.CharField(max_length=50, blank=True, null=True, verbose_name='Write a Heading')
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name='Write a Description')
    class_name = models.CharField(max_length=50, blank=True, null=True, default="icon-box-clr-1", verbose_name='Write a Class Name for Change Card Color')
    class_name_icon = models.CharField(max_length=50, blank=True, null=True, default="fas fa-user-friends", verbose_name='Write a Class Name for Change Icon')
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.heading} {self.description}'



class Appointment(models.Model):

    class Meta:
        verbose_name_plural = 'Appointments'
        verbose_name = 'Appointment'


    image = models.ImageField(blank=True, null=True, upload_to="appointment_images", verbose_name='Upload an Image for Appointment Section') 
    heading_one = models.CharField(max_length=50, blank=True, null=True, default="Get a Appointment Today!", verbose_name='Write a Heading For First Card')
    description_one = models.CharField(max_length=200, blank=True, null=True, verbose_name='Write a Description For First Card')
    heading_two = models.CharField(max_length=50, blank=True, null=True, default="We Are The Best Choice For Your Case", verbose_name='Write a Heading For Second Card')
    description_two = models.CharField(max_length=200, blank=True, null=True, verbose_name='Write a Description For Second Card')
    number = models.IntegerField(default=0, verbose_name='Enter Number For Appointment')
    check_point_one = models.CharField(max_length=50, blank=True, null=True, verbose_name='Write a First Check Point')
    check_point_two = models.CharField(max_length=50, blank=True, null=True, verbose_name='Write a Second Check Point')
    check_point_three = models.CharField(max_length=50, blank=True, null=True, verbose_name='Write a Third Check Point')
    btn_text = models.CharField(max_length=15, blank=True, null=True, default="Get Appointment", verbose_name='Write a Button Text')
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.heading_one} {self.description_one}'

    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



    
class Testimonial(models.Model):

    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'

    
    image = models.ImageField(blank=True, null=True, upload_to="testimonial_images", verbose_name='Upload an Image of Client')
    quote = models.CharField(max_length=200, blank=True, null=True, verbose_name='Write a Quote/Good Words of Client')
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Write Name of Client')
    class_name = models.CharField(max_length=50, blank=True, null=True, default="anim1", verbose_name='Write a Class Name for Change Card Color')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.quote} {self.name}'


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Blog(models.Model):
    
    class Meta:
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'
        ordering = ["date"]

    image = models.ImageField(blank=True, null=True, upload_to="blog_images", verbose_name='Upload an Image of Blog')
    heading = models.CharField(max_length=50, blank=True, null=True, verbose_name='Write a Heading of Blog')
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name='Write a Description of Blog')
    admin_image = models.ImageField(blank=True, null=True, upload_to="admin_images", verbose_name='Upload an Image of Admin')
    admin_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Write Name of Admin')
    date = models.DateTimeField(blank=True, null=True, verbose_name='Write Date of Blog')
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.heading} {self.description}'

    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def admin_imageURL(self):
        try:
            url = self.admin_image.url
        except:
            url = ''
        return url




class Contact(models.Model):

    class Meta:
        verbose_name_plural = 'Contacts Info'
        verbose_name = "Contact Info"

    
    address = models.CharField(max_length=50, blank=True, null=True, default="Dhaka, Bangladesh", verbose_name='Set An Address')
    call = models.CharField(max_length=50, blank=True, null=True, verbose_name='Set Phone Number')
    email = models.CharField(max_length=50, blank=True, null=True, verbose_name='Set Email')
    support = models.CharField(max_length=50, blank=True, null=True, verbose_name='Set Support Email')
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.address} {self.call} {self.email} {self.support}'




class UserContact(models.Model):
    
    class Meta:
        verbose_name_plural = 'User Contact Info'
        verbose_name = 'User Contact Info'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(verbose_name="Phone",max_length=100)
    subject = models.CharField(verbose_name="Subject",max_length=100)
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'




class Schedule(models.Model):
    class Meta:
        verbose_name_plural = 'Set Available Time For Appointments'
        verbose_name = 'Set Available Time For Appointment'

    s_time = models.TimeField(verbose_name="Start Time")
    e_time = models.TimeField(verbose_name="End Time")
    date = models.DateField(verbose_name="Date")
    day = models.CharField(verbose_name="Day",max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.s_time} {self.e_time} {self.date} {self.day}'

    

