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
from checkr_api_py.types import models, params


class GeosClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Geo:
        """
        Delete an existing Geo

        Deletes an existing Geo.


        DELETE /geos/{id}

        Args:
            id: ID of the Geo.
            request_options: Additional options to customize the HTTP request

        Returns:
            Geo was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.geos.delete(id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/geos/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Geo,
            request_options=request_options or default_request_options(),
        )

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
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GeosListResponse:
        """
        List existing Geos

        Returns a list of existing Geos with the input `name` or `state`.


        GET /geos

        Args:
            name: Returns all Geos with the input `name`.
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            state: Returns all Geos with the input state.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Geos

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.geos.list()
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
        if not isinstance(state, type_utils.NotGiven):
            encode_query_param(
                _query,
                "state",
                to_encodable(item=state, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/geos",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.GeosListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Geo:
        """
        Retrieve an existing Geo

        Returns an existing Geo with the input ID.


        GET /geos/{id}

        Args:
            id: ID of the Geo.
            request_options: Additional options to customize the HTTP request

        Returns:
            Geo details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.geos.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/geos/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Geo,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        name: str,
        state: str,
        city: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Geo:
        """
        Create a new Geo

        Creates a new Geo resource.

        **Note**: Attempting to create a new Geo with the same name/state combination will result in an
        409 error


        POST /geos

        Args:
            city: A major city within the input state.
            name: Human-readable name of the Geo.
            state: US state for the Geo.
            request_options: Additional options to customize the HTTP request

        Returns:
            Geo was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.geos.create(name="San Francisco", state="CA", city="San Francisco")
        ```
        """
        _json = to_encodable(
            item={"city": city, "name": name, "state": state},
            dump_with=params._SerializerGeosCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/geos",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Geo,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        id: str,
        city: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Geo:
        """
        Update an existing Geo

        Updates an existing Geo resource with the input `city`.
        `city` can only be added once.


        POST /geos/{id}

        Args:
            city: Updates the Geo with the input city.
            id: ID of the Geo.
            request_options: Additional options to customize the HTTP request

        Returns:
            Geo was successfully updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.geos.update(id="string", city="San Francisco")
        ```
        """
        _json = to_encodable(
            item={"city": city}, dump_with=params._SerializerGeosUpdateBody
        )
        return self._base_client.request(
            method="POST",
            path=f"/geos/{id}",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Geo,
            request_options=request_options or default_request_options(),
        )


class AsyncGeosClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Geo:
        """
        Delete an existing Geo

        Deletes an existing Geo.


        DELETE /geos/{id}

        Args:
            id: ID of the Geo.
            request_options: Additional options to customize the HTTP request

        Returns:
            Geo was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.geos.delete(id="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/geos/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Geo,
            request_options=request_options or default_request_options(),
        )

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
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GeosListResponse:
        """
        List existing Geos

        Returns a list of existing Geos with the input `name` or `state`.


        GET /geos

        Args:
            name: Returns all Geos with the input `name`.
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            state: Returns all Geos with the input state.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Geos

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.geos.list()
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
        if not isinstance(state, type_utils.NotGiven):
            encode_query_param(
                _query,
                "state",
                to_encodable(item=state, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/geos",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.GeosListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Geo:
        """
        Retrieve an existing Geo

        Returns an existing Geo with the input ID.


        GET /geos/{id}

        Args:
            id: ID of the Geo.
            request_options: Additional options to customize the HTTP request

        Returns:
            Geo details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.geos.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/geos/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Geo,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        name: str,
        state: str,
        city: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Geo:
        """
        Create a new Geo

        Creates a new Geo resource.

        **Note**: Attempting to create a new Geo with the same name/state combination will result in an
        409 error


        POST /geos

        Args:
            city: A major city within the input state.
            name: Human-readable name of the Geo.
            state: US state for the Geo.
            request_options: Additional options to customize the HTTP request

        Returns:
            Geo was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.geos.create(name="San Francisco", state="CA", city="San Francisco")
        ```
        """
        _json = to_encodable(
            item={"city": city, "name": name, "state": state},
            dump_with=params._SerializerGeosCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/geos",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Geo,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        id: str,
        city: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Geo:
        """
        Update an existing Geo

        Updates an existing Geo resource with the input `city`.
        `city` can only be added once.


        POST /geos/{id}

        Args:
            city: Updates the Geo with the input city.
            id: ID of the Geo.
            request_options: Additional options to customize the HTTP request

        Returns:
            Geo was successfully updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.geos.update(id="string", city="San Francisco")
        ```
        """
        _json = to_encodable(
            item={"city": city}, dump_with=params._SerializerGeosUpdateBody
        )
        return await self._base_client.request(
            method="POST",
            path=f"/geos/{id}",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Geo,
            request_options=request_options or default_request_options(),
        )
