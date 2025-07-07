import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class CompleteClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Report:
        """
        Complete an existing Report

        Cancels all pending or suspended screenings and completes the report.

        Use this endpoint to complete reports which include pending or suspended screenings. If a report is completed with pending or suspended screenings, the following events will be triggered:

          - The `status` for all in-progress screenings within the report will be updated to `canceled`.
          - A cancellation reason and the reason’s description will be added to each canceled screening.
          - Checkr will issue webhooks upon report completion.
            - If all screenings are canceled, a `report.canceled` webhook will be issued.
            - If at least one screening has a result before the report is completed, Checkr will issue two webhooks: first, `report.updated`, followed by `report.complete`.


        POST /reports/{id}/complete

        Args:
            id: The Report's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Report was successfully updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.complete.create(id="string")
        ```
        """
        return self._base_client.request(
            method="POST",
            path=f"/reports/{id}/complete",
            auth_names=["basic_auth"],
            cast_to=models.Report,
            request_options=request_options or default_request_options(),
        )


class AsyncCompleteClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Report:
        """
        Complete an existing Report

        Cancels all pending or suspended screenings and completes the report.

        Use this endpoint to complete reports which include pending or suspended screenings. If a report is completed with pending or suspended screenings, the following events will be triggered:

          - The `status` for all in-progress screenings within the report will be updated to `canceled`.
          - A cancellation reason and the reason’s description will be added to each canceled screening.
          - Checkr will issue webhooks upon report completion.
            - If all screenings are canceled, a `report.canceled` webhook will be issued.
            - If at least one screening has a result before the report is completed, Checkr will issue two webhooks: first, `report.updated`, followed by `report.complete`.


        POST /reports/{id}/complete

        Args:
            id: The Report's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Report was successfully updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.complete.create(id="string")
        ```
        """
        return await self._base_client.request(
            method="POST",
            path=f"/reports/{id}/complete",
            auth_names=["basic_auth"],
            cast_to=models.Report,
            request_options=request_options or default_request_options(),
        )
