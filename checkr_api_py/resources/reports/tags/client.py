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


class TagsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        id: str,
        tag: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportsTagsDeleteResponse:
        """
        Delete a tag from a Report

        This request is used to delete a tag from a Report.


        DELETE /reports/{id}/tags

        Args:
            id: The Report's ID.
            tag: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Report tags were successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.tags.delete(id="string", tag="West Coast")
        ```
        """
        _json = to_encodable(
            item={"tag": tag}, dump_with=params._SerializerReportsTagsDeleteBody
        )
        return self._base_client.request(
            method="DELETE",
            path=f"/reports/{id}/tags",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.ReportsTagsDeleteResponse,
            request_options=request_options or default_request_options(),
        )

    def list(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ReportTags:
        """
        Retrieve tags for a Report

        Retrieves tags for the input Report.


        GET /reports/{id}/tags

        Args:
            id: The Report's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of report tags.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.tags.list(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/reports/{id}/tags",
            auth_names=["basic_auth"],
            cast_to=models.ReportTags,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        id: str,
        tag: str,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportsTagsCreateResponse:
        """
        Add a tag to a Report

        This request is used to add a tag to a Report.
        <p><b>Note: </b>The <code>tag</code> value passed to <code>POST /v1/reports/{id}/tags</code> will match the <code>name</code> field in the response.</p>


        POST /reports/{id}/tags

        Args:
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            id: The Report's ID.
            tag: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Report tag was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.tags.create(id="string", tag="To Review")
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
        _json = to_encodable(
            item={"tag": tag}, dump_with=params._SerializerReportsTagsCreateBody
        )
        return self._base_client.request(
            method="POST",
            path=f"/reports/{id}/tags",
            auth_names=["basic_auth"],
            query_params=_query,
            json=_json,
            cast_to=models.ReportsTagsCreateResponse,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        id: str,
        tags: typing.List[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportsTagsUpdateResponse:
        """
        Update tags for a Report

        This request is used to define all tags for a Report.


        PUT /reports/{id}/tags

        Args:
            id: The Report's ID.
            tags: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            Report tags were successfully updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.tags.update(id="string", tags=["To Review"])
        ```
        """
        _json = to_encodable(
            item={"tags": tags}, dump_with=params._SerializerReportsTagsUpdateBody
        )
        return self._base_client.request(
            method="PUT",
            path=f"/reports/{id}/tags",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.ReportsTagsUpdateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncTagsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        id: str,
        tag: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportsTagsDeleteResponse:
        """
        Delete a tag from a Report

        This request is used to delete a tag from a Report.


        DELETE /reports/{id}/tags

        Args:
            id: The Report's ID.
            tag: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Report tags were successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.tags.delete(id="string", tag="West Coast")
        ```
        """
        _json = to_encodable(
            item={"tag": tag}, dump_with=params._SerializerReportsTagsDeleteBody
        )
        return await self._base_client.request(
            method="DELETE",
            path=f"/reports/{id}/tags",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.ReportsTagsDeleteResponse,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ReportTags:
        """
        Retrieve tags for a Report

        Retrieves tags for the input Report.


        GET /reports/{id}/tags

        Args:
            id: The Report's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of report tags.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.tags.list(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/reports/{id}/tags",
            auth_names=["basic_auth"],
            cast_to=models.ReportTags,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        id: str,
        tag: str,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportsTagsCreateResponse:
        """
        Add a tag to a Report

        This request is used to add a tag to a Report.
        <p><b>Note: </b>The <code>tag</code> value passed to <code>POST /v1/reports/{id}/tags</code> will match the <code>name</code> field in the response.</p>


        POST /reports/{id}/tags

        Args:
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            id: The Report's ID.
            tag: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Report tag was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.tags.create(id="string", tag="To Review")
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
        _json = to_encodable(
            item={"tag": tag}, dump_with=params._SerializerReportsTagsCreateBody
        )
        return await self._base_client.request(
            method="POST",
            path=f"/reports/{id}/tags",
            auth_names=["basic_auth"],
            query_params=_query,
            json=_json,
            cast_to=models.ReportsTagsCreateResponse,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        id: str,
        tags: typing.List[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportsTagsUpdateResponse:
        """
        Update tags for a Report

        This request is used to define all tags for a Report.


        PUT /reports/{id}/tags

        Args:
            id: The Report's ID.
            tags: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            Report tags were successfully updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.tags.update(id="string", tags=["To Review"])
        ```
        """
        _json = to_encodable(
            item={"tags": tags}, dump_with=params._SerializerReportsTagsUpdateBody
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/reports/{id}/tags",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.ReportsTagsUpdateResponse,
            request_options=request_options or default_request_options(),
        )
