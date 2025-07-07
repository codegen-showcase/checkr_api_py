import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class SsnClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        candidate_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Ssn:
        """
        Get a candidate's encrypted SSN

        Returns an encrypted SSN for the input `candidate_id`.


        GET /candidates/{candidate_id}/ssn

        Args:
            candidate_id: The candidate's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate's encrypted SSN

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.ssn.list(candidate_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/ssn",
            auth_names=["basic_auth"],
            cast_to=models.Ssn,
            request_options=request_options or default_request_options(),
        )


class AsyncSsnClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        candidate_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Ssn:
        """
        Get a candidate's encrypted SSN

        Returns an encrypted SSN for the input `candidate_id`.


        GET /candidates/{candidate_id}/ssn

        Args:
            candidate_id: The candidate's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate's encrypted SSN

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.ssn.list(candidate_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/ssn",
            auth_names=["basic_auth"],
            cast_to=models.Ssn,
            request_options=request_options or default_request_options(),
        )
