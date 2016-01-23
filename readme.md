# iamvegan-backend

###Example of creating or updating a user

Only accepts a url with these paramters to store the device ID or update the name:

`https://sigma-kayak-119906.appspot.com/user?device_id=2342&name=Peter`

- It will create a unique, 4 digit ID if the device ID doesn't already exist, or return the existing information if it does
- If you push the same device ID with a different "name" parameter, it will update the record with the new name

###Example of returning user info via user ID

Only accepts a url with this paramter to return the user information:

https://sigma-kayak-119906.appspot.com/user?user_id=5824

###Response format

```
{
    "date": "01/23/2016",
    "secondary": "none",
    "userID": "5824",
    "name": "Peter",
    "primary": "vegan"
}
```