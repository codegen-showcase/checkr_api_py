import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class MotorVehicleReportsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.MotorVehicleReport:
        """
        Retrieve an existing Motor Vehicle Report

        Returns an existing Motor Vehicle Report with the input ID.


        GET /motor_vehicle_reports/{id}

        Args:
            id: ID of the Motor Vehicle Report to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Motor Vehicle Report details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.motor_vehicle_reports.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/motor_vehicle_reports/{id}",
            auth_names=["basic_auth"],
            cast_to=models.MotorVehicleReport,
            request_options=request_options or default_request_options(),
        )


class AsyncMotorVehicleReportsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.MotorVehicleReport:
        """
        Retrieve an existing Motor Vehicle Report

        Returns an existing Motor Vehicle Report with the input ID.


        GET /motor_vehicle_reports/{id}

        Args:
            id: ID of the Motor Vehicle Report to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Motor Vehicle Report details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.motor_vehicle_reports.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/motor_vehicle_reports/{id}",
            auth_names=["basic_auth"],
            cast_to=models.MotorVehicleReport,
            request_options=request_options or default_request_options(),
        )
