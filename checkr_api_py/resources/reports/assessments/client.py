import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class AssessmentsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, report_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ReportsAssessmentsListResponse:
        """
        List existing Assessments

        Returns Assessments for an existing Report.


        GET /reports/{report_id}/assessments

        Args:
            report_id: The ID of the associated Report.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Assessments

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.assessments.list(report_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/reports/{report_id}/assessments",
            auth_names=["basic_auth"],
            cast_to=models.ReportsAssessmentsListResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAssessmentsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, report_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ReportsAssessmentsListResponse:
        """
        List existing Assessments

        Returns Assessments for an existing Report.


        GET /reports/{report_id}/assessments

        Args:
            report_id: The ID of the associated Report.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Assessments

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.assessments.list(report_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/reports/{report_id}/assessments",
            auth_names=["basic_auth"],
            cast_to=models.ReportsAssessmentsListResponse,
            request_options=request_options or default_request_options(),
        )
