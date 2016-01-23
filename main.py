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
    name = ndb.StringProperty(default='Vegan')
    primary = ndb.StringProperty(default='vegan')
    date = ndb.DateTimeProperty(auto_now_add=True)

##
# Functions
##

# Generates user IDs
def userIDreturn(deviceID, name):
    # userID = ''.join(random.choice('123456789') for i in range(4))
    # userID = ''.join(random.choice('1234') for i in range(1))

    deviceInfoQuery = UserInfo.query(UserInfo.deviceID == deviceID)

    try:
        deviceInfoQuery.fetch()[0]
    except:
        if name is "":
            name = "Vegan"
        user = UserInfo(deviceID=deviceID,
                            name=name)
        user.put()
        query_dict = {"deviceID" : user.deviceID,  "name" : user.name, "primary" : user.primary, "date" : user.date.strftime('%m/%d/%Y')}
        return query_dict
    else:
        query = deviceInfoQuery.fetch()[0]
        if name is not "":
            query.name = name
            query.put()
        user = query
        query_dict = {"deviceID" : user.deviceID,  "name" : user.name, "primary" : user.primary, "date" : user.date.strftime('%m/%d/%Y')}
        return query_dict

##
# Classes
##

class Main(webapp2.RequestHandler):
    def get(self):
        self.response.write("You shouldn't be here.")

class User(webapp2.RequestHandler):
    def get(self):
        deviceID = self.request.get('device_id')
        name = self.request.get('name')
        if deviceID is not "":
            try:
                user_query.fetch()[0]
            except:
                userID = userIDreturn(deviceID, name)
                self.response.headers['Content-Type'] = 'application/json'
                self.response.out.write(json.dumps(userID))
            else:
                query = user_query.fetch()[0]
                user = query
                query_dict = {"deviceID" : user.deviceID,  "name" : user.name, "primary" : user.primary, "date" : user.date.strftime('%m/%d/%Y')}
                self.response.headers['Content-Type'] = 'application/json'
                self.response.out.write(json.dumps(query_dict))
        else:
            self.response.out.write("Needs device ID url format.")


app = webapp2.WSGIApplication([
    ('/', Main),
    ('/user', User)
], debug=True)