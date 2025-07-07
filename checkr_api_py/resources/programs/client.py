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


class ProgramsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ProgramsListResponse:
        """
        List existing Programs

        Returns a list of existing Programs with the input `name`.


        GET /programs

        Args:
            name: Returns Programs with the input `name`.
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Programs

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.programs.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "name",
                to_encodable(item=name, dump_with=str),
                style="form",
                explode=True,
            )
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
            path="/programs",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.ProgramsListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Program:
        """
        Retrieve an existing Program

        Returns an existing Program with the input ID.


        GET /programs/{id}

        Args:
            id: ID of the Program to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Program details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.programs.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/programs/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Program,
            request_options=request_options or default_request_options(),
        )


class AsyncProgramsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ProgramsListResponse:
        """
        List existing Programs

        Returns a list of existing Programs with the input `name`.


        GET /programs

        Args:
            name: Returns Programs with the input `name`.
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Programs

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.programs.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "name",
                to_encodable(item=name, dump_with=str),
                style="form",
                explode=True,
            )
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
            path="/programs",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.ProgramsListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Program:
        """
        Retrieve an existing Program

        Returns an existing Program with the input ID.


        GET /programs/{id}

        Args:
            id: ID of the Program to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Program details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.programs.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/programs/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Program,
            request_options=request_options or default_request_options(),
        )
