## GEOCODING API
### Installation:
Python version: 3.6 and above<br>
```sh
pip install -r requirements.txt
```

### Running the App:
Create an .env file with the following content.
```sh
FLASK_APP="main"
API_KEY="xxxxxxxxxxxxxxxxxx"
```
Then run 
```sh
flask run
```

### Testing output:
To test the output try the following curl command

```sh
curl --location --request POST 'http://localhost:5000/getAddressDetails' \
--header 'Content-Type: application/json' \
--data-raw '{
"address": "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
"output_format": "json"
}'
```

Response should be something like 
```json
{
    "address": "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
    "coordinates": {
        "lat": 12.9658286,
        "lng": 77.63948169999999
    }
}
```


