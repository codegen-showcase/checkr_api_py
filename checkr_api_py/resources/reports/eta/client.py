import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class EtaClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ReportEta:
        """
        Retrieve a Report's ETA

        Returns an existing Report ETA for the input Report ID.


        GET /reports/{id}/eta

        Args:
            id: ID of the Report for which the ETA was generated.
            request_options: Additional options to customize the HTTP request

        Returns:
            Report ETA

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.eta.list(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/reports/{id}/eta",
            auth_names=["basic_auth"],
            cast_to=models.ReportEta,
            request_options=request_options or default_request_options(),
        )


class AsyncEtaClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ReportEta:
        """
        Retrieve a Report's ETA

        Returns an existing Report ETA for the input Report ID.


        GET /reports/{id}/eta

        Args:
            id: ID of the Report for which the ETA was generated.
            request_options: Additional options to customize the HTTP request

        Returns:
            Report ETA

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.eta.list(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/reports/{id}/eta",
            auth_names=["basic_auth"],
            cast_to=models.ReportEta,
            request_options=request_options or default_request_options(),
        )
