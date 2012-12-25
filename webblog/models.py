#coding=utf-8
from django.db import models

# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now=True)
    category_rate = models.SmallIntegerField(verbose_name="排名")

    def __unicode__(self):
        return self.name

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category)
    title = models.CharField(max_length=20, db_index=True, unique=True)
    desc = models.CharField(max_length=150)
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now=True,db_index=True)
    update_time = models.DateTimeField()    
    is_pub = models.BooleanField()
    is_close = models.BooleanField()
    is_visiable = models.BooleanField()
    
    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'blog'
        ordering = ['-pub_time']

class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True) 
    tag_name = models.CharField(max_length=20, db_index=True,unique=True)
    desc = models.CharField(max_length=50)
    create_time = models.DateField(auto_now=True)
    tag_rate = models.SmallIntegerField()
    
    def __unicode__(self):
        return self.tag_name

class Blog_Tag(models.Model):
    relation_id = models.AutoField(primary_key=True)
    blog_id = models.ForeignKey(Blog)
    tag_id = models.ForeignKey(Tag)
    
    def __unicode__(self):
        s = "the %d relate the blog %d and the Tag %d" % (self.relation_id, self.blog_id.blog_id, self.tag_id.tag_id)
        return s

class Comment(models.Model):
    COMMENT_LEVEL_CHOICES = (
        (0, '一级评论'),
        (1, '二级评论'),
    )
    comment_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=10)
    author_email = models.EmailField()
    content = models.TextField()
    is_close = models.BooleanField()
    is_discard = models.BooleanField()
    comment_level = models.SmallIntegerField(choices=COMMENT_LEVEL_CHOICES)
    parent_id = models.ForeignKey('self', blank=True, null=True)
    blog_id = models.ForeignKey(Blog, blank=True, null=True)
    
    def __unicode__(self):
        return 'the %s has say: %s' % (self.author_name, self.content[:10]+'..')

    
