from ApiRetrys import ApiRetry
from requests import Response
api = ApiRetry(show_logs=True)
res: Response = api.get(url='https://www.programiz.com/')
print(res)

