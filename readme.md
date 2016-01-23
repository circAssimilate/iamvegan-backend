# iamvegan-backend

###Example of creating or updating a user

`https://sigma-kayak-119906.appspot.com/user?device_id=67EADC65-1C39-42CA-95CC-7EF8692B68C7&name=John`

###Example of returning user info

`https://sigma-kayak-119906.appspot.com/user?device_id=67EADC65-1C39-42CA-95CC-7EF8692B68C7`

- It will store the unique device ID if the device ID doesn't already exist. If `name` is not present, the name defaults to "Vegan". If it does exist, it will return the existing information
- If you push the same device ID with a `name` parameter, it will update the record with the value of `name`

###Response format

```
{
    "date": "01/23/2016",
    "primary": "vegan",
    "deviceID": "67EADC65-1C39-42CA-95CC-7EF8692B68C7",
    "name": "John"
}
```