import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from checkr_api_py.types import models, params


class ContinuousChecksClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ContinuousCheck:
        """
        Cancel an existing Continuous Check

        Cancels an existing Continuous Check.


        DELETE /continuous_checks/{id}

        Args:
            id: The Continuous Check's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Continuous Check was successfully canceled

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.continuous_checks.delete(id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/continuous_checks/{id}",
            auth_names=["basic_auth"],
            cast_to=models.ContinuousCheck,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ContinuousCheck:
        """
        Retrieve an existing Continuous Check

        Returns an existing Continuous Check with the input ID.


        GET /continuous_checks/{id}

        Args:
            id: The Continuous Check's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Continuous Check details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.continuous_checks.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/continuous_checks/{id}",
            auth_names=["basic_auth"],
            cast_to=models.ContinuousCheck,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        id: str,
        node: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        work_locations: typing.Union[
            typing.Optional[typing.List[params.WorkLocation]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ContinuousCheck:
        """
        Update an existing Continuous Check

        Updates the node and/or work locations of an existing Continuous Check.


        POST /continuous_checks/{id}

        Args:
            node: `custom_id` of the associated node.

            work_locations: Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.

            id: The Continuous Check's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Continuous Check was successfully updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.continuous_checks.create(id="string")
        ```
        """
        _json = to_encodable(
            item={"node": node, "work_locations": work_locations},
            dump_with=params._SerializerContinuousChecksCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path=f"/continuous_checks/{id}",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.ContinuousCheck,
            request_options=request_options or default_request_options(),
        )


class AsyncContinuousChecksClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ContinuousCheck:
        """
        Cancel an existing Continuous Check

        Cancels an existing Continuous Check.


        DELETE /continuous_checks/{id}

        Args:
            id: The Continuous Check's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Continuous Check was successfully canceled

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.continuous_checks.delete(id="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/continuous_checks/{id}",
            auth_names=["basic_auth"],
            cast_to=models.ContinuousCheck,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ContinuousCheck:
        """
        Retrieve an existing Continuous Check

        Returns an existing Continuous Check with the input ID.


        GET /continuous_checks/{id}

        Args:
            id: The Continuous Check's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Continuous Check details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.continuous_checks.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/continuous_checks/{id}",
            auth_names=["basic_auth"],
            cast_to=models.ContinuousCheck,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        id: str,
        node: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        work_locations: typing.Union[
            typing.Optional[typing.List[params.WorkLocation]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ContinuousCheck:
        """
        Update an existing Continuous Check

        Updates the node and/or work locations of an existing Continuous Check.


        POST /continuous_checks/{id}

        Args:
            node: `custom_id` of the associated node.

            work_locations: Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.

            id: The Continuous Check's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Continuous Check was successfully updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.continuous_checks.create(id="string")
        ```
        """
        _json = to_encodable(
            item={"node": node, "work_locations": work_locations},
            dump_with=params._SerializerContinuousChecksCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/continuous_checks/{id}",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.ContinuousCheck,
            request_options=request_options or default_request_options(),
        )
