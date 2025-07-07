import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class AdverseItemsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, report_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ReportsAdverseItemsListResponse:
        """
        List existing Adverse Items

        Returns a list of existing Adverse Items with the input `report_id`.

        <b>Note: </b>Report must be in a `consider` status and cannot have any existing Adverse Actions that have not been canceled.

        Returns 400 if the Report's status is not Consider or the Report already has an active (non-cancelled) Adverse Action.


        GET /reports/{report_id}/adverse_items

        Args:
            report_id: The ID of the associated Report.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Adverse Items

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.adverse_items.list(report_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/reports/{report_id}/adverse_items",
            auth_names=["basic_auth"],
            cast_to=models.ReportsAdverseItemsListResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAdverseItemsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, report_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ReportsAdverseItemsListResponse:
        """
        List existing Adverse Items

        Returns a list of existing Adverse Items with the input `report_id`.

        <b>Note: </b>Report must be in a `consider` status and cannot have any existing Adverse Actions that have not been canceled.

        Returns 400 if the Report's status is not Consider or the Report already has an active (non-cancelled) Adverse Action.


        GET /reports/{report_id}/adverse_items

        Args:
            report_id: The ID of the associated Report.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Adverse Items

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.adverse_items.list(report_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/reports/{report_id}/adverse_items",
            auth_names=["basic_auth"],
            cast_to=models.ReportsAdverseItemsListResponse,
            request_options=request_options or default_request_options(),
        )
