<h1 align="center" >Hello 👋, I'm Ryo</h1>
<h3 align="center" >An independent backend developer</h3>

<h1 align="center" >Welcome To APIRetry🔥</h1>

> I created this library to make it easier for developers to handle time out requests that may be caused by network difficulties

## Feature

- automatically repeats if the request times out
- The number of repetitions and waiting time can be adjusted and default values ​​are provided
- maintain flexibility by returning all responses received
- provides logs to make monitoring easier, which can be turned on or not
- provides all the methods in the request

## Tech

- [requests](https://docs.python-requests.org/) is an easy-to-use Python library for interacting with APIs and making HTTP requests

## Requirement

- [Python](https://www.python.org/) v3.11.6+
- [requests](https://docs.python-requests.org/) 2.31.0+

## Installation

```sh
pip install APIRetry
```

## Example Usage

Basic use

```python
from ApiRetrys import ApiRetry

api = ApiRetry(show_logs=False)
response = api.get(url='https://github.com/')

# or you can define data types

from ApiRetrys import ApiRetry
from requests import Response

api = ApiRetry(show_logs=False)
response: Response = api.get(url='https://github.com/')

```

With with other parameters

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

## 🚀Structure

```
│   LICENSE
│   README.md
│   setup.py
│
└───APIRetry
    │   ApiRetrys.py
    │   __init__.py
    │
    ├───Exceptions
    │       MaxRetryExceptions.py
    │
    └───utils
            Logs.py
```

## Author

👤 **Rio Dwi Saputra**

- Twitter: [@ryosora12](https://twitter.com/ryosora12)
- Github: [@ryosoraa](https://github.com/ryosoraa)
- LinkedIn: [@rio-dwi-saputra-23560b287](https://www.linkedin.com/in/rio-dwi-saputra-23560b287/)

<a href="https://www.linkedin.com/in/ryosora/">
  <img align="left" alt="Ryo's LinkedIn" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a href="https://www.instagram.com/ryosoraaa/">
  <img align="left" alt="Ryo's Instagram" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />
</a>
