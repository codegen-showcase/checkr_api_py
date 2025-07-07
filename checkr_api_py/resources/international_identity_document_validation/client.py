import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class InternationalIdentityDocumentValidationClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.InternationalIdentityDocumentValidation:
        """
        Retrieve an existing International Identity Document Validation

        Returns an existing International Identity Document Validation with the input ID.


        GET /international_identity_document_validation/{id}

        Args:
            id: ID of the International Identity Document Validation to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            International Identity Document Validation details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.international_identity_document_validation.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/international_identity_document_validation/{id}",
            auth_names=["basic_auth"],
            cast_to=models.InternationalIdentityDocumentValidation,
            request_options=request_options or default_request_options(),
        )


class AsyncInternationalIdentityDocumentValidationClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.InternationalIdentityDocumentValidation:
        """
        Retrieve an existing International Identity Document Validation

        Returns an existing International Identity Document Validation with the input ID.


        GET /international_identity_document_validation/{id}

        Args:
            id: ID of the International Identity Document Validation to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            International Identity Document Validation details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.international_identity_document_validation.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/international_identity_document_validation/{id}",
            auth_names=["basic_auth"],
            cast_to=models.InternationalIdentityDocumentValidation,
            request_options=request_options or default_request_options(),
        )
