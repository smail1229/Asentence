
class Entry(object):
    data = {
        "title" : "",             # entry's title
        "content" : "",           # entry's content
        "praise" : 0,             # entry's praise
        "author" : None,          # entry's author
        "cover" : -1,             # the name of the image
        "create_time" : None,     # utc time
        "update_time" : None,     # utc time
        "comments" : [],          # the comments
        "isDelete" : False       # if true the user is deleted
    }
