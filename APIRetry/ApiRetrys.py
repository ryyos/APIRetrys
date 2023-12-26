import requests
from requests import Response
from typing import Union
from time import sleep
from icecream import ic
from Exceptions.MaxRetryExceptions import MaxRetryExceptions
from utils.Logs import logger

class ApiRetry:
    def __init__(self, show_logs: bool = False) -> None:
        self.show_logs = show_logs

    def get(
            self, 
            url: str, 
            headers: dict, 
            max_retries: int = 5, 
            retry_interval: Union[int, float] = 0.2,
            params  = None,
            data    = None,
            cookies = None,
            files   = None,
            auth    = None,
            timeout = None,
            proxies = None,
            hooks   = None,
            stream  = None,
            verify  = None,
            cert    = None,
            json    = None,
            ) -> Response:
        
        for retry in range(max_retries):
            try:
                response = requests.get(
                        url     = url,
                        params  = params,
                        data    = data,
                        headers = headers,
                        cookies = cookies,
                        files   = files,
                        auth    = auth,
                        timeout = timeout,
                        proxies = proxies,
                        hooks   = hooks,
                        stream  = stream,
                        verify  = verify,
                        cert    = cert,
                        json    = json,
                )

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
        
        raise MaxRetryExceptions(message=f"Failed to retrieve data after {max_retries} retries. The server may be unreachable or experiencing issues")
        

    def post(
            self, 
            url: str, 
            headers: dict, 
            max_retries: int = 5, 
            retry_interval: Union[int, float] = 0.2,
            data    = None,
            json    = None,
            params  = None,
            cookies = None,
            files   = None,
            auth    = None,
            timeout = None,
            proxies = None,
            hooks   = None,
            stream  = None,
            verify  = None,
            cert    = None,
            ) -> Response:
        
        for retry in range(max_retries):
            try:
                response = requests.post(
                    url     = url,
                    data    = data,
                    json    = json,
                    params  = params,
                    headers = headers,
                    cookies = cookies,
                    files   = files,
                    auth    = auth,
                    timeout = timeout,
                    proxies = proxies,
                    hooks   = hooks,
                    stream  = stream,
                    verify  = verify,
                    cert    = cert,
                )

                if self.show_logs and response.status_code == 200:
                    logger.info(f"method: POST")
                    logger.info(f"status code: {response.status_code}")
                    logger.info(f"retry to: {retry}")

                elif self.show_logs and response.status_code != 200:
                    logger.warning(f"method: POST")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry}")


                return response
            except Exception as err:
                logger.error(f'message: {err}')
                logger.warning(f'try the request again')
                
            sleep(retry_interval)
            retry_interval+= 0.2
        
        raise MaxRetryExceptions(message=f"Failed to retrieve data after {max_retries} retries. The server may be unreachable or experiencing issues")

    def head(
            self, 
            url: str, 
            headers: dict, 
            max_retries: int = 5, 
            retry_interval: Union[int, float] = 0.2,
            params  = None,
            data    = None,
            cookies = None,
            files   = None,
            auth    = None,
            timeout = None,
            proxies = None,
            hooks   = None,
            stream  = None,
            verify  = None,
            cert    = None,
            json    = None,
            ) -> Response:
        
        for retry in range(max_retries):
            try:
                response    = requests.head(
                    url     = url,
                    params  = params,
                    data    = data,
                    headers = headers,
                    cookies = cookies,
                    files   = files,
                    auth    = auth,
                    timeout = timeout,
                    proxies = proxies,
                    hooks   = hooks,
                    stream  = stream,
                    verify  = verify,
                    cert    = cert,
                    json    = json,
                )

                if self.show_logs and response.status_code == 200:
                    logger.info(f"method: HEAD")
                    logger.info(f"status code: {response.status_code}")
                    logger.info(f"retry to: {retry}")

                elif self.show_logs and response.status_code != 200:
                    logger.warning(f"method: HEAD")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry}")


                return response
            except Exception as err:
                logger.error(f'message: {err}')
                logger.warning(f'try the request again')
                
            sleep(retry_interval)
            retry_interval+= 0.2
        
        raise MaxRetryExceptions(message=f"Failed to retrieve data after {max_retries} retries. The server may be unreachable or experiencing issues")

    def put(
            self, 
            url: str, 
            headers: dict, 
            max_retries: int = 5, 
            retry_interval: Union[int, float] = 0.2,
            data    = None,
            params  = None,
            cookies = None,
            files   = None,
            auth    = None,
            timeout = None,
            proxies = None,
            hooks   = None,
            stream  = None,
            verify  = None,
            cert    = None,
            json    = None,
            ) -> Response:
        
        for retry in range(max_retries):
            try:
                response    = requests.put(
                    url     = url,
                    data    = data,
                    params  = params,
                    headers = headers,
                    cookies = cookies,
                    files   = files,
                    auth    = auth,
                    timeout = timeout,
                    proxies = proxies,
                    hooks   = hooks,
                    stream  = stream,
                    verify  = verify,
                    cert    = cert,
                    json    = json,
                )

                if self.show_logs and response.status_code == 200:
                    logger.info(f"method: PUT")
                    logger.info(f"status code: {response.status_code}")
                    logger.info(f"retry to: {retry}")

                elif self.show_logs and response.status_code != 200:
                    logger.warning(f"method: PUT")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry}")


                return response
            except Exception as err:
                logger.error(f'message: {err}')
                logger.warning(f'try the request again')
                
            sleep(retry_interval)
            retry_interval+= 0.2
        
        raise MaxRetryExceptions(message=f"Failed to retrieve data after {max_retries} retries. The server may be unreachable or experiencing issues")