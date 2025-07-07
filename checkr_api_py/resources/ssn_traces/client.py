import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class SsnTracesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.SsnTrace:
        """
        Retrieve an existing SSN Trace

        Returns an existing SSN Trace with the input ID.


        GET /ssn_traces/{id}

        Args:
            id: ID of the SSN Trace to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            SSN Trace details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.ssn_traces.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/ssn_traces/{id}",
            auth_names=["basic_auth"],
            cast_to=models.SsnTrace,
            request_options=request_options or default_request_options(),
        )


class AsyncSsnTracesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.SsnTrace:
        """
        Retrieve an existing SSN Trace

        Returns an existing SSN Trace with the input ID.


        GET /ssn_traces/{id}

        Args:
            id: ID of the SSN Trace to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            SSN Trace details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.ssn_traces.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/ssn_traces/{id}",
            auth_names=["basic_auth"],
            cast_to=models.SsnTrace,
            request_options=request_options or default_request_options(),
        )
