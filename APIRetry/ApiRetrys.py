import requests
from requests import Response
from typing import Union
from time import sleep
from icecream import ic
from LogsOptions import LogsOptions
from utils.Logs import logger

class ApiRetry:
    def __init__(self, options: LogsOptions = None) -> None:
        self.show_logs = options.show_log
        self.path = options.path

        print(options)
        pass

    def get(self, url: str, headers: dict, max_retries: int = 5, retry_interval: Union[int, float] = 0.2):
        for retry in range(max_retries):
            try:
                response = requests.get(url=url, headers=headers)

                if self.show_logs and response.status_code == 200:
                    logger.info(f"method: GET")
                    logger.info(f"status code: {response.status_code}")
                    logger.info(f"retry to: {retry}")

                elif self.show_logs and response.status_code != 200:
                    logger.warning(f"method: GET")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry}")


                return response
            except Exception as err:
                logger.error(f'message: {err}')
                logger.warning(f'try the request again')
                
            sleep(retry_interval)
            retry_interval+= 0.2
        
        raise
        

    def post(self, url: str, headers: dict, max_retries: int = 5, retry_interval: Union[int, float] = 0.2, payload: any = None):
        for retry in range(max_retries):
            try:
                response = requests.post(url=url, headers=headers, data=payload)

                if self.show_logs and response.status_code == 200:
                    logger.info(f"method: GET")
                    logger.info(f"status code: {response.status_code}")
                    logger.info(f"retry to: {retry}")
                    
                elif self.show_logs and response.status_code != 200:
                    logger.warning(f"method: GET")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry}")

                return response
            except Exception as err:
                # self.__logs.err(message=err, url=url)
                ic(err)
            sleep(retry_interval)
            retry_interval+= 0.2
        