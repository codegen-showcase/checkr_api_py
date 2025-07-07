import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from checkr_api_py.types import models, params


class PostalAddressClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        candidate_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatePostalAddress:
        """
        Get the Candidate's Postal Addresses

        Returns the Postal Address of a given candidate.


        GET /candidates/{candidate_id}/postal_address

        Args:
            candidate_id: The candidate's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate postal address

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.postal_address.list(candidate_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/postal_address",
            auth_names=["basic_auth"],
            cast_to=models.CandidatePostalAddress,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        candidate_id: str,
        data: typing.Union[
            typing.Optional[params.CandidatesPostalAddressCreateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatePostalAddress:
        """
        Create a new Postal Address

        Creates a new Postal Address for a given candidate.


        POST /candidates/{candidate_id}/postal_address

        Args:
            data: CandidatesPostalAddressCreateBody
            candidate_id: The candidate's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate Postal Address was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.postal_address.create(candidate_id="string")
        ```
        """
        _json = (
            to_encodable(
                item=data, dump_with=params._SerializerCandidatesPostalAddressCreateBody
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/candidates/{candidate_id}/postal_address",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.CandidatePostalAddress,
            request_options=request_options or default_request_options(),
        )


class AsyncPostalAddressClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        candidate_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatePostalAddress:
        """
        Get the Candidate's Postal Addresses

        Returns the Postal Address of a given candidate.


        GET /candidates/{candidate_id}/postal_address

        Args:
            candidate_id: The candidate's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate postal address

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.postal_address.list(candidate_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/postal_address",
            auth_names=["basic_auth"],
            cast_to=models.CandidatePostalAddress,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        candidate_id: str,
        data: typing.Union[
            typing.Optional[params.CandidatesPostalAddressCreateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatePostalAddress:
        """
        Create a new Postal Address

        Creates a new Postal Address for a given candidate.


        POST /candidates/{candidate_id}/postal_address

        Args:
            data: CandidatesPostalAddressCreateBody
            candidate_id: The candidate's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate Postal Address was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.postal_address.create(candidate_id="string")
        ```
        """
        _json = (
            to_encodable(
                item=data, dump_with=params._SerializerCandidatesPostalAddressCreateBody
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/candidates/{candidate_id}/postal_address",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.CandidatePostalAddress,
            request_options=request_options or default_request_options(),
        )
