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


class CountiesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        states: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CountiesListResponse:
        """
        Get Counties by State(s)

        Returns a list of all counties for the input state(s). If no state is provided with the query, returns a list of all counties in the United States.


        GET /counties

        Args:
            states: A comma-separated list of states' Federal Information Processing Series (FIPS) values to query.
            request_options: Additional options to customize the HTTP request

        Returns:
            Counties by State

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.counties.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(states, type_utils.NotGiven):
            encode_query_param(
                _query,
                "states",
                to_encodable(item=states, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/counties",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.CountiesListResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncCountiesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        states: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CountiesListResponse:
        """
        Get Counties by State(s)

        Returns a list of all counties for the input state(s). If no state is provided with the query, returns a list of all counties in the United States.


        GET /counties

        Args:
            states: A comma-separated list of states' Federal Information Processing Series (FIPS) values to query.
            request_options: Additional options to customize the HTTP request

        Returns:
            Counties by State

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.counties.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(states, type_utils.NotGiven):
            encode_query_param(
                _query,
                "states",
                to_encodable(item=states, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/counties",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.CountiesListResponse,
            request_options=request_options or default_request_options(),
        )
