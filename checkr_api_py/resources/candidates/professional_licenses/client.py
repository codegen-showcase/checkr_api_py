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


class ProfessionalLicensesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        candidate_id: str,
        license_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatesProfessionalLicensesDeleteResponse:
        """
        Delete an existing Professional License

        Deletes an existing Professional License


        DELETE /candidates/{candidate_id}/professional_licenses/{license_id}

        Args:
            candidate_id: The Candidate's ID
            license_id: The ID of the license to delete.
            request_options: Additional options to customize the HTTP request

        Returns:
            Professional License was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.professional_licenses.delete(
            candidate_id="string", license_id="string"
        )
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/candidates/{candidate_id}/professional_licenses/{license_id}",
            auth_names=["basic_auth"],
            cast_to=models.CandidatesProfessionalLicensesDeleteResponse,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        candidate_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatesProfessionalLicensesListResponse:
        """
        List existing Professional Licenses

        Returns a list of existing Professional Licenses for the given Candidate ID.


        GET /candidates/{candidate_id}/professional_licenses

        Args:
            candidate_id: The Candidate's ID
            request_options: Additional options to customize the HTTP request

        Returns:
            List of existing Professional Licenses for candidate

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.professional_licenses.list(candidate_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/professional_licenses",
            auth_names=["basic_auth"],
            cast_to=models.CandidatesProfessionalLicensesListResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        candidate_id: str,
        data: typing.Union[
            typing.Optional[params.CandidatesProfessionalLicensesCreateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ProfessionalLicense:
        """
        Create a new Professional License

        Creates a new Professional License for a given candidate. A maximum of two licenses may exist for each candidate. When a report is run with [Professional License Verification](#tag/Professional-License-Verification), all candidate licenses existing at the time of report creation will be included for verification.


        POST /candidates/{candidate_id}/professional_licenses

        Args:
            data: CandidatesProfessionalLicensesCreateBody
            candidate_id: The Candidate's ID
            request_options: Additional options to customize the HTTP request

        Returns:
            Professional License was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.professional_licenses.create(candidate_id="string")
        ```
        """
        _json = (
            to_encodable(
                item=data,
                dump_with=params._SerializerCandidatesProfessionalLicensesCreateBody,
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/candidates/{candidate_id}/professional_licenses",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.ProfessionalLicense,
            request_options=request_options or default_request_options(),
        )


class AsyncProfessionalLicensesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        candidate_id: str,
        license_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatesProfessionalLicensesDeleteResponse:
        """
        Delete an existing Professional License

        Deletes an existing Professional License


        DELETE /candidates/{candidate_id}/professional_licenses/{license_id}

        Args:
            candidate_id: The Candidate's ID
            license_id: The ID of the license to delete.
            request_options: Additional options to customize the HTTP request

        Returns:
            Professional License was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.professional_licenses.delete(
            candidate_id="string", license_id="string"
        )
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/candidates/{candidate_id}/professional_licenses/{license_id}",
            auth_names=["basic_auth"],
            cast_to=models.CandidatesProfessionalLicensesDeleteResponse,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        candidate_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatesProfessionalLicensesListResponse:
        """
        List existing Professional Licenses

        Returns a list of existing Professional Licenses for the given Candidate ID.


        GET /candidates/{candidate_id}/professional_licenses

        Args:
            candidate_id: The Candidate's ID
            request_options: Additional options to customize the HTTP request

        Returns:
            List of existing Professional Licenses for candidate

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.professional_licenses.list(candidate_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/professional_licenses",
            auth_names=["basic_auth"],
            cast_to=models.CandidatesProfessionalLicensesListResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        candidate_id: str,
        data: typing.Union[
            typing.Optional[params.CandidatesProfessionalLicensesCreateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ProfessionalLicense:
        """
        Create a new Professional License

        Creates a new Professional License for a given candidate. A maximum of two licenses may exist for each candidate. When a report is run with [Professional License Verification](#tag/Professional-License-Verification), all candidate licenses existing at the time of report creation will be included for verification.


        POST /candidates/{candidate_id}/professional_licenses

        Args:
            data: CandidatesProfessionalLicensesCreateBody
            candidate_id: The Candidate's ID
            request_options: Additional options to customize the HTTP request

        Returns:
            Professional License was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.professional_licenses.create(candidate_id="string")
        ```
        """
        _json = (
            to_encodable(
                item=data,
                dump_with=params._SerializerCandidatesProfessionalLicensesCreateBody,
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/candidates/{candidate_id}/professional_licenses",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.ProfessionalLicense,
            request_options=request_options or default_request_options(),
        )
