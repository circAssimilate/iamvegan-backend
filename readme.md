# iamvegan-backend

Backend accepts this url format to store the device ID and name:

`https://sigma-kayak-119906.appspot.com/user?device_id=2342&name=Peter`

Here's the response:

```
{'date': datetime.datetime(2016, 1, 23, 10, 36, 56, 965910), 'secondary': u'none', 'userID': u'5824', 'name': u'Peter', 'primary': u'vegan'}
```

- It will create a unique, 4 digit ID if the device ID doesn't already exist, or return the existing information if it does
- If you push the same device ID with a different "name" parameter, it will update the record with the new name