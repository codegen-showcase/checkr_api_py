import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class AccountClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Account:
        """
        Retrieve authenticated account details

        Returns Account details for the authenticated account.


        GET /account

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            Account details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.list()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/account",
            auth_names=["basic_auth"],
            cast_to=models.Account,
            request_options=request_options or default_request_options(),
        )


class AsyncAccountClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Account:
        """
        Retrieve authenticated account details

        Returns Account details for the authenticated account.


        GET /account

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            Account details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.list()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/account",
            auth_names=["basic_auth"],
            cast_to=models.Account,
            request_options=request_options or default_request_options(),
        )
