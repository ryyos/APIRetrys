<h1 align="center" >Hello, I'm Ryo 👋</h1>

<h1 align="center" >Welcome To ApiRetrys 🔥</h1>

![Version](https://img.shields.io/badge/version-0.0.4-green.svg?cacheSeconds=2592000)

> Are you annoyed because your request has an error due to internet problems? I think this could be the answer

## Feature ✨

- automatically repeats if the request times out
- The number of repetitions and waiting time can be adjusted and default values ​​are provided
- maintain flexibility by returning all responses received
- provides logs to make monitoring easier, which can be turned on or not
- provides all the methods in the request
- can handle to may requests
- You can handle forbidden (403) by refreshing the session with a request to the main URL

## Tech 💻

- [requests](https://docs.python-requests.org/) is an easy-to-use Python library for interacting with APIs and making HTTP requests

## Requirement ⚙️

- [Python](https://www.python.org/) v3.11.6+
- [requests](https://docs.python-requests.org/) 2.31.0+

## Installation 🛠️

```sh
pip install ApiRetrys
```

## How To Usage 🤔

Basic use

```python
from ApiRetrys import ApiRetry

api = ApiRetry(show_logs=True)
response = api.get(url='https://github.com/')

# or you can define data types

from ApiRetrys import ApiRetry
from requests import Response

api = ApiRetry(show_logs=True)
response: Response = api.get(url='https://github.com/',)

# or you want to manually set the max_retries
# by defaulth (max_retries) is 5
response: Response = api.get(url='https://github.com/', max_retries=10)
```

#### if you set param (show_logs=True) then a log will come out like this

<br>
<div style="text-align: center;">
  <img src="https://raw.githubusercontent.com/ryyos/ryyos/main/images/ApiRetrys/logs_true.png"> 
</div>
<br>

### If the error exceeds max_retries then it will raise the exception MaxRetryExceptions

<br>
<div style="text-align: center;">
  <img src="https://raw.githubusercontent.com/ryyos/ryyos/main/images/ApiRetrys/max_retires.png"> 
</div>
<br>

### With other parameters

```python
from ApiRetrys import ApiRetry
from requests import Response

headers = {
   "PUBLIC-CSRF-TOKEN": '7giS6UPv3Rf2l9fclp2wFzCEI',
   "User-Agent": user_agent.random
}

payload = {
    "query":"anime",
    "page":1,
    "per_page":50,
    "sorting":"likes",
    "pro_first":"1",
    "filters":[],
    "additional_fields":[]
    }

cookies = {
    'PRIVATE-CSRF-TOKEN': '8Mc45%2BAa3Vd',
    'cf_clearance': 'rpQn91kojLw_ZCzrgjP',
    '__stripe_mid': '0adecf01-7471-434e-aa12-6c2d33cbb216fd19aa',
    'g_state': '{"i_p":1702902016560,"i_l":1}',
    'visitor-uuid': 'fbf18513-e803-',
    '__cf_bm': '_ukyfnf1.He..wDhIxF',
    '__stripe_sid': 'c7956d65-b70f-4e',
    'referrer-host': 'www.google.com'
}

api = ApiRetry(show_logs=False)
response: Response = api.post(url='https://github.com/', data=payload, cookies=cookies)
```

### examples of more complex usage as well as the use of handlers for many requests and forbidden

```python

from ApiRetrys import ApiRetry
from requests import Response

class Main:
    def __init__(self) -> None:

        self.api = ApiRetry(

            # parameters to display logs or not
            show_logs=True,

            # parameter whether you want to use the default header,
            # but only contain the user agent
            defaulth_headers=True,

            # param to handle responses 403 and 429,
            # if false it will be returned even though the responses are 403 and 429
            handle_forbidden=True,

            # whatever response you want to handle
            # This is the default value, if it is not entered there is no problem
            codes_handler=[403, 429],

            # URL to refresh the session if you get a 403 response
            # (it is recommended to use the main URL of the destination website)
            redirect_url='https://github.com/')
        ...


    def execute(self, url: str):
        response: Response = self.api.get(url)

        print(response)
        ...

if __name__ == '__main__':
    main = Main()
    main.execute('https://github.com/ryyos/ApiRetrys')

```

### explanation

when you try to make a request to the url https://github.com/ryyos/ApiRetrys
but you get a 403 response because your session does not have CSRF-TOKEN, or because there are too many requests, then the code will handle it by trying to refresh the session by making requests to the main URL in the redirect_url parameter

## 🚀Structure

```
│   LICENSE
│   README.md
│   setup.py
│
└───ApiRetrys
        ApiRetrys.py
        Logs.py
        MaxRetryExceptions.py
        __init__.py
```

## Author

👤 **Rio Dwi Saputra**

- Twitter: [@ryyo_cs](https://twitter.com/ryyo_cs)
- Github: [@ryyos](https://github.com/ryyos)
- Instagram: [@ryyo.cs](https://www.instagram.com/ryyo.cs/)
- LinkedIn: [@rio-dwi-saputra-23560b287](https://www.linkedin.com/in/rio-dwi-saputra-23560b287/)

<a href="https://www.linkedin.com/in/rio-dwi-saputra-23560b287/">
  <img align="left" alt="Ryo's LinkedIn" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a href="https://www.instagram.com/ryyo.cs/">
  <img align="left" alt="Ryo's Instagram" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />
</a>
