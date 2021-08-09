#
# MIT License
#
# Copyright (c) 2020 Airbyte
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#


from abc import ABC
from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Tuple

import requests
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream
from airbyte_cdk.sources.streams.http import HttpStream
from airbyte_cdk.sources.streams.http.auth import TokenAuthenticator

"""
TODO: Most comments in this class are instructive and should be deleted after the source is implemented.

This file provides a stubbed example of how to use the Airbyte CDK to develop both a source connector which supports full refresh or and an
incremental syncs from an HTTP API.

The various TODOs are both implementation hints and steps - fulfilling all the TODOs should be sufficient to implement one basic and one incremental
stream from a source. This pattern is the same one used by Airbyte internally to implement connectors.

The approach here is not authoritative, and devs are free to use their own judgement.

There are additional required TODOs in the files within the integration_tests folder and the spec.json file.
"""


# Basic full refresh stream
class Book(HttpStream, ABC):
    """  
    TODO remove this comment

    This class represents a stream output by the connector.
    This is an abstract base class meant to contain all the common functionality at the API level e.g: the API base URL, pagination strategy,
    parsing responses etc..

    Each stream should extend this class (or another abstract subclass of it) to specify behavior unique to that stream.

    Typically for REST APIs each stream corresponds to a resource in the API. For example if the API
    contains the endpoints
        - GET v1/customers
        - GET v1/employees

    then you should have three classes:
    `class BookStream(HttpStream, ABC)` which is the current class
    `class Customers(BookStream)` contains behavior to pull data for customers using v1/customers
    `class Employees(BookStream)` contains behavior to pull data for employees using v1/employees

    If some streams implement incremental sync, it is typical to create another class
    `class IncrementalBookStream((BookStream), ABC)` then have concrete stream implementations extend it. An example
    is provided below.

    See the reference docs for the full list of configurable options.
    """
    date_field_name = "date"

    # TODO: Fill in the url base. Required.
    url_base = "https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json"
    cursor_field = date_field_name
    primary_key = ""

    def __init__(self, publisher: Optional[str],  title: Optional[str],  price: Optional[str], offset: Optional[str],  isbn: Optional[str], contributor: Optional[str], author: Optional[str], age_group: Optional[str], api_key: str):
        super().__init__()
        self.publisher = publisher
        self.api_key = api_key

        self.age_group = age_group
        self.author = author
        self.contributor = contributor
        self.isbn = isbn
        self.offset = offset
        self.price = price
        self.title = title

    # def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
    #     """
    #     TODO: Override this method to define a pagination strategy. If you will not be using pagination, no action is required - just return None.

    #     This method should return a Mapping (e.g: dict) containing whatever information required to make paginated requests. This dict is passed
    #     to most other methods in this class to help you form headers, request bodies, query params, etc..

    #     For example, if the API accepts a 'page' parameter to determine which page of the result to return, and a response from the API contains a
    #     'page' number, then this method should probably return a dict {'page': response.json()['page'] + 1} to increment the page count by 1.
    #     The request_params method should then read the input next_page_token and set the 'page' param to next_page_token['page'].

    #     :param response: the most recent response from the API
    #     :return If there is another page in the result, a mapping (e.g: dict) containing information needed to query the next page in the response.
    #             If there are no more pages in the result, return None.
    #     """
    #     return None
    def path(
        self, stream_state: Mapping[str, Any] = None, stream_slice: Mapping[str, Any] = None, next_page_token: Mapping[str, Any] = None
    ) -> str:
        some_path=''
        return some_path
        # ,stream_slice[self.date_field_name]

    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        return None
    def request_params(self, **kwargs) -> MutableMapping[str, Any]:
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

        return params

    # def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
    #     """
    #     TODO: Override this method to define how a response is parsed.
    #     :return an iterable containing each record in the response
    #     """
    #     yield {}
    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        response_json = response.json()
        yield response_json

    # def stream_slices(self, stream_state: Mapping[str, Any] = None, **kwargs) -> Iterable[Optional[Mapping[str, any]]]:
    #     stream_state = stream_state or {}
    #     start_date = pendulum.parse(stream_state.get(self.date_field_name, self._start_date))
    #     return chunk_date_range(start_date)

    # def get_updated_state(self, current_stream_state: MutableMapping[str, Any], latest_record: Mapping[str, Any]):
    #     current_stream_state = current_stream_state or {}
    #     current_stream_state[self.date_field_name] = max(
    #         latest_record[self.date_field_name], current_stream_state.get(self.date_field_name, self._start_date)
    #     )
    #     return current_stream_state
    def get_updated_state(self, current_stream_state: MutableMapping[str, Any], latest_record: Mapping[str, Any]) -> Mapping[str, Any]:
        """
        Override to determine the latest state after reading the latest record. This typically compared the cursor_field from the latest record and
        the current state and picks the 'most' recent cursor. This is how a stream's state is determined. Required for incremental.
        """
        return {}
class Customers(Book):
    """
    TODO: Change class name to match the table/data source this stream corresponds to.
    """

    # TODO: Fill in the primary key. Required. This is usually a unique field in the stream, like an ID or a timestamp.
    primary_key = "customer_id"

    def path(
        self, stream_state: Mapping[str, Any] = None, stream_slice: Mapping[str, Any] = None, next_page_token: Mapping[str, Any] = None
    ) -> str:
        """
        TODO: Override this method to define the path this stream corresponds to. E.g. if the url is https://example-api.com/v1/customers then this
        should return "customers". Required.
        """
        return "customers"


# Basic incremental stream
class IncrementalBook(Book, ABC):
    """
    TODO fill in details of this class to implement functionality related to incremental syncs for your connector.
         if you do not need to implement incremental sync for any streams, remove this class.
    """

    # TODO: Fill in to checkpoint stream reads after N records. This prevents re-reading of data if the stream fails for any reason.
    state_checkpoint_interval = None

    @property
    def cursor_field(self) -> str:
        """
        TODO
        Override to return the cursor field used by this stream e.g: an API entity might always use created_at as the cursor field. This is
        usually id or date based. This field's presence tells the framework this in an incremental stream. Required for incremental.

        :return str: The name of the cursor field.
        """
        return []

    def get_updated_state(self, current_stream_state: MutableMapping[str, Any], latest_record: Mapping[str, Any]) -> Mapping[str, Any]:
        """
        Override to determine the latest state after reading the latest record. This typically compared the cursor_field from the latest record and
        the current state and picks the 'most' recent cursor. This is how a stream's state is determined. Required for incremental.
        """
        return {}


class Employees(IncrementalBook):
    """
    TODO: Change class name to match the table/data source this stream corresponds to.
    """

    # TODO: Fill in the cursor_field. Required.
    cursor_field = "start_date"

    # TODO: Fill in the primary key. Required. This is usually a unique field in the stream, like an ID or a timestamp.
    primary_key = "employee_id"

    def path(self, **kwargs) -> str:
        """
        TODO: Override this method to define the path this stream corresponds to. E.g. if the url is https://example-api.com/v1/employees then this should
        return "single". Required.
        """
        return "employees"

    def stream_slices(self, stream_state: Mapping[str, Any] = None, **kwargs) -> Iterable[Optional[Mapping[str, any]]]:
        """
        TODO: Optionally override this method to define this stream's slices. If slicing is not needed, delete this method.

        Slices control when state is saved. Specifically, state is saved after a slice has been fully read.
        This is useful if the API offers reads by groups or filters, and can be paired with the state object to make reads efficient. See the "concepts"
        section of the docs for more information.

        The function is called before reading any records in a stream. It returns an Iterable of dicts, each containing the
        necessary data to craft a request for a slice. The stream state is usually referenced to determine what slices need to be created.
        This means that data in a slice is usually closely related to a stream's cursor_field and stream_state.

        An HTTP request is made for each returned slice. The same slice can be accessed in the path, request_params and request_header functions to help
        craft that specific request.

        For example, if https://example-api.com/v1/employees offers a date query params that returns data for that particular day, one way to implement
        this would be to consult the stream state object for the last synced date, then return a slice containing each date from the last synced date
        till now. The request_params function would then grab the date from the stream_slice and make it part of the request by injecting it into
        the date query param.
        """
        raise NotImplementedError("Implement stream slices or delete this method!")
"""
algo 
"""

# Source
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
                params["offset"] = offset
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
            # When API requests is sent but the requested data is not available or the API call fails
            # for some reason, a JSON error is returned.
            # https://exchangeratesapi.io/documentation/#errors
            error = resp.json().get("error")
            code = error.get("code")
            message = error.get("message") or error.get("info")
            # If code is base_currency_access_restricted, error is caused by switching base currency while using free
            # plan
            # if code :
            #     message = f"{message} (this plan doesn't support selecting the base currency)"
            return False
        except Exception as e:
            return False, e

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        return [Book(config.get("publisher"), config.get("title"), config.get("price"), config.get("offset"), config.get("isbn"), config.get("contributor"), config.get("author"), config.get("age_group"),  config["api_key"])]

    # def check_connection(self, logger, config) -> Tuple[bool, any]:
    #     """
    #     TODO: Implement a connection check to validate that the user-provided config can be used to connect to the underlying API

    #     See https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-stripe/source_stripe/source.py#L232
    #     for an example.

    #     :param config:  the user-input config object conforming to the connector's spec.json
    #     :param logger:  logger object
    #     :return Tuple[bool, any]: (True, None) if the input config can be used to connect to the API successfully, (False, error) otherwise.
    #     """
    #     return True, None

    # def streams(self, config: Mapping[str, Any]) -> List[Stream]:
    #     """
    #     TODO: Replace the streams below with your own streams.

    #     :param config: A Mapping of the user input configuration as defined in the connector spec.
    #     """
    #     # TODO remove the authenticator if not required.
    #     auth = TokenAuthenticator(token="api_key")  # Oauth2Authenticator is also available if you need oauth support
    #     return [Customers(authenticator=auth), Employees(authenticator=auth)]
