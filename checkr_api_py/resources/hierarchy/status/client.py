import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class StatusClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.HierarchyStatusListResponse:
        """
        Retrieve Hierarchy update status

        Returns the status of the latest Hierarchy ingestion request.

        This call requires no input, and is provided as a means to determine the progress of an
        asynchronous `POST /hierarchy` request.


        GET /hierarchy/status

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            The current status of hierarchy ingestion.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.hierarchy.status.list()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/hierarchy/status",
            auth_names=["basic_auth"],
            cast_to=models.HierarchyStatusListResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncStatusClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.HierarchyStatusListResponse:
        """
        Retrieve Hierarchy update status

        Returns the status of the latest Hierarchy ingestion request.

        This call requires no input, and is provided as a means to determine the progress of an
        asynchronous `POST /hierarchy` request.


        GET /hierarchy/status

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            The current status of hierarchy ingestion.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.hierarchy.status.list()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/hierarchy/status",
            auth_names=["basic_auth"],
            cast_to=models.HierarchyStatusListResponse,
            request_options=request_options or default_request_options(),
        )
