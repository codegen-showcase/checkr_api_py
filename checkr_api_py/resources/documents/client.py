import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class DocumentsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Document:
        """
        Retrieve a Document

        Returns an existing Document with the input ID.

        Report Document IDs can be retrieved from the [Retrieve an existing Report](#operation/getReport)
        endpoint. Candidate Document IDs can be retrieved using the
        [List a Candidate's Documents](#operation/getCandidateDocuments) endpoint.


        GET /documents/{id}

        Args:
            id: ID of the Document to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Document details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.documents.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/documents/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Document,
            request_options=request_options or default_request_options(),
        )


class AsyncDocumentsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Document:
        """
        Retrieve a Document

        Returns an existing Document with the input ID.

        Report Document IDs can be retrieved from the [Retrieve an existing Report](#operation/getReport)
        endpoint. Candidate Document IDs can be retrieved using the
        [List a Candidate's Documents](#operation/getCandidateDocuments) endpoint.


        GET /documents/{id}

        Args:
            id: ID of the Document to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            Document details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.documents.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/documents/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Document,
            request_options=request_options or default_request_options(),
        )
