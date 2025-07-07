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
from checkr_api_py.types import models


class NodesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, custom_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.HierarchyNode:
        """
        Delete an existing node

        Deletes an existing node by custom_id.

        Parent nodes and nodes assigned to continuous check subscriptions or legacy
        subscriptions cannot be deleted.


        DELETE /nodes/{custom_id}

        Args:
            custom_id: custom_id of the Node.
            request_options: Additional options to customize the HTTP request

        Returns:
            Node

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.nodes.delete(custom_id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/nodes/{custom_id}",
            auth_names=["basic_auth"],
            cast_to=models.HierarchyNode,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        include: typing.Union[
            typing.Optional[typing_extensions.Literal["packages"]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        order: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        order_by: typing.Union[
            typing.Optional[typing_extensions.Literal["created_at", "custom_id"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.NodesListResponse:
        """
        List existing Nodes

        Returns a list of existing Nodes that make up the current Account Hierarchy.

        * If `include=packages` is passed, each Node object in the response will include a "packages" field. This will be an array of strings representing the slugs of the account Packages that are assigned (directly or indirectly) to the given Node. This field can be used to build UIs that truncate the list of Packages displayed to a requester, or to display only the nodes that are relevant to the requester.

        * If `include=packages` is not passed, no package information will be included in the response.

        This endpoint uses pagination; please see the corresponding [reference page](#section/Reference/Pagination) for details.


        GET /nodes

        Args:
            include: Includes a "packages" array with each Node object, containing a list of slugs for packages that are assigned to that node or its ancestors.
            order: Returns records arranged in order as specified by the `order_by` parameter. If neither is specified, records will be listed in ascending order.
            order_by: Returns records sorted by custom_id or created_at. If neither is specified, records will be sorted by created_at.
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Nodes

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.nodes.list(include="packages", order="desc", order_by="custom_id")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(include, type_utils.NotGiven):
            encode_query_param(
                _query,
                "include",
                to_encodable(
                    item=include, dump_with=typing_extensions.Literal["packages"]
                ),
                style="form",
                explode=True,
            )
        if not isinstance(order, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order",
                to_encodable(
                    item=order,
                    dump_with=typing.Optional[typing_extensions.Literal["asc", "desc"]],
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
                    dump_with=typing.Optional[
                        typing_extensions.Literal["created_at", "custom_id"]
                    ],
                ),
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
            path="/nodes",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.NodesListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        custom_id: str,
        include: typing.Union[
            typing.Optional[typing_extensions.Literal["packages"]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.HierarchyNode:
        """
        Retrieve an existing node

        Returns an existing node by custom_id.


        * If `include=packages` is passed, the response will include a "packages" field.
        This will be an array of strings representing the slugs of the account
        Packages that are assigned (directly or indirectly) to the given Node. This field can be
        used to build UIs that truncate the list of Packages displayed to a requester, or to
        display only the nodes that are relevant to the requester.


        * If `include=packages` is not passed, no package information will be included in the response.


        GET /nodes/{custom_id}

        Args:
            include: Includes a "packages" array with each Node object, containing a list of slugs for packages that are assigned to that node or its ancestors.
            custom_id: custom_id of the Node.
            request_options: Additional options to customize the HTTP request

        Returns:
            Node

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.nodes.get(custom_id="string", include="packages")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(include, type_utils.NotGiven):
            encode_query_param(
                _query,
                "include",
                to_encodable(
                    item=include, dump_with=typing_extensions.Literal["packages"]
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/nodes/{custom_id}",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.HierarchyNode,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self, *, custom_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.HierarchyNode:
        """
        Update an existing node

        Updates the name and tier on an existing node by custom_id.


        PATCH /nodes/{custom_id}

        Args:
            custom_id: custom_id of the Node.
            request_options: Additional options to customize the HTTP request

        Returns:
            Node

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.nodes.patch(custom_id="string")
        ```
        """
        return self._base_client.request(
            method="PATCH",
            path=f"/nodes/{custom_id}",
            auth_names=["basic_auth"],
            cast_to=models.HierarchyNode,
            request_options=request_options or default_request_options(),
        )


class AsyncNodesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, custom_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.HierarchyNode:
        """
        Delete an existing node

        Deletes an existing node by custom_id.

        Parent nodes and nodes assigned to continuous check subscriptions or legacy
        subscriptions cannot be deleted.


        DELETE /nodes/{custom_id}

        Args:
            custom_id: custom_id of the Node.
            request_options: Additional options to customize the HTTP request

        Returns:
            Node

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.nodes.delete(custom_id="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/nodes/{custom_id}",
            auth_names=["basic_auth"],
            cast_to=models.HierarchyNode,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        include: typing.Union[
            typing.Optional[typing_extensions.Literal["packages"]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        order: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        order_by: typing.Union[
            typing.Optional[typing_extensions.Literal["created_at", "custom_id"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.NodesListResponse:
        """
        List existing Nodes

        Returns a list of existing Nodes that make up the current Account Hierarchy.

        * If `include=packages` is passed, each Node object in the response will include a "packages" field. This will be an array of strings representing the slugs of the account Packages that are assigned (directly or indirectly) to the given Node. This field can be used to build UIs that truncate the list of Packages displayed to a requester, or to display only the nodes that are relevant to the requester.

        * If `include=packages` is not passed, no package information will be included in the response.

        This endpoint uses pagination; please see the corresponding [reference page](#section/Reference/Pagination) for details.


        GET /nodes

        Args:
            include: Includes a "packages" array with each Node object, containing a list of slugs for packages that are assigned to that node or its ancestors.
            order: Returns records arranged in order as specified by the `order_by` parameter. If neither is specified, records will be listed in ascending order.
            order_by: Returns records sorted by custom_id or created_at. If neither is specified, records will be sorted by created_at.
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Nodes

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.nodes.list(include="packages", order="desc", order_by="custom_id")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(include, type_utils.NotGiven):
            encode_query_param(
                _query,
                "include",
                to_encodable(
                    item=include, dump_with=typing_extensions.Literal["packages"]
                ),
                style="form",
                explode=True,
            )
        if not isinstance(order, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order",
                to_encodable(
                    item=order,
                    dump_with=typing.Optional[typing_extensions.Literal["asc", "desc"]],
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
                    dump_with=typing.Optional[
                        typing_extensions.Literal["created_at", "custom_id"]
                    ],
                ),
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
            path="/nodes",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.NodesListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        custom_id: str,
        include: typing.Union[
            typing.Optional[typing_extensions.Literal["packages"]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.HierarchyNode:
        """
        Retrieve an existing node

        Returns an existing node by custom_id.


        * If `include=packages` is passed, the response will include a "packages" field.
        This will be an array of strings representing the slugs of the account
        Packages that are assigned (directly or indirectly) to the given Node. This field can be
        used to build UIs that truncate the list of Packages displayed to a requester, or to
        display only the nodes that are relevant to the requester.


        * If `include=packages` is not passed, no package information will be included in the response.


        GET /nodes/{custom_id}

        Args:
            include: Includes a "packages" array with each Node object, containing a list of slugs for packages that are assigned to that node or its ancestors.
            custom_id: custom_id of the Node.
            request_options: Additional options to customize the HTTP request

        Returns:
            Node

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.nodes.get(custom_id="string", include="packages")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(include, type_utils.NotGiven):
            encode_query_param(
                _query,
                "include",
                to_encodable(
                    item=include, dump_with=typing_extensions.Literal["packages"]
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/nodes/{custom_id}",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.HierarchyNode,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self, *, custom_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.HierarchyNode:
        """
        Update an existing node

        Updates the name and tier on an existing node by custom_id.


        PATCH /nodes/{custom_id}

        Args:
            custom_id: custom_id of the Node.
            request_options: Additional options to customize the HTTP request

        Returns:
            Node

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.nodes.patch(custom_id="string")
        ```
        """
        return await self._base_client.request(
            method="PATCH",
            path=f"/nodes/{custom_id}",
            auth_names=["basic_auth"],
            cast_to=models.HierarchyNode,
            request_options=request_options or default_request_options(),
        )
