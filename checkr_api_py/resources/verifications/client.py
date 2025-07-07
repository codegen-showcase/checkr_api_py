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

    def get(
        self,
        *,
        verification_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Verification:
        """
        Retrieve a Verification

        Returns an existing Verification with the input ID


        GET /verifications/{verification_id}

        Args:
            verification_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Verification details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.verifications.get(verification_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/verifications/{verification_id}",
            auth_names=["basic_auth"],
            cast_to=models.Verification,
            request_options=request_options or default_request_options(),
        )


class AsyncVerificationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        verification_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Verification:
        """
        Retrieve a Verification

        Returns an existing Verification with the input ID


        GET /verifications/{verification_id}

        Args:
            verification_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Verification details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.verifications.get(verification_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/verifications/{verification_id}",
            auth_names=["basic_auth"],
            cast_to=models.Verification,
            request_options=request_options or default_request_options(),
        )
