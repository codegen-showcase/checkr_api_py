import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class ProfessionalLicenseVerificationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ProfessionalLicenseVerification:
        """
        Retrieve an existing Professional License Verification

        Returns an existing Professional License Verification with the input ID.


        GET /professional_license_verifications/{id}

        Args:
            id: ID of the Professional License Verification to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Professional License Verification details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.professional_license_verifications.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/professional_license_verifications/{id}",
            auth_names=["basic_auth"],
            cast_to=models.ProfessionalLicenseVerification,
            request_options=request_options or default_request_options(),
        )


class AsyncProfessionalLicenseVerificationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ProfessionalLicenseVerification:
        """
        Retrieve an existing Professional License Verification

        Returns an existing Professional License Verification with the input ID.


        GET /professional_license_verifications/{id}

        Args:
            id: ID of the Professional License Verification to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Professional License Verification details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.professional_license_verifications.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/professional_license_verifications/{id}",
            auth_names=["basic_auth"],
            cast_to=models.ProfessionalLicenseVerification,
            request_options=request_options or default_request_options(),
        )
