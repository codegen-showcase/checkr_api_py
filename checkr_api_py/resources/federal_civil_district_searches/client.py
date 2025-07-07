import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class FederalCivilDistrictSearchesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.FederalDistrictCivilSearch:
        """
        Retrieve an existing Federal District Civil Search

        Returns an existing Federal District Civil Search with the input ID.


        GET /federal_civil_district_searches/{id}

        Args:
            id: ID of the Federal District Civil Search to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Federal District Civil Search details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.federal_civil_district_searches.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/federal_civil_district_searches/{id}",
            auth_names=["basic_auth"],
            cast_to=models.FederalDistrictCivilSearch,
            request_options=request_options or default_request_options(),
        )


class AsyncFederalCivilDistrictSearchesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.FederalDistrictCivilSearch:
        """
        Retrieve an existing Federal District Civil Search

        Returns an existing Federal District Civil Search with the input ID.


        GET /federal_civil_district_searches/{id}

        Args:
            id: ID of the Federal District Civil Search to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Federal District Civil Search details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.federal_civil_district_searches.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/federal_civil_district_searches/{id}",
            auth_names=["basic_auth"],
            cast_to=models.FederalDistrictCivilSearch,
            request_options=request_options or default_request_options(),
        )
