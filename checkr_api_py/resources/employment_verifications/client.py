import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class EmploymentVerificationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.EmploymentVerification:
        """
        Retrieve an existing Employment Verification

        Returns an existing Employment Verification with the input ID.


        GET /employment_verifications/{id}

        Args:
            id: ID of the Employment Verification to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Employment Verification details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.employment_verifications.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/employment_verifications/{id}",
            auth_names=["basic_auth"],
            cast_to=models.EmploymentVerification,
            request_options=request_options or default_request_options(),
        )


class AsyncEmploymentVerificationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.EmploymentVerification:
        """
        Retrieve an existing Employment Verification

        Returns an existing Employment Verification with the input ID.


        GET /employment_verifications/{id}

        Args:
            id: ID of the Employment Verification to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Employment Verification details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.employment_verifications.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/employment_verifications/{id}",
            auth_names=["basic_auth"],
            cast_to=models.EmploymentVerification,
            request_options=request_options or default_request_options(),
        )
