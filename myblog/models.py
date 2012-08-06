from django.db import models

# Create your models here.

# blog_aside
class BlogAside(models.Model):
    name = models.CharField(max_length=50)
    sortNum = models.IntegerField(default=20)
    status = models.IntegerField()
    desc = models.CharField(max_length=200)

    def __unicode__(self):
        return r'the name is %s, and the desc is %s' % (self.name, self.desc)

# blog_molu
class BlogMolu(models.Model):
    asideId = models.ForeignKey('BlogAside')
    name = models.CharField(max_length=50)
    sortNum = models.IntegerField(default=20)
    status = models.IntegerField()
    desc = models.CharField(max_length=200)
    add_time = models.IntegerField()

# blog artcle
class BlogArtcle(models.Model):
    moluId = models.ForeignKey('BlogMolu')
    aisdeId = models.ForeignKey('BlogAside')
    label = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    add_time = models.IntegerField()
    Update_time = models.IntegerField()
    status = models.IntegerField()
    desc = models.CharField(max_length=200)

# blogTags
class BlogTags(models.Model):
    artcleId = models.ForeignKey('BlogArtcle')
    tags = models.CharField(max_length=20)
    sort_name = models.IntegerField()

