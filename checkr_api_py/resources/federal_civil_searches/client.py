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


class FederalCivilSearchesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        id: str,
        exclude: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FederalCivilSearch:
        """
        Retrieve an existing Federal Civil Search

        Returns an existing Federal Civil Search with the input ID.


        GET /federal_civil_searches/{id}

        Args:
            exclude: Indicates whether to return district screenings in pointer search payload
            id: ID of the Federal Civil Search to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Federal Civil Search details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.federal_civil_searches.get(id="string", exclude="district")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(exclude, type_utils.NotGiven):
            encode_query_param(
                _query,
                "exclude",
                to_encodable(item=exclude, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/federal_civil_searches/{id}",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.FederalCivilSearch,
            request_options=request_options or default_request_options(),
        )


class AsyncFederalCivilSearchesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        id: str,
        exclude: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FederalCivilSearch:
        """
        Retrieve an existing Federal Civil Search

        Returns an existing Federal Civil Search with the input ID.


        GET /federal_civil_searches/{id}

        Args:
            exclude: Indicates whether to return district screenings in pointer search payload
            id: ID of the Federal Civil Search to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Federal Civil Search details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.federal_civil_searches.get(id="string", exclude="district")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(exclude, type_utils.NotGiven):
            encode_query_param(
                _query,
                "exclude",
                to_encodable(item=exclude, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/federal_civil_searches/{id}",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.FederalCivilSearch,
            request_options=request_options or default_request_options(),
        )
