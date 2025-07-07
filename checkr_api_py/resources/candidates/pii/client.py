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


class PiiClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        deletion_contact_email_address: str,
        id: str,
        deletion_contact_first_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deletion_contact_last_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Candidate:
        """
        Request PII removal for a Candidate

        Requests the removal of PII from an existing Candidate

        Requesting the removal of PII from a candidate who has already had PII removed will result in an error.


        DELETE /candidates/{id}/pii

        Args:
            deletion_contact_first_name: First name of person requesting candidate's PII removal.
            deletion_contact_last_name: Last name of person requesting candidate's PII removal.
            deletion_contact_email_address: Email address of person requesting candidate's PII removal.
            id: The Candidate's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.pii.delete(
            deletion_contact_email_address="john.smith@gmail.com",
            id="string",
            deletion_contact_first_name="John",
            deletion_contact_last_name="Smith",
        )
        ```
        """
        _json = to_encodable(
            item={
                "deletion_contact_first_name": deletion_contact_first_name,
                "deletion_contact_last_name": deletion_contact_last_name,
                "deletion_contact_email_address": deletion_contact_email_address,
            },
            dump_with=params._SerializerCandidatesPiiDeleteBody,
        )
        return self._base_client.request(
            method="DELETE",
            path=f"/candidates/{id}/pii",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Candidate,
            request_options=request_options or default_request_options(),
        )


class AsyncPiiClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        deletion_contact_email_address: str,
        id: str,
        deletion_contact_first_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deletion_contact_last_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Candidate:
        """
        Request PII removal for a Candidate

        Requests the removal of PII from an existing Candidate

        Requesting the removal of PII from a candidate who has already had PII removed will result in an error.


        DELETE /candidates/{id}/pii

        Args:
            deletion_contact_first_name: First name of person requesting candidate's PII removal.
            deletion_contact_last_name: Last name of person requesting candidate's PII removal.
            deletion_contact_email_address: Email address of person requesting candidate's PII removal.
            id: The Candidate's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.pii.delete(
            deletion_contact_email_address="john.smith@gmail.com",
            id="string",
            deletion_contact_first_name="John",
            deletion_contact_last_name="Smith",
        )
        ```
        """
        _json = to_encodable(
            item={
                "deletion_contact_first_name": deletion_contact_first_name,
                "deletion_contact_last_name": deletion_contact_last_name,
                "deletion_contact_email_address": deletion_contact_email_address,
            },
            dump_with=params._SerializerCandidatesPiiDeleteBody,
        )
        return await self._base_client.request(
            method="DELETE",
            path=f"/candidates/{id}/pii",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Candidate,
            request_options=request_options or default_request_options(),
        )
