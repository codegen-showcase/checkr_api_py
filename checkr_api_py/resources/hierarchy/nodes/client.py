import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)
from checkr_api_py.types import params


class NodesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        nodes: typing.List[params.HierarchyNode],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Add nodes to a hierarchy

        Adds new nodes to an existing Account Hierarchy.

        This endpoint creates the nodes synchronously.


        POST /hierarchy/nodes

        Args:
            nodes: typing.List[HierarchyNode]
            request_options: Additional options to customize the HTTP request

        Returns:
            Nodes were successfully added to the hierarchy

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.hierarchy.nodes.create(
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
            item={"nodes": nodes}, dump_with=params._SerializerHierarchyNodesCreateBody
        )
        return self._base_client.request(
            method="POST",
            path="/hierarchy/nodes",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=str,
            request_options=request_options or default_request_options(),
        )


class AsyncNodesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        nodes: typing.List[params.HierarchyNode],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Add nodes to a hierarchy

        Adds new nodes to an existing Account Hierarchy.

        This endpoint creates the nodes synchronously.


        POST /hierarchy/nodes

        Args:
            nodes: typing.List[HierarchyNode]
            request_options: Additional options to customize the HTTP request

        Returns:
            Nodes were successfully added to the hierarchy

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.hierarchy.nodes.create(
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
            item={"nodes": nodes}, dump_with=params._SerializerHierarchyNodesCreateBody
        )
        return await self._base_client.request(
            method="POST",
            path="/hierarchy/nodes",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=str,
            request_options=request_options or default_request_options(),
        )
