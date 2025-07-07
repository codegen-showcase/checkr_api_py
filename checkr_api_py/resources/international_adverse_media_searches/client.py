import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class InternationalAdverseMediaSearchesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.InternationalAdverseMediaSearch:
        """
        Retrieve an existing International Adverse Media Search

        Returns an existing International Adverse Media Search with the input ID.


        GET /international_adverse_media_searches/{id}

        Args:
            id: ID of the International Adverse Media Search to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            International Adverse Media Search details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.international_adverse_media_searches.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/international_adverse_media_searches/{id}",
            auth_names=["basic_auth"],
            cast_to=models.InternationalAdverseMediaSearch,
            request_options=request_options or default_request_options(),
        )


class AsyncInternationalAdverseMediaSearchesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.InternationalAdverseMediaSearch:
        """
        Retrieve an existing International Adverse Media Search

        Returns an existing International Adverse Media Search with the input ID.


        GET /international_adverse_media_searches/{id}

        Args:
            id: ID of the International Adverse Media Search to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            International Adverse Media Search details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.international_adverse_media_searches.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/international_adverse_media_searches/{id}",
            auth_names=["basic_auth"],
            cast_to=models.InternationalAdverseMediaSearch,
            request_options=request_options or default_request_options(),
        )
