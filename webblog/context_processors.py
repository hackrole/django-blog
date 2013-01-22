from webblog.models import Tag,Category,Comment,Blog
def sidebar(request):
    """
    add the sidebar data to the template
    """
    tags = Tag.objects.all()
    cate = Category.objects.all()
    hotcomment = Comment.objects.filter(is_close=False)[0:5]
    
    mostcomment = Blog.objects.raw(
        'select blog_id,count(c.comment_id) as count from blog as b left join webblog_comment as c on b.blog_id=c.blog_id_id group by blog_id order by blog_id limit 10'
        )
    recentBlog = Blog.objects.order_by('-pub_time')[0:5]
 
    return {
        'tags': tags,
        'cate': cate,
        'hotcomment': hotcomment,
        'mostcomment': mostcomment,
        'recentBlog': recentBlog,
        }
     
