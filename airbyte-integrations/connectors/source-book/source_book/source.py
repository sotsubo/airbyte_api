from abc import ABC
from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Tuple

import requests
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream
from airbyte_cdk.sources.streams.http import HttpStream
from airbyte_cdk.sources.streams.http.auth import TokenAuthenticator

class Book(HttpStream, ABC):
    date_field_name = "date"

    url_base = "https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json"
    cursor_field = date_field_name
    primary_key = ""

    def __init__(self, publisher: Optional[str],  title: Optional[str],  price: Optional[str], offset: Optional[int],  isbn: Optional[str], contributor: Optional[str], author: Optional[str], age_group: Optional[str], api_key: str):
        super().__init__()
        self.publisher = publisher
        self.api_key = api_key

        self.age_group = age_group
        self.author = author
        self.contributor = contributor
        self.isbn = isbn
        if offset:
            self.offset = offset
        else: 
            self.offset = 0
        self.price = price
        self.title = title

    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        response_json = response.json()
        if (response_json['num_results'] - self.offset) > 20:
            self.offset  += 20
            print ("response_json['num_results'",response_json['num_results'])

            print ("self.offset",self.offset)

            return {"offset": self.offset}
        
    def path(
        self, stream_state: Mapping[str, Any] = None, stream_slice: Mapping[str, Any] = None, next_page_token: Mapping[str, Any] = None
    ) -> str:
        return ''
    def request_params(self, next_page_token: Mapping[str, Any] = None, **kwargs) -> MutableMapping[str, Any]:
        params = {"api-key": self.api_key}

        if self.age_group is not None:
            params["age-group"] = self.age_group
        if self.author is not None:
            params["author"] = self.author
        if self.contributor is not None:
            params["contributor"] = self.contributor
        if self.isbn is not None:
            params["isbn"] = self.isbn
        if self.offset is not None:
            params["offset"] = self.offset
        if self.price is not None:
            params["price"] = self.price
        if self.publisher is not None:
            params["publisher"] = self.publisher
        if self.title is not None:
            params["title"] = self.title
        if next_page_token:
            params.update(next_page_token)
        return params

    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        response_json = response.json()
        yield response_json
class OffsetException(Exception):
    pass

class SourceBook(AbstractSource):
    def check_connection(self, logger, config) -> Tuple[bool, any]:
        try:
            params = {"api-key": config["api_key"]}
            publisher = config.get("publisher")
            if publisher is not None:
                params["publisher"] = publisher
            age_group = config.get("age_group")
            if age_group is not None:
                params["age-group"] = age_group
            author = config.get("author")
            if author is not None:
                params["author"] = author
            contributor = config.get("contributor")
            if contributor is not None:
                params["contributor"] = contributor
            isbn = config.get("isbn")
            if isbn is not None:
                params["isbn"] = isbn
            offset = config.get("offset")
            if offset is not None:
                try:
                    if  (offset % 20) != 0:
                        raise OffsetException("offset must be a multiple of 20")
                    else:
                        params["offset"] = offset
                except OffsetException as e:
                    return False, e

            price = config.get("price")
            if price is not None:
                params["price"] = price
            title = config.get("title")
            if title is not None:
                params["title"] = title
            resp = requests.get(f"{Book.url_base}", params=params)
            status = resp.status_code
            logger.info(f"Ping response code: {status}")
            if status == 200:
                return True, None
       
        except Exception as e:
            return False, e

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        return [Book(config.get("publisher"), config.get("title"), config.get("price"), config.get("offset"), config.get("isbn"), config.get("contributor"), config.get("author"), config.get("age_group"),  config["api_key"])]

    