import typing
import typing_extensions

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


class WorksitesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a Worksite

        Deletes specified Worksite. If there are at least one Form I-9 associated
        with a Worksite, this Worksite cannot be deleted.


        DELETE /i9/worksites/{id}

        Args:
            id: Worksite resource Id
            request_options: Additional options to customize the HTTP request

        Returns:
            Workspace successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.i9.worksites.delete(id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/i9/worksites/{id}",
            auth_names=["basic_auth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        order: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        order_by: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "city", "name", "state", "street_line1", "street_line2", "zip_code"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.I9WorksitesListResponse:
        """
        List existing Worksites

        Returns a list with all existing Worksites for the authenticated Checkr account.


        GET /i9/worksites

        Args:
            order: Returns records listed in ascending or descending order of the order_by parameter. If neither is specified, records will be listed in descending order.

            order_by: Returns records ordered by `field`.

        If neither is specified, records will not be ordered.

            request_options: Additional options to customize the HTTP request

        Returns:
            List of Worksites

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.i9.worksites.list(order="desc", order_by="street_line1")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(order, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order",
                to_encodable(
                    item=order, dump_with=typing_extensions.Literal["asc", "desc"]
                ),
                style="form",
                explode=True,
            )
        if not isinstance(order_by, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order_by",
                to_encodable(
                    item=order_by,
                    dump_with=typing_extensions.Literal[
                        "city",
                        "name",
                        "state",
                        "street_line1",
                        "street_line2",
                        "zip_code",
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/i9/worksites",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.I9WorksitesListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.WorksiteDetailed:
        """
        Retrieve a Worksite

        Returns a specified Worksite for the authenticated Checkr account.

        GET /i9/worksites/{id}

        Args:
            id: Worksite resource Id
            request_options: Additional options to customize the HTTP request

        Returns:
            Worksite details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.i9.worksites.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/i9/worksites/{id}",
            auth_names=["basic_auth"],
            cast_to=models.WorksiteDetailed,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        city: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        street_line1: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        street_line2: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        zip_code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.WorksiteDetailed:
        """
        Create new Worksite

        Create new Worksites for the authenticated account.


        POST /i9/worksites

        Args:
            city: City of Worksite.
            name: Worksite name.
            state: State of Worksite.
            street_line1: Line one of Worksite address.
            street_line2: Line two of Worksite address.
            zip_code: ZIP Code of Worksite.
            request_options: Additional options to customize the HTTP request

        Returns:
            Resource created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.i9.worksites.create(
            city="San Francisco",
            name="Head Office",
            state="CA",
            street_line1="Some Rd",
            street_line2="Some Rd 2",
            zip_code="66554",
        )
        ```
        """
        _json = to_encodable(
            item={
                "city": city,
                "name": name,
                "state": state,
                "street_line1": street_line1,
                "street_line2": street_line2,
                "zip_code": zip_code,
            },
            dump_with=params._SerializerWorksite,
        )
        return self._base_client.request(
            method="POST",
            path="/i9/worksites",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.WorksiteDetailed,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        id: str,
        city: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        everify_status: typing.Union[
            typing.Optional[typing_extensions.Literal["active", "inactive"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        street_line1: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        street_line2: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        zip_code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.I9WorksitesUpdateResponse:
        """
        Update Worksite information

        Update Worksite information


        PUT /i9/worksites/{id}

        Args:
            city: City of Worksite.
            everify_status: Worksite E-Verify Status.
            name: Worksite name.
            state: State of Worksite.
            street_line1: Line one of Worksite address.
            street_line2: Line two of Worksite address.
            zip_code: ZIP Code of Worksite.
            id: Worksite resource Id
            request_options: Additional options to customize the HTTP request

        Returns:
            Worksite successfully updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.i9.worksites.update(
            id="string",
            city="San Francisco",
            everify_status="inactive",
            name="Head Office",
            state="CA",
            street_line1="Some Rd",
            street_line2="Some Rd 2",
            zip_code="66554",
        )
        ```
        """
        _json = to_encodable(
            item={
                "city": city,
                "everify_status": everify_status,
                "name": name,
                "state": state,
                "street_line1": street_line1,
                "street_line2": street_line2,
                "zip_code": zip_code,
            },
            dump_with=params._SerializerI9WorksitesUpdateBody,
        )
        return self._base_client.request(
            method="PUT",
            path=f"/i9/worksites/{id}",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.I9WorksitesUpdateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncWorksitesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a Worksite

        Deletes specified Worksite. If there are at least one Form I-9 associated
        with a Worksite, this Worksite cannot be deleted.


        DELETE /i9/worksites/{id}

        Args:
            id: Worksite resource Id
            request_options: Additional options to customize the HTTP request

        Returns:
            Workspace successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.i9.worksites.delete(id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/i9/worksites/{id}",
            auth_names=["basic_auth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        order: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        order_by: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "city", "name", "state", "street_line1", "street_line2", "zip_code"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.I9WorksitesListResponse:
        """
        List existing Worksites

        Returns a list with all existing Worksites for the authenticated Checkr account.


        GET /i9/worksites

        Args:
            order: Returns records listed in ascending or descending order of the order_by parameter. If neither is specified, records will be listed in descending order.

            order_by: Returns records ordered by `field`.

        If neither is specified, records will not be ordered.

            request_options: Additional options to customize the HTTP request

        Returns:
            List of Worksites

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.i9.worksites.list(order="desc", order_by="street_line1")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(order, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order",
                to_encodable(
                    item=order, dump_with=typing_extensions.Literal["asc", "desc"]
                ),
                style="form",
                explode=True,
            )
        if not isinstance(order_by, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order_by",
                to_encodable(
                    item=order_by,
                    dump_with=typing_extensions.Literal[
                        "city",
                        "name",
                        "state",
                        "street_line1",
                        "street_line2",
                        "zip_code",
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/i9/worksites",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.I9WorksitesListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.WorksiteDetailed:
        """
        Retrieve a Worksite

        Returns a specified Worksite for the authenticated Checkr account.

        GET /i9/worksites/{id}

        Args:
            id: Worksite resource Id
            request_options: Additional options to customize the HTTP request

        Returns:
            Worksite details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.i9.worksites.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/i9/worksites/{id}",
            auth_names=["basic_auth"],
            cast_to=models.WorksiteDetailed,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        city: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        street_line1: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        street_line2: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        zip_code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.WorksiteDetailed:
        """
        Create new Worksite

        Create new Worksites for the authenticated account.


        POST /i9/worksites

        Args:
            city: City of Worksite.
            name: Worksite name.
            state: State of Worksite.
            street_line1: Line one of Worksite address.
            street_line2: Line two of Worksite address.
            zip_code: ZIP Code of Worksite.
            request_options: Additional options to customize the HTTP request

        Returns:
            Resource created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.i9.worksites.create(
            city="San Francisco",
            name="Head Office",
            state="CA",
            street_line1="Some Rd",
            street_line2="Some Rd 2",
            zip_code="66554",
        )
        ```
        """
        _json = to_encodable(
            item={
                "city": city,
                "name": name,
                "state": state,
                "street_line1": street_line1,
                "street_line2": street_line2,
                "zip_code": zip_code,
            },
            dump_with=params._SerializerWorksite,
        )
        return await self._base_client.request(
            method="POST",
            path="/i9/worksites",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.WorksiteDetailed,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        id: str,
        city: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        everify_status: typing.Union[
            typing.Optional[typing_extensions.Literal["active", "inactive"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        street_line1: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        street_line2: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        zip_code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.I9WorksitesUpdateResponse:
        """
        Update Worksite information

        Update Worksite information


        PUT /i9/worksites/{id}

        Args:
            city: City of Worksite.
            everify_status: Worksite E-Verify Status.
            name: Worksite name.
            state: State of Worksite.
            street_line1: Line one of Worksite address.
            street_line2: Line two of Worksite address.
            zip_code: ZIP Code of Worksite.
            id: Worksite resource Id
            request_options: Additional options to customize the HTTP request

        Returns:
            Worksite successfully updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.i9.worksites.update(
            id="string",
            city="San Francisco",
            everify_status="inactive",
            name="Head Office",
            state="CA",
            street_line1="Some Rd",
            street_line2="Some Rd 2",
            zip_code="66554",
        )
        ```
        """
        _json = to_encodable(
            item={
                "city": city,
                "everify_status": everify_status,
                "name": name,
                "state": state,
                "street_line1": street_line1,
                "street_line2": street_line2,
                "zip_code": zip_code,
            },
            dump_with=params._SerializerI9WorksitesUpdateBody,
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/i9/worksites/{id}",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.I9WorksitesUpdateResponse,
            request_options=request_options or default_request_options(),
        )
