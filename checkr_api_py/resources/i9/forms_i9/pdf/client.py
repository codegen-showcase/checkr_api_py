import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)


class PdfClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Retrieve Form I-9 PDF file

        Retrieves a Form I-9 PDF file associated with the Form I-9 ID.

        This endpoint returns a pre-signed S3 URL, valid for 5 minutes.


        GET /i9/forms_i9/{id}/pdf

        Args:
            id: ID of the Form I9
            request_options: Additional options to customize the HTTP request

        Returns:
            PDF URL

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.i9.forms_i9.pdf.list(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/i9/forms_i9/{id}/pdf",
            auth_names=["basic_auth"],
            cast_to=str,
            request_options=request_options or default_request_options(),
        )


class AsyncPdfClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Retrieve Form I-9 PDF file

        Retrieves a Form I-9 PDF file associated with the Form I-9 ID.

        This endpoint returns a pre-signed S3 URL, valid for 5 minutes.


        GET /i9/forms_i9/{id}/pdf

        Args:
            id: ID of the Form I9
            request_options: Additional options to customize the HTTP request

        Returns:
            PDF URL

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.i9.forms_i9.pdf.list(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/i9/forms_i9/{id}/pdf",
            auth_names=["basic_auth"],
            cast_to=str,
            request_options=request_options or default_request_options(),
        )
