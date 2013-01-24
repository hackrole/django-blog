#!/usr/bin/python2.7
#coding=utf-8

from django.core.paginator import Paginator

class PageHelp:
    """
    from a Pagintor object output a html-page string 
    """

    def __init__(self, p):
        """ 
        init
        """
        if isinstance(p, Paginator):
            self.p = p
        else:
            raise TypeError("not a Pagintor object")
        # self.class = class
   
        

    def normalPage(self, current_page = None, max_page=10, first_and_end=True, pre_and_next=True, if_goto=False):
        """
        current_page: if None, not active current page, else active the given page num, like current_page = 1.
        max_page: the max show page nums, the other will be show by ...
        first_and_end: if show the first and end button.
        pre_and_next: if show pre and next button.
        if_goto: if show the goto button.
        """
        
        p = self.p
        output = []
        for page in p.page_range:
            if page >= max_page:
                s = '<a href="?page=%s" class="current">%s</a>...' % (page, page)
                output.append(s)
                break;
            if current_page is not None and page == currrent_page:
                s = '<a href="?page=%s" class="current">%s</a>' % (page, page)
            else:
                s= '<a href="?page=%s" class="current">%s</a>' % (page, page)

            output.append(s)

        if pre_and_next:
            s1 = '<a href="?page=%s" class="pre">%s</a>' % (page, "上一页")
            s2 = 'a href="?page=%s" class="next">%s</a>' % (page, "下一页")
            output.insert(0, s1)
            output.append(s2)
        if first_and_end:
            s1 = '<a href="?page=%s" class="first">%s</a>' % (page, "首页")
            s2 = '<a href="?page=%s" class="end">%s</a>' % (page, "末页")
            output.insert(0, s1)
            output.append(s2)
        # if if_goto:
        #     s = '
        output = ''.join(output)
        return output
        
