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
from checkr_api_py.resources.hierarchy.nodes import AsyncNodesClient, NodesClient
from checkr_api_py.resources.hierarchy.status import AsyncStatusClient, StatusClient
from checkr_api_py.types import models, params


class HierarchyClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.status = StatusClient(base_client=self._base_client)
        self.nodes = NodesClient(base_client=self._base_client)

    def list(
        self,
        *,
        node_custom_ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.HierarchyListResponse:
        """
        Retrieve Hierarchy (Deprecated)

        **Note:** This endpoint is _deprecated_ and will no longer be supported. Please use the new [List existing Nodes](#operation/nodesList) endpoint instead.

        Retrieves the current Hierarchy for the Account.

        Returns the account hierarchy in its entirety, or from a specific node to its children. The returned JSON object will include the Packages assigned to each node in the dashboard. This is useful for building UIs that truncate the list of Packages displayed to a requester, or display only the nodes that are relevant to the requester.

        Output is arranged hierarchically, with child nodes accessible through the parent node. Customers without large hierarchy mode enabled who do not specify pagination parameters will be returned the entire hierarchy. Customers with large hierarchy mode enabled and pagination parameters specified in this request will be returned the given page and number of results per page. If pagination parameters are not included, only the first page of the hierarchy will be returned.

        **Note:** Customers with large hierarchy mode enabled will see a different response. Please reach out to clients@checkr.com if you have any questions.


        GET /hierarchy

        Args:
            node_custom_ids: An array of `custom_ids` for the nodes to return. Returns the portion(s) of the Account Hierarchy matching the input nodes and their descendants.
            page: Specifies the page to retrieve. The default page is 1.
            per_page: Indicates how many nodes each page should contain. The default per_page value is 20.
            request_options: Additional options to customize the HTTP request

        Returns:
            The hierarchy for the account.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.hierarchy.list()
        ```
        """
        models.HierarchyListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(node_custom_ids, type_utils.NotGiven):
            encode_query_param(
                _query,
                "node_custom_ids",
                to_encodable(item=node_custom_ids, dump_with=typing.List[str]),
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
            path="/hierarchy",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.HierarchyListResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        nodes: typing.List[params.HierarchyNode],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.HierarchyCreateResponse:
        """
        Create Hierarchy

        Creates a new or replaces an existing Account Hierarchy.

        The Hierarchy endpoint performs ingestion asynchronously. Check the status
        of the ingestion by calling `GET /v1/hierarchy/status`. Once ingested, use the Checkr Dashboard to assign your nodes to Packages, PAMs, and Users.


        POST /hierarchy

        Args:
            nodes: typing.List[HierarchyNode]
            request_options: Additional options to customize the HTTP request

        Returns:
            Ingestion successfully initiated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.hierarchy.create(
            nodes=[
                {
                    "custom_id": "zpy8orej4r614ize",
                    "name": "Acme Staffing",
                    "packages": ["driver_pro", "tasker_pro"],
                    "parent_custom_id": "parent custom id",
                    "tier": "department",
                }
            ]
        )
        ```
        """
        _json = to_encodable(
            item={"nodes": nodes}, dump_with=params._SerializerHierarchyCreateBody
        )
        return self._base_client.request(
            method="POST",
            path="/hierarchy",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.HierarchyCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncHierarchyClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.status = AsyncStatusClient(base_client=self._base_client)
        self.nodes = AsyncNodesClient(base_client=self._base_client)

    async def list(
        self,
        *,
        node_custom_ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.HierarchyListResponse:
        """
        Retrieve Hierarchy (Deprecated)

        **Note:** This endpoint is _deprecated_ and will no longer be supported. Please use the new [List existing Nodes](#operation/nodesList) endpoint instead.

        Retrieves the current Hierarchy for the Account.

        Returns the account hierarchy in its entirety, or from a specific node to its children. The returned JSON object will include the Packages assigned to each node in the dashboard. This is useful for building UIs that truncate the list of Packages displayed to a requester, or display only the nodes that are relevant to the requester.

        Output is arranged hierarchically, with child nodes accessible through the parent node. Customers without large hierarchy mode enabled who do not specify pagination parameters will be returned the entire hierarchy. Customers with large hierarchy mode enabled and pagination parameters specified in this request will be returned the given page and number of results per page. If pagination parameters are not included, only the first page of the hierarchy will be returned.

        **Note:** Customers with large hierarchy mode enabled will see a different response. Please reach out to clients@checkr.com if you have any questions.


        GET /hierarchy

        Args:
            node_custom_ids: An array of `custom_ids` for the nodes to return. Returns the portion(s) of the Account Hierarchy matching the input nodes and their descendants.
            page: Specifies the page to retrieve. The default page is 1.
            per_page: Indicates how many nodes each page should contain. The default per_page value is 20.
            request_options: Additional options to customize the HTTP request

        Returns:
            The hierarchy for the account.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.hierarchy.list()
        ```
        """
        models.HierarchyListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(node_custom_ids, type_utils.NotGiven):
            encode_query_param(
                _query,
                "node_custom_ids",
                to_encodable(item=node_custom_ids, dump_with=typing.List[str]),
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
            path="/hierarchy",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.HierarchyListResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        nodes: typing.List[params.HierarchyNode],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.HierarchyCreateResponse:
        """
        Create Hierarchy

        Creates a new or replaces an existing Account Hierarchy.

        The Hierarchy endpoint performs ingestion asynchronously. Check the status
        of the ingestion by calling `GET /v1/hierarchy/status`. Once ingested, use the Checkr Dashboard to assign your nodes to Packages, PAMs, and Users.


        POST /hierarchy

        Args:
            nodes: typing.List[HierarchyNode]
            request_options: Additional options to customize the HTTP request

        Returns:
            Ingestion successfully initiated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.hierarchy.create(
            nodes=[
                {
                    "custom_id": "zpy8orej4r614ize",
                    "name": "Acme Staffing",
                    "packages": ["driver_pro", "tasker_pro"],
                    "parent_custom_id": "parent custom id",
                    "tier": "department",
                }
            ]
        )
        ```
        """
        _json = to_encodable(
            item={"nodes": nodes}, dump_with=params._SerializerHierarchyCreateBody
        )
        return await self._base_client.request(
            method="POST",
            path="/hierarchy",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.HierarchyCreateResponse,
            request_options=request_options or default_request_options(),
        )
