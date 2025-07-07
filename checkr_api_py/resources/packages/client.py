import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from checkr_api_py.types import models


class PackagesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Package:
        """
        Delete an existing Package

        Deletes an existing Package.


        DELETE /packages/{id}

        Args:
            id: ID of the Package to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Package was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.packages.delete(id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/packages/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Package,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PackagesListResponse:
        """
        List existing Packages

        Returns a list of all existing Packages.


        GET /packages

        Args:
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Packages

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.packages.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=typing.Optional[float]),
                style="form",
                explode=True,
            )
        if not isinstance(per_page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "per_page",
                to_encodable(item=per_page, dump_with=typing.Optional[float]),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/packages",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.PackagesListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Package:
        """
        Retrieve an existing Package

        Returns an existing Package with the input ID.


        GET /packages/{id}

        Args:
            id: ID of the Package to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Package details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.packages.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/packages/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Package,
            request_options=request_options or default_request_options(),
        )


class AsyncPackagesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Package:
        """
        Delete an existing Package

        Deletes an existing Package.


        DELETE /packages/{id}

        Args:
            id: ID of the Package to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Package was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.packages.delete(id="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/packages/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Package,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PackagesListResponse:
        """
        List existing Packages

        Returns a list of all existing Packages.


        GET /packages

        Args:
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Packages

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.packages.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=typing.Optional[float]),
                style="form",
                explode=True,
            )
        if not isinstance(per_page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "per_page",
                to_encodable(item=per_page, dump_with=typing.Optional[float]),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/packages",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.PackagesListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Package:
        """
        Retrieve an existing Package

        Returns an existing Package with the input ID.


        GET /packages/{id}

        Args:
            id: ID of the Package to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Package details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.packages.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/packages/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Package,
            request_options=request_options or default_request_options(),
        )
