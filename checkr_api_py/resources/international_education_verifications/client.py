import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class InternationalEducationVerificationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.InternationalEducationVerification:
        """
        Retrieve an existing International Education Verificaiton

        Returns an existing International Education Verificaiton with the input ID.


        GET /international_education_verifications/{id}

        Args:
            id: ID of the International Education Verificaiton to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            International Education Verification details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.international_education_verifications.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/international_education_verifications/{id}",
            auth_names=["basic_auth"],
            cast_to=models.InternationalEducationVerification,
            request_options=request_options or default_request_options(),
        )


class AsyncInternationalEducationVerificationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.InternationalEducationVerification:
        """
        Retrieve an existing International Education Verificaiton

        Returns an existing International Education Verificaiton with the input ID.


        GET /international_education_verifications/{id}

        Args:
            id: ID of the International Education Verificaiton to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            International Education Verification details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.international_education_verifications.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/international_education_verifications/{id}",
            auth_names=["basic_auth"],
            cast_to=models.InternationalEducationVerification,
            request_options=request_options or default_request_options(),
        )
