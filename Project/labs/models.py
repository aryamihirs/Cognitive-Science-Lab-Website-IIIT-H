from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.

class About(models.Model):
	question = models.CharField(max_length = 500)
	answer = models.TextField(max_length = 1000)
	time_added = models.DateTimeField('time added', default = timezone.now)

class Post(models.Model):
	professor_name = models.ForeignKey(User)
	post_title = models.CharField(max_length=500, unique=True, default='Post Title')
	post_text = models.TextField(max_length = 5000)
	pub_date = models.DateTimeField('date published', default=timezone.now)
	photo = models.ImageField(upload_to = 'images/posts', blank=True)	
	def __str__(self):
		return self.post_text
    	
class Comment(models.Model):
	post = models.ForeignKey(Post)
	comment_text = models.TextField(max_length=5000, help_text = 'enter your comment in no more than 500 words.')
	name_of_person = models.CharField(max_length = 60, default = 'Anonymous', blank = True)
	time_posted = models.DateTimeField('date posted', default = timezone.now)
	verified = models.BooleanField(default = 0)
	
	def __str__(self):
		return self.comment_text



class Volunteer(models.Model):
	gender_list = [('M', 'Male'), ('F', 'Female')]
	occupation_list = [('Student', 'Student'), ('Service', 'Service Man'), ('Business', 'Business Man'), 
						('Doctor', 'Doctor'),('Teacher', 'Teacher'), ('Unemployed', 'Unemployed')]
	lab_list = [('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')]
	transport_list = [('Public', 'Public Transport'), ('Private Vehicle', 'Private Vehicle'), ('Bicycle', 'Bicycle'),
						('Walk', 'Walk'), ('Others', 'Others')]
	hands = [('Left', 'Left'), ('Right', 'Right')]
	
	Name = models.CharField(max_length = 60)
	Mail_id = models.EmailField (max_length = 60)
	Mobile_number = models.CharField(max_length = 15)
	Date_of_birth = models.DateField()
	Gender = models.CharField(max_length = 20, choices = gender_list, default = 'M')
	Occupation_status = models.CharField(max_length = 50, choices = occupation_list, default = 'Student')
	Lab_you_want_to_contribute_in = models.CharField(max_length = 50, choices = lab_list, default = 'a')
	How_do_you_plan_to_contribute = models.TextField(max_length = 6000)
	Transportation_plans = models.CharField(max_length = 50, choices = transport_list, default = 'Public')
	Handedness = models.CharField(max_length = 50, choices = hands, default = 'Right')
	Nationality = models.CharField(max_length = 20)
	Time_applied = models.DateTimeField('date posted', default = timezone.now)
	reviewed = models.BooleanField(default = 0)
	
class Video(models.Model):
	description = models.CharField(max_length = 200)
	video_id = models.CharField(max_length = 100, help_text = "copy the video id given in the url. write xyz if v='xyz' in the video url.")
	uploaded_by = models.ForeignKey(User)
	time_uploaded = models.DateTimeField(default = timezone.now)

class Gallery(models.Model):
	my_image = models.ImageField(upload_to = 'images/gallery')
	tag_line = models.CharField(max_length = 1000)
	upload_time = models.DateTimeField(default = timezone.now)
		
class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['name_of_person', 'comment_text']

class VolunteerForm(ModelForm):
	class Meta:
		model = Volunteer
		fields = ['Name', 'Mail_id', 'Mobile_number', 'Date_of_birth', 'Gender', 'Occupation_status',
				'Lab_you_want_to_contribute_in', 'How_do_you_plan_to_contribute', 'Transportation_plans',
				'Handedness', 'Nationality']
