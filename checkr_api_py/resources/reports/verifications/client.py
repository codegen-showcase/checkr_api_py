import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class VerificationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, report_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ReportsVerificationsListResponse:
        """
        List existing Verifications

        Returns a list of existing Verifications for the input `report_id`.


        GET /reports/{report_id}/verifications

        Args:
            report_id: Returns the list of verifications for the input `report_id`.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Report Verifications

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.verifications.list(report_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/reports/{report_id}/verifications",
            auth_names=["basic_auth"],
            cast_to=models.ReportsVerificationsListResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncVerificationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, report_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ReportsVerificationsListResponse:
        """
        List existing Verifications

        Returns a list of existing Verifications for the input `report_id`.


        GET /reports/{report_id}/verifications

        Args:
            report_id: Returns the list of verifications for the input `report_id`.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Report Verifications

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.verifications.list(report_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/reports/{report_id}/verifications",
            auth_names=["basic_auth"],
            cast_to=models.ReportsVerificationsListResponse,
            request_options=request_options or default_request_options(),
        )
