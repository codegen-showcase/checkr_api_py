import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class SexOffenderSearchesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.SexOffenderSearch:
        """
        Retrieve an existing Sex Offender Registry Search

        Returns an existing Sex Offender Registry Search with the input ID.


        GET /sex_offender_searches/{id}

        Args:
            id: ID of the Sex Offender Search to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Sex Offender Registry Search details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sex_offender_searches.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sex_offender_searches/{id}",
            auth_names=["basic_auth"],
            cast_to=models.SexOffenderSearch,
            request_options=request_options or default_request_options(),
        )


class AsyncSexOffenderSearchesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.SexOffenderSearch:
        """
        Retrieve an existing Sex Offender Registry Search

        Returns an existing Sex Offender Registry Search with the input ID.


        GET /sex_offender_searches/{id}

        Args:
            id: ID of the Sex Offender Search to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Sex Offender Registry Search details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sex_offender_searches.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sex_offender_searches/{id}",
            auth_names=["basic_auth"],
            cast_to=models.SexOffenderSearch,
            request_options=request_options or default_request_options(),
        )
