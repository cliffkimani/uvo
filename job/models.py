from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from users.models import Writer, Affiliate, Client, Supaa

class Job(models.Model):
    STATUS_ARTICLE = (
        ('draft', 'Draft'),
        ('waiting', 'Draft'),
        ('allotted', 'Draft'),
        ('review', 'Draft'),
        ('fowarded', 'Draft'),
        ('complete', 'Draft'),
        ('revision', 'Draft'),
        ('dispute', 'Draft'),
    )
    STATUS_TASK = (
        ('editing', 'Editing'),
        ('scratch', 'Scratch'),
    )
    STATUS_SPACING = (
        ('double', 'Double'),
        ('single', 'Single'),
    )
    STATUS_DEAD = (
        ('3 hours', '3 hours'),
        ('6 hours', '6 hours'),
        ('12 hours', '12 hours'),
        ('24 hours', '24 hours'),
        ('48 hours', '48 hours'),
        ('3 days', '3 days'),
        ('4 days', '4 days'),
        ('5 days', '5 days'),
        ('7 days', '7 days'),
        ('10 days', '10 days'),
        ('14 days', '14 days'),
        ('20 days', '20 days'),
        ('30 days', '30 days'),
    )
    STATUS_FORMAT = (
        ('APA', 'APA'),
        ('MLA', 'MLA'),
        ('Turabian', 'Turabian'),
        ('Chicago', 'Chicago'),
        ('Harvard', 'Harvard'),
        ('Other', 'Other'),
    )
    STATUS_LEVEL = (
        ('highschool', 'highschool'),
        ('college', 'college'),
        ('university', 'university'),
        ('masters', 'masters'),
        ('PhD', 'PhD'),
    )
    STATUS_TYPE = (
        ('Admission Essay', 'Admission Essay'),
        ('Annotated Bibliography', 'Annotated Bibliography'),
        ('Argumentative Essay', 'Argumentative Essay'),
        ('Book Report', 'Book Report'),
        ('Assignment', 'Assignment'),
        ('Movie Review', 'Movie Review'),
        ('Case Study', 'Case Study'),
        ('Coursework', 'Coursework'),
        ('Dissertation', 'Dissertation'),
        ('Dissertation Chapter - Abstract', 'Dissertation Chapter - Abstract'),
        ('Dissertation Chapter - Abstract', 'Dissertation Chapter - Abstract'),
        ('Dissertation Chapter - Abstract', 'Dissertation Chapter - Abstract'),
        ('Dissertation Chapter - Introduction Chapter', 'Dissertation Chapter - Introduction Chapter'),
        ('Dissertation Chapter - Literature Review', 'Dissertation Chapter - Literature Review'),
        ('Dissertation Chapter - Methodology', 'Dissertation Chapter - Methodology'),
        ('Dissertation Chapter - Results', 'Dissertation Chapter - Results'),
        ('Dissertation Chapter - Discussion', 'Dissertation Chapter - Discussion'),
        ('Dissertation Chapter - Hypothesis', 'Dissertation Chapter - Hypothesis'),
        ('Dissertation Chapter - Conclusion Chapter', 'Dissertation Chapter - Conclusion Chapter'),
        ('Essay', 'Essay'),
        ('Formatting', 'Formatting'),
        ('Lab Report', 'Lab Report'),
        ('Math Problem', 'Math Problem'),
        ('Personal Statement', 'Personal Statement'),
        ('PowerPoint Presentation', 'PowerPoint Presentation'),
        ('Proofreading', 'Proofreading'),
        ('Paraphrasing', 'Paraphrasing'),
        ('Research Paper', 'Research Paper'),
        ('Research Proposal', 'Research Proposal'),
        ('Scholarship Essay', 'Scholarship Essay'),
        ('Speech', 'Speech'),
        ('Statistics Project', 'Statistics Project'),
        ('Term Paper', 'Term Paper'),
        ('Thesis', 'Thesis'),
        ('Thesis Proposal', 'Thesis Proposal'),
    )
    STATUS_FIELD = (
        ('Arts & Humanities', 'Arts & Humanities'),
        ('Social Sciences', 'Social Sciences'),
        ('Sciences', 'Sciences'),
        ('Information Technology', 'Information Technology'),
        ('Applied sciences', 'Applied sciences'),
        ('Economics', 'Economics'),
        ('Law', 'Law'),
        ('Other', 'Other'),
    )


    
    submitted = models.DateTimeField(auto_now_add =True)
    #job_files = models.ForeignKey(JobFile, related_name='Files')
    due_date = models.DateTimeField(auto_now_add =True)
    time_allowance = models.FloatField()
    status = models.CharField (max_length=10,
    	choices = STATUS_ARTICLE,
        default = 'draft')
    fee = models.FloatField()
    accuracy = models.IntegerField()
    rating = models.IntegerField()
    affiliate = models.ForeignKey(Affiliate) 
    discount = models.FloatField()
    customer = models.ForeignKey(Client)
    writer = models.ForeignKey(Writer)
    pages = models.IntegerField()
    citations = models.IntegerField()
    provide_references = models.BooleanField()
    affiliate = models.ForeignKey(Affiliate)
    discount = models.FloatField()
    words = models.IntegerField()
    title = models.CharField(max_length=100)
    prime = models.BooleanField()

    job_type= models.CharField (max_length=50,
    	choices = STATUS_TASK,
        default = 'draft')
    deadline = models.CharField (max_length=50,
    	choices = STATUS_DEAD,
        default = 'draft')
    formatting = models.CharField (max_length=50,
    	choices = STATUS_FORMAT,
        default = 'draft')
    service_type = models.CharField (max_length=50,
    	choices = STATUS_TYPE,
        default = 'draft')
    academic_level = models.CharField (max_length=50,
    	choices = STATUS_LEVEL,
        default = 'draft')
    discpline = models.CharField (max_length=50,
    	choices = STATUS_FIELD,
        default = 'draft')
    spacing = models.CharField (max_length=50,
    	choices = STATUS_SPACING,
        default = 'draft')
    top_assign = models.BooleanField()
    plag_report = models.BooleanField()
    slides = models.IntegerField()
    charts = models.IntegerField()
    paper_detail = models.TextField()
    additional_comment = models.CharField(max_length=10)

class JobFile(models.Model):
    upload = models.FileField()
    #job = models.ForeignKey(Job, default = Job.objects.get[1])
