import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class InternationalCriminalSearchesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.InternationalCriminalSearch:
        """
        Retrieve an existing International Criminal Search

        Returns an existing International Criminal Search with the input ID.


        GET /international_criminal_searches/{id}

        Args:
            id: ID of the International Criminal Search to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            International Criminal Search details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.international_criminal_searches.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/international_criminal_searches/{id}",
            auth_names=["basic_auth"],
            cast_to=models.InternationalCriminalSearch,
            request_options=request_options or default_request_options(),
        )


class AsyncInternationalCriminalSearchesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.InternationalCriminalSearch:
        """
        Retrieve an existing International Criminal Search

        Returns an existing International Criminal Search with the input ID.


        GET /international_criminal_searches/{id}

        Args:
            id: ID of the International Criminal Search to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            International Criminal Search details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.international_criminal_searches.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/international_criminal_searches/{id}",
            auth_names=["basic_auth"],
            cast_to=models.InternationalCriminalSearch,
            request_options=request_options or default_request_options(),
        )
