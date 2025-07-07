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


class SubscriptionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.SubscriptionCanceled:
        """
        Cancel an existing Subscription

        Cancels an existing Subscription.


        DELETE /subscriptions/{id}

        Args:
            id: ID of the Subscription.
            request_options: Additional options to customize the HTTP request

        Returns:
            Subscription was successfully canceled

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscriptions.delete(id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/subscriptions/{id}",
            auth_names=["basic_auth"],
            cast_to=models.SubscriptionCanceled,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        candidate_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["active", "inactive"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionsListResponse:
        """
        List existing Subscriptions

        Lists existing Subscriptions with the input parameters.

        GET /subscriptions

        Args:
            candidate_id: ID of the candidate to search for subscriptions.
            created_after: Returns subscriptions created after the input date.
            created_before: Returns subscriptions created before the input date.
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            status: Returns subscriptions with the input status.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Subscriptions

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscriptions.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(candidate_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "candidate_id",
                to_encodable(item=candidate_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(created_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created_after",
                to_encodable(item=created_after, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(created_before, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created_before",
                to_encodable(item=created_before, dump_with=str),
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
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal["active", "inactive"],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/subscriptions",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.SubscriptionsListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Subscription:
        """
        Retrieve an existing Subscription

        Retrieves an existing Subscription.


        GET /subscriptions/{id}

        Args:
            id: ID of the Subscription.
            request_options: Additional options to customize the HTTP request

        Returns:
            Subscription details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscriptions.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/subscriptions/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        candidate_id: str,
        package: str,
        start_date: str,
        interval_count: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        interval_unit: typing.Union[
            typing.Optional[typing_extensions.Literal["day", "month", "week", "year"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        node: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        work_locations: typing.Union[
            typing.Optional[typing.List[params.WorkLocation]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Create a new Subscription

        Creates a new Subscription.

        <b>Notes for International Customers: </b>Subscriptions are not available for reports which include international packages.
        If your candidate is located outside the US, you may not create a Subscription for them.


        POST /subscriptions

        Args:
            interval_count: The number of intervals between each recurrent background check.
            interval_unit: Interval at which the subscription will repeat.
            node: <font color="red">Required</font> for hierarchy-enabled accounts.

        `custom_id` of the associated node.

            work_locations: <font color="red">Required</font> for hierarchy-enabled accounts.
        Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.

            candidate_id: ID of the candidate being screened.
            package: `slug` of the associated package.

            start_date: Start date for the subscription. This is the date on which the subscription will begin, and the first time the report will be run.
            request_options: Additional options to customize the HTTP request

        Returns:
            Subscription was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscriptions.create(
            candidate_id="string", package="string", start_date="1970-01-01"
        )
        ```
        """
        _json = to_encodable(
            item={
                "interval_count": interval_count,
                "interval_unit": interval_unit,
                "node": node,
                "work_locations": work_locations,
                "candidate_id": candidate_id,
                "package": package,
                "start_date": start_date,
            },
            dump_with=params._SerializerSubscriptionsCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/subscriptions",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        id: str,
        candidate_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        interval_count: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        interval_unit: typing.Union[
            typing.Optional[typing_extensions.Literal["day", "month", "week", "year"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        node: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        package: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        start_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        work_locations: typing.Union[
            typing.Optional[typing.List[params.WorkLocation]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Update a Subscription

        Updates a Subscription. Specify only those parameters you wish to change.


        POST /subscriptions/{id}

        Args:
            candidate_id: ID of the candidate being screened.
            interval_count: The number of intervals between each recurrent background check.
            interval_unit: Interval at which the subscription will repeat.
            node: `custom_id` of the associated node.

            package: Package to run for the Report.
            start_date: Start date for the subscription. This is the date on which the subscription will begin, and the first time the report will be run.
            work_locations: Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.

            id: ID of the Subscription.
            request_options: Additional options to customize the HTTP request

        Returns:
            Subscription was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscriptions.update(id="string")
        ```
        """
        _json = to_encodable(
            item={
                "candidate_id": candidate_id,
                "interval_count": interval_count,
                "interval_unit": interval_unit,
                "node": node,
                "package": package,
                "start_date": start_date,
                "work_locations": work_locations,
            },
            dump_with=params._SerializerSubscriptionsUpdateBody,
        )
        return self._base_client.request(
            method="POST",
            path=f"/subscriptions/{id}",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )


class AsyncSubscriptionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.SubscriptionCanceled:
        """
        Cancel an existing Subscription

        Cancels an existing Subscription.


        DELETE /subscriptions/{id}

        Args:
            id: ID of the Subscription.
            request_options: Additional options to customize the HTTP request

        Returns:
            Subscription was successfully canceled

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscriptions.delete(id="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/subscriptions/{id}",
            auth_names=["basic_auth"],
            cast_to=models.SubscriptionCanceled,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        candidate_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["active", "inactive"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionsListResponse:
        """
        List existing Subscriptions

        Lists existing Subscriptions with the input parameters.

        GET /subscriptions

        Args:
            candidate_id: ID of the candidate to search for subscriptions.
            created_after: Returns subscriptions created after the input date.
            created_before: Returns subscriptions created before the input date.
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            status: Returns subscriptions with the input status.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Subscriptions

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscriptions.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(candidate_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "candidate_id",
                to_encodable(item=candidate_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(created_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created_after",
                to_encodable(item=created_after, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(created_before, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created_before",
                to_encodable(item=created_before, dump_with=str),
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
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal["active", "inactive"],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/subscriptions",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.SubscriptionsListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Subscription:
        """
        Retrieve an existing Subscription

        Retrieves an existing Subscription.


        GET /subscriptions/{id}

        Args:
            id: ID of the Subscription.
            request_options: Additional options to customize the HTTP request

        Returns:
            Subscription details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscriptions.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/subscriptions/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        candidate_id: str,
        package: str,
        start_date: str,
        interval_count: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        interval_unit: typing.Union[
            typing.Optional[typing_extensions.Literal["day", "month", "week", "year"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        node: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        work_locations: typing.Union[
            typing.Optional[typing.List[params.WorkLocation]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Create a new Subscription

        Creates a new Subscription.

        <b>Notes for International Customers: </b>Subscriptions are not available for reports which include international packages.
        If your candidate is located outside the US, you may not create a Subscription for them.


        POST /subscriptions

        Args:
            interval_count: The number of intervals between each recurrent background check.
            interval_unit: Interval at which the subscription will repeat.
            node: <font color="red">Required</font> for hierarchy-enabled accounts.

        `custom_id` of the associated node.

            work_locations: <font color="red">Required</font> for hierarchy-enabled accounts.
        Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.

            candidate_id: ID of the candidate being screened.
            package: `slug` of the associated package.

            start_date: Start date for the subscription. This is the date on which the subscription will begin, and the first time the report will be run.
            request_options: Additional options to customize the HTTP request

        Returns:
            Subscription was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscriptions.create(
            candidate_id="string", package="string", start_date="1970-01-01"
        )
        ```
        """
        _json = to_encodable(
            item={
                "interval_count": interval_count,
                "interval_unit": interval_unit,
                "node": node,
                "work_locations": work_locations,
                "candidate_id": candidate_id,
                "package": package,
                "start_date": start_date,
            },
            dump_with=params._SerializerSubscriptionsCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/subscriptions",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        id: str,
        candidate_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        interval_count: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        interval_unit: typing.Union[
            typing.Optional[typing_extensions.Literal["day", "month", "week", "year"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        node: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        package: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        start_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        work_locations: typing.Union[
            typing.Optional[typing.List[params.WorkLocation]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Update a Subscription

        Updates a Subscription. Specify only those parameters you wish to change.


        POST /subscriptions/{id}

        Args:
            candidate_id: ID of the candidate being screened.
            interval_count: The number of intervals between each recurrent background check.
            interval_unit: Interval at which the subscription will repeat.
            node: `custom_id` of the associated node.

            package: Package to run for the Report.
            start_date: Start date for the subscription. This is the date on which the subscription will begin, and the first time the report will be run.
            work_locations: Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.

            id: ID of the Subscription.
            request_options: Additional options to customize the HTTP request

        Returns:
            Subscription was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscriptions.update(id="string")
        ```
        """
        _json = to_encodable(
            item={
                "candidate_id": candidate_id,
                "interval_count": interval_count,
                "interval_unit": interval_unit,
                "node": node,
                "package": package,
                "start_date": start_date,
                "work_locations": work_locations,
            },
            dump_with=params._SerializerSubscriptionsUpdateBody,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/subscriptions/{id}",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )
