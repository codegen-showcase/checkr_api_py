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


class UsersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

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
    ) -> models.UsersListResponse:
        """
        List existing Users

        Returns a list of all existing Users.


        GET /users

        Args:
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Users

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.users.list()
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
            path="/users",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.UsersListResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncUsersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

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
    ) -> models.UsersListResponse:
        """
        List existing Users

        Returns a list of all existing Users.


        GET /users

        Args:
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Users

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.users.list()
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
            path="/users",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.UsersListResponse,
            request_options=request_options or default_request_options(),
        )
