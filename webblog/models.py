#coding=utf-8
from django.db import models
import re
from django.core.exceptions import ValidationError

# Create your models here.

class Category(models.Model):
    """
    分类信息表
    """
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=100,blank=True)
    create_time = models.DateTimeField(auto_now=True)
    category_pv = models.IntegerField(default=0, verbose_name="点击次数")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-category_pv']

class Blog(models.Model):
    """
    博客主表
    """
    blog_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,db_column="category_id")
    title = models.CharField(max_length=20, db_index=True, unique=True)
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now=True,db_index=True)
    blog_pv = models.IntegerField(default=0)
    is_closed = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'blog'
        ordering = ['-pub_time','-blog_pv']

class Tag(models.Model):
    """
    标签表
    """
    tag_id = models.AutoField(primary_key=True) 
    blog = models.ManyToManyField(Blog)
    tag_name = models.CharField(max_length=20, db_index=True,unique=True)
    desc = models.CharField(max_length=50)
    create_time = models.DateField(auto_now=True)
    tag_pv = models.IntegerField(default=0, verbose_name="点击量")
    
    def __unicode__(self):
        return self.tag_name

    class Meta:
        #db_table = 'tag'
        ordering = ['-tag_pv',"-create_time"]


class Comment(models.Model):
    """
    评论表
    """
    COMMENT_LEVEL_CHOICES = (
        (0, '一级评论'),
        (1, '二级评论'),
    )
    comment_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=10)
    author_email = models.EmailField()
    content = models.TextField()
    is_close = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog)
    comment_up = models.IntegerField(default=0,verbose_name="加分次数")
    
    def __unicode__(self):
        return 'the %s has say: %s' % (self.author_name, self.content[:10]+'..')

    class Meta:
        ordering = ['-comment_up']

    
class About(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    website = models.URLField(blank=True)
    content = models.TextField()
    
    def __unicode__(self):
        return '%s with email: %s send this: %s' % (self.name, self.email, self.content)

def validate_qq(value):
    reqq = re.compile("[0-9]{6,10}")
    if not reqq.match(value):
        raise ValidationError(u'%s is not a qq contact' % value)
        
class Contact(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    website = models.URLField(blank=True,null=True)
    qq = models.CharField(max_length=12, blank=True, validators=[validate_qq,])    
    if_accept_email = models.BooleanField(default=False)
    content = models.TextField()
    
    def __unicode__(self):
        return '%(name)s with email: %(email)s' % ({'name':self.name, 'email':self.email})
    
