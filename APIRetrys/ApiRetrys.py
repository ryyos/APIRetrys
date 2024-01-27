import requests

from fake_useragent import FakeUserAgent
from requests import Response
from requests.sessions import Session
from typing import Union, List
from time import sleep
from .MaxRetryExceptions import MaxRetryExceptions
from .Logs import logger

class ApiRetry:
    def __init__(self, 
                 redirect_url: str = None,
                 show_logs: bool = False, 
                 exception_code: List[int] = [200, 404, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511],
                 codes_handler: List[int] = [403, 429],
                 handle_forbidden: bool = False,
                 defaulth_headers: bool = False
                 ) -> None:
        
        self.sessions = Session()
        self.faker = FakeUserAgent()
        
        self.show_logs = show_logs
        self.status_code = exception_code
        self.redirect_url = redirect_url
        self.defaulth_headers = defaulth_headers

        self.doit_handler = handle_forbidden
        self.codes_handler = codes_handler

    def get(
            self, 
            url: str, 
            max_retries: int = 5, 
            retry_interval: Union[int, float] = 0.2,
            headers = None, 
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
            header = {"User-Agent": self.faker.random} if self.defaulth_headers else headers
            
            try:
                response = self.sessions.get(
                        url     = url,
                        params  = params,
                        data    = data,
                        headers = header,
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
                    logger.warning(f"retry to: {retry+1}")

                if response.status_code in self.codes_handler and self.doit_handler:
                    logger.warning(f"method: GET")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry+1}")

                    self.sessions.get(url=self.redirect_url, headers=header)
                    sleep(retry_interval)
                    retry_interval+= 5

                    continue

                return response
            except Exception as err:
                logger.error(f'message: {err}')
                logger.warning(f'try the request again')
                logger.warning(f"retry to: {retry+1}")
                print()
                
            sleep(retry_interval)
            retry_interval+= 0.2
        
        raise MaxRetryExceptions(message=f"Failed to retrieve data after {max_retries} retries. The server may be unreachable or experiencing issues")
        

    def post(
            self, 
            url: str, 
            max_retries: int = 5, 
            retry_interval: Union[int, float] = 0.2,
            headers = None, 
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
            header = {"User-Agent": self.faker.random} if self.defaulth_headers else headers

            try:
                response = self.sessions.post(
                    url     = url,
                    data    = data,
                    json    = json,
                    params  = params,
                    headers = header,
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
                    logger.warning(f"retry to: {retry+1}")

                if response.status_code in self.codes_handler and self.doit_handler:
                    logger.warning(f"method: POST")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry+1}")

                    self.sessions.get(url=self.redirect_url, headers=header)
                    sleep(retry_interval)
                    retry_interval+= 5

                    continue


                return response
            except Exception as err:
                logger.error(f'message: {err}')
                logger.warning(f'try the request again')
                logger.warning(f"retry to: {retry+1}")
                print()
                
            sleep(retry_interval)
            retry_interval+= 0.2
        
        raise MaxRetryExceptions(message=f"Failed to retrieve data after {max_retries} retries. The server may be unreachable or experiencing issues")

    def head(
            self, 
            url: str, 
            max_retries: int = 5, 
            retry_interval: Union[int, float] = 0.2,
            headers = None, 
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
            header = {"User-Agent": self.faker.random} if self.defaulth_headers else headers

            try:
                response    = self.sessions.head(
                    url     = url,
                    params  = params,
                    data    = data,
                    headers = header,
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
                    logger.warning(f"retry to: {retry+1}")

                if response.status_code in self.codes_handler and self.doit_handler:
                    logger.warning(f"method: HEAD")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry+1}")

                    self.sessions.get(url=self.redirect_url, headers=header)
                    sleep(retry_interval)
                    retry_interval+= 5

                    continue

                return response
            except Exception as err:
                logger.error(f'message: {err}')
                logger.warning(f'try the request again')
                logger.warning(f"retry to: {retry+1}")
                print()
                
            sleep(retry_interval)
            retry_interval+= 0.2
        
        raise MaxRetryExceptions(message=f"Failed to retrieve data after {max_retries} retries. The server may be unreachable or experiencing issues")

    def put(
            self, 
            url: str, 
            max_retries: int = 5, 
            retry_interval: Union[int, float] = 0.2,
            headers = None, 
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
            header = {"User-Agent": self.faker.random} if self.defaulth_headers else headers

            try:
                response    = self.sessions.put(
                    url     = url,
                    data    = data,
                    params  = params,
                    headers = header,
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
                    logger.warning(f"retry to: {retry+1}")

                if response.status_code in self.codes_handler and self.doit_handler:
                    logger.warning(f"method: PUT")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry+1}")

                    self.sessions.get(url=self.redirect_url, headers=header)
                    sleep(retry_interval)
                    retry_interval+= 5

                    continue


                return response
            except Exception as err:
                logger.error(f'message: {err}')
                logger.warning(f'try the request again')
                logger.warning(f"retry to: {retry+1}")
                print()
                
            sleep(retry_interval)
            retry_interval+= 0.2
        
        raise MaxRetryExceptions(message=f"Failed to retrieve data after {max_retries} retries. The server may be unreachable or experiencing issues")
    

    def delete(
            self, 
            url: str, 
            max_retries: int = 5, 
            retry_interval: Union[int, float] = 0.2,
            headers = None, 
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
            header = {"User-Agent": self.faker.random} if self.defaulth_headers else headers

            try:
                response    = self.sessions.delete(
                    url     = url,
                    params  = params,
                    data    = data,
                    headers = header,
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
                    logger.info(f"method: DELETE")
                    logger.info(f"status code: {response.status_code}")
                    logger.info(f"retry to: {retry}")

                elif self.show_logs and response.status_code != 200:
                    logger.warning(f"method: DELETE")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry+1}")

                if response.status_code in self.codes_handler and self.doit_handler:
                    logger.warning(f"method: DELETE")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry+1}")

                    self.sessions.get(url=self.redirect_url, headers=header)
                    sleep(retry_interval)
                    retry_interval+= 5

                    continue

                return response
            except Exception as err:
                logger.error(f'message: {err}')
                logger.warning(f'try the request again')
                logger.warning(f"retry to: {retry+1}")
                print()
                
            sleep(retry_interval)
            retry_interval+= 0.2
        
        raise MaxRetryExceptions(message=f"Failed to retrieve data after {max_retries} retries. The server may be unreachable or experiencing issues")
    

    def request(
            self, 
            url: str, 
            method: str,
            max_retries: int = 5, 
            retry_interval: Union[int, float] = 0.2,
            headers = None, 
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
            header = {"User-Agent": self.faker.random} if self.defaulth_headers else headers

            try:
                response    = self.sessions.request(
                    method  = method,
                    url     = url,
                    params  = params,
                    data    = data,
                    headers = header,
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
                    logger.info(f"method: REQUEST")
                    logger.info(f"status code: {response.status_code}")
                    logger.info(f"retry to: {retry}")

                elif self.show_logs and response.status_code != 200:
                    logger.warning(f"method: REQUEST")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry+1}")

                if response.status_code in self.codes_handler and self.doit_handler:
                    logger.warning(f"method: REQUEST")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry+1}")

                    self.sessions.get(url=self.redirect_url, headers=header)
                    sleep(retry_interval)
                    retry_interval+= 5

                    continue

                return response
            except Exception as err:
                logger.error(f'message: {err}')
                logger.warning(f'try the request again')
                logger.warning(f"retry to: {retry+1}")
                print()
                
            sleep(retry_interval)
            retry_interval+= 0.2
        
        raise MaxRetryExceptions(message=f"Failed to retrieve data after {max_retries} retries. The server may be unreachable or experiencing issues")
    

    def options(
            self, 
            url: str, 
            max_retries: int = 5, 
            retry_interval: Union[int, float] = 0.2,
            headers = None, 
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
            header = {"User-Agent": self.faker.random} if self.defaulth_headers else headers

            try:
                response = self.sessions.options(
                        url     = url,
                        params  = params,
                        data    = data,
                        headers = header,
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
                    logger.info(f"method: OPTIONS")
                    logger.info(f"status code: {response.status_code}")
                    logger.info(f"retry to: {retry}")

                elif self.show_logs and response.status_code != 200:
                    logger.warning(f"method: OPTIONS")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry+1}")


                if response.status_code in self.codes_handler and self.doit_handler:
                    logger.warning(f"method: OPTIONS")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry+1}")

                    self.sessions.get(url=self.redirect_url, headers=header)
                    sleep(retry_interval)
                    retry_interval+= 5

                    continue


                return response
            except Exception as err:
                logger.error(f'message: {err}')
                logger.warning(f'try the request again')
                logger.warning(f"retry to: {retry+1}")
                print()
                
            sleep(retry_interval)
            retry_interval+= 0.2
        
        raise MaxRetryExceptions(message=f"Failed to retrieve data after {max_retries} retries. The server may be unreachable or experiencing issues")
    

    def patch(
            self, 
            url: str, 
            max_retries: int = 5, 
            retry_interval: Union[int, float] = 0.2,
            headers = None, 
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
            header = {"User-Agent": self.faker.random} if self.defaulth_headers else headers

            try:
                response = self.sessions.patch(
                        url     = url,
                        params  = params,
                        data    = data,
                        headers = header,
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
                    logger.info(f"method: PATCH")
                    logger.info(f"status code: {response.status_code}")
                    logger.info(f"retry to: {retry}")

                elif self.show_logs and response.status_code != 200:
                    logger.warning(f"method: PATCH")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry+1}")

                if response.status_code in self.codes_handler and self.doit_handler:
                    logger.warning(f"method: GET")
                    logger.warning(f"status code: {response.status_code}")
                    logger.warning(f"retry to: {retry+1}")

                    self.sessions.get(url=self.redirect_url, headers=header)
                    sleep(retry_interval)
                    retry_interval+= 5

                    continue


                return response
            except Exception as err:
                logger.error(f'message: {err}')
                logger.warning(f'try the request again')
                logger.warning(f"retry to: {retry+1}")
                print()
                
            sleep(retry_interval)
            retry_interval+= 0.2
        
        raise MaxRetryExceptions(message=f"Failed to retrieve data after {max_retries} retries. The server may be unreachable or experiencing issues")