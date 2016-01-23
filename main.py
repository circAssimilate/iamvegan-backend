# App Engine
import webapp2
import os
# import jinja2
import random
from google.appengine.ext import ndb
# import datetime
import json
# import urllib

from google.appengine.ext import ndb

##
# Models
##

class UserInfo(ndb.Model):
    deviceID = ndb.StringProperty(default='')
    userID = ndb.StringProperty(default='')
    name = ndb.StringProperty(default='Veganite')
    primary = ndb.StringProperty(default='vegan')
    secondary = ndb.StringProperty(default='none')
    date = ndb.DateTimeProperty(auto_now_add=True)

##
# Functions
##

# Generates user IDs
def userIDreturn(deviceID, name):
    userID = ''.join(random.choice('123456789') for i in range(4))
    # userID = ''.join(random.choice('1234') for i in range(1))

    ID_query = UserInfo.query(UserInfo.deviceID == deviceID)
    userID_query = UserInfo.query(UserInfo.userID == userID)

    try:
        ID_query.fetch()[0]
    except:
        try:
            userID_query.fetch()[0]
        except:
            user = UserInfo(deviceID=deviceID,
                            userID=userID,
                            name=name,
                            primary="vegan")
            user.put()
            return {"userID" : user.userID, "date" : user.date, "name" : user.name, "primary" : user.primary, "secondary" : user.secondary}
        else:
            userIDreturn(deviceID, name)
    else:
        query = ID_query.fetch()[0]
        query.name = name
        query.put()

        return {"userID" : query.userID, "date" : query.date, "name" : query.name, "primary" : query.primary, "secondary" : query.secondary}
##
# Classes
##

class Main(webapp2.RequestHandler):
    def get(self):
        self.response.write("You shouldn't be here.")

class User(webapp2.RequestHandler):
    def get(self):
        deviceID = self.request.get('device_id')
        userID = self.request.get('user_id')
        name = self.request.get('name')
        if deviceID is not "" and name is not "":
            userID = userIDreturn(deviceID, name)
            self.response.out.write(userID)
        elif userID is not "" and deviceID is "" and name is "":
            user_query = UserInfo.query(UserInfo.userID == userID)
            try:
                user_query.fetch()[0]
            except:
                self.response.out.write("No such user")
            else:
                query = user_query.fetch()[0]
                self.response.out.write({"userID" : query.userID, "date" : query.date, "name" : query.name, "primary" : query.primary, "secondary" : query.secondary})
        else:
            self.response.out.write("Invalid Endpoint")


app = webapp2.WSGIApplication([
    ('/', Main),
    ('/user', User)
], debug=True)