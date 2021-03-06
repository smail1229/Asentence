
class User(object):
    data = {
        "authenticated" : 0,   # the statu of the user, 1 is valid
        "email" : "",          # user's email
        "password" : "",       # user's password
        "username" : "",       # user's username
        "role" : 0 ,           # user's role, 0 for common
        "avatar" : "",         # the name of the image
        "weixin" : None,       # wechart identifier
        "weibo" : None,        # weibo identifier
        "qq" : None,           # qq identifier
        "collection" : [],     # my collections
        "create_time": None,   # register time
        "update_time": None,   # update time
        "isDelete" : False     # if true the user is deleted
    }
