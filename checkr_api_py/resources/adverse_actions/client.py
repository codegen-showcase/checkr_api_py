import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class AdverseActionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.AdverseAction:
        """
        Cancel an existing Adverse Action

        Cancels an existing Adverse Action.


        DELETE /adverse_actions/{id}

        Args:
            id: ID of the Adverse Action.
            request_options: Additional options to customize the HTTP request

        Returns:
            Adverse Action was successfully canceled

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.adverse_actions.delete(id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/adverse_actions/{id}",
            auth_names=["basic_auth"],
            cast_to=models.AdverseAction,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.AdverseAction:
        """
        Retrieve an existing Adverse Action

        Returns an existing Adverse Action with the input ID.


        GET /adverse_actions/{id}

        Args:
            id: ID of the Adverse Action.
            request_options: Additional options to customize the HTTP request

        Returns:
            Adverse Action details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.adverse_actions.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/adverse_actions/{id}",
            auth_names=["basic_auth"],
            cast_to=models.AdverseAction,
            request_options=request_options or default_request_options(),
        )


class AsyncAdverseActionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.AdverseAction:
        """
        Cancel an existing Adverse Action

        Cancels an existing Adverse Action.


        DELETE /adverse_actions/{id}

        Args:
            id: ID of the Adverse Action.
            request_options: Additional options to customize the HTTP request

        Returns:
            Adverse Action was successfully canceled

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.adverse_actions.delete(id="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/adverse_actions/{id}",
            auth_names=["basic_auth"],
            cast_to=models.AdverseAction,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.AdverseAction:
        """
        Retrieve an existing Adverse Action

        Returns an existing Adverse Action with the input ID.


        GET /adverse_actions/{id}

        Args:
            id: ID of the Adverse Action.
            request_options: Additional options to customize the HTTP request

        Returns:
            Adverse Action details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.adverse_actions.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/adverse_actions/{id}",
            auth_names=["basic_auth"],
            cast_to=models.AdverseAction,
            request_options=request_options or default_request_options(),
        )
