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


class DriverLicensesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        candidate_id: str,
        driver_license_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DriverLicense:
        """
        Delete an existing Driver License

        Deletes a specific driver license for a given candidate.


        DELETE /candidates/{candidate_id}/driver_licenses/{driver_license_id}

        Args:
            candidate_id: The Candidate's ID.
            driver_license_id: The Driver License ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Driver License was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.driver_licenses.delete(
            candidate_id="string", driver_license_id="string"
        )
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/candidates/{candidate_id}/driver_licenses/{driver_license_id}",
            auth_names=["basic_auth"],
            cast_to=models.DriverLicense,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        candidate_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatesDriverLicensesListResponse:
        """
        List existing Driver Licenses

        Returns a list of existing Driver Licenses for the input Candidate ID.


        GET /candidates/{candidate_id}/driver_licenses

        Args:
            candidate_id: The Candidate's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Driver Licenses

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.driver_licenses.list(candidate_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/driver_licenses",
            auth_names=["basic_auth"],
            cast_to=models.CandidatesDriverLicensesListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        candidate_id: str,
        driver_license_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DriverLicense:
        """
        Retrieve an existing Driver License

        Returns a specific driver license for a given candidate.


        GET /candidates/{candidate_id}/driver_licenses/{driver_license_id}

        Args:
            candidate_id: The Candidate's ID.
            driver_license_id: The Driver License ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Driver License details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.driver_licenses.get(
            candidate_id="string", driver_license_id="string"
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/driver_licenses/{driver_license_id}",
            auth_names=["basic_auth"],
            cast_to=models.DriverLicense,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        candidate_id: str,
        current: bool,
        number: str,
        state: str,
        issued_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DriverLicense:
        """
        Create a new Driver License

        Creates a new Driver License for a given candidate.

        If a `current` driver license is created for a candidate with an existing driver license marked `current`, the existing license will be updated to reflect that it is no longer `current`.

        If a `candidate_driver_license` exists with the `state` and `number` passed in with the POST request, a new license will not be created. The `current` and `issued_date` values of the existing license will be updated with on the parameters passed.

        **Note:** When a new driver license is created, Checkr will attempt to apply the new license information to resolve any existing exceptions for the candidate's most recent MVR screening if the screening has not yet produced reportable results.


        See [Driver License validation](#section/Reference/Driver-License-validation) in the Reference section for a list of valid driver license number input by state.


        POST /candidates/{candidate_id}/driver_licenses

        Args:
            issued_date: The issued date of the driver license.
            candidate_id: The Candidate's ID.
            current: Defines whether the driver license is the candidate's current license. `true` if the license is the candidate's current license, `false` otherwise.
            number: The driver license number.
            state: The state that issued the driver license.
            request_options: Additional options to customize the HTTP request

        Returns:
            Driver License was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.driver_licenses.create(
            candidate_id="string",
            current=True,
            number="F2222222",
            state="CA",
            issued_date="2010-01-30",
        )
        ```
        """
        _json = to_encodable(
            item={
                "issued_date": issued_date,
                "current": current,
                "number": number,
                "state": state,
            },
            dump_with=params._SerializerCandidatesDriverLicensesCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path=f"/candidates/{candidate_id}/driver_licenses",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.DriverLicense,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        candidate_id: str,
        driver_license_id: str,
        current: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        issued_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DriverLicense:
        """
        Update an existing Driver License

        Updates an existing Driver License for a given candidate.

        **Note**: Updating an existing license to `current: true` will set any existing `current` license to `current: false`.


        POST /candidates/{candidate_id}/driver_licenses/{driver_license_id}

        Args:
            current: The updated current status of the driver license. `true` if the license is the candidate's current license, `false` otherwise.
            issued_date: The updated issued date of the driver license.
            number: The updated number of the driver license.
            state: The updated state that issued the driver license.
            candidate_id: The Candidate's ID.
            driver_license_id: The Driver License ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Driver License was successfully updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.driver_licenses.update(
            candidate_id="string",
            driver_license_id="string",
            issued_date="2010-01-30",
            number="F1111111",
            state="CA",
        )
        ```
        """
        _json = to_encodable(
            item={
                "current": current,
                "issued_date": issued_date,
                "number": number,
                "state": state,
            },
            dump_with=params._SerializerCandidatesDriverLicensesUpdateBody,
        )
        return self._base_client.request(
            method="POST",
            path=f"/candidates/{candidate_id}/driver_licenses/{driver_license_id}",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.DriverLicense,
            request_options=request_options or default_request_options(),
        )


class AsyncDriverLicensesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        candidate_id: str,
        driver_license_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DriverLicense:
        """
        Delete an existing Driver License

        Deletes a specific driver license for a given candidate.


        DELETE /candidates/{candidate_id}/driver_licenses/{driver_license_id}

        Args:
            candidate_id: The Candidate's ID.
            driver_license_id: The Driver License ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Driver License was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.driver_licenses.delete(
            candidate_id="string", driver_license_id="string"
        )
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/candidates/{candidate_id}/driver_licenses/{driver_license_id}",
            auth_names=["basic_auth"],
            cast_to=models.DriverLicense,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        candidate_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatesDriverLicensesListResponse:
        """
        List existing Driver Licenses

        Returns a list of existing Driver Licenses for the input Candidate ID.


        GET /candidates/{candidate_id}/driver_licenses

        Args:
            candidate_id: The Candidate's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Driver Licenses

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.driver_licenses.list(candidate_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/driver_licenses",
            auth_names=["basic_auth"],
            cast_to=models.CandidatesDriverLicensesListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        candidate_id: str,
        driver_license_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DriverLicense:
        """
        Retrieve an existing Driver License

        Returns a specific driver license for a given candidate.


        GET /candidates/{candidate_id}/driver_licenses/{driver_license_id}

        Args:
            candidate_id: The Candidate's ID.
            driver_license_id: The Driver License ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Driver License details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.driver_licenses.get(
            candidate_id="string", driver_license_id="string"
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/driver_licenses/{driver_license_id}",
            auth_names=["basic_auth"],
            cast_to=models.DriverLicense,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        candidate_id: str,
        current: bool,
        number: str,
        state: str,
        issued_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DriverLicense:
        """
        Create a new Driver License

        Creates a new Driver License for a given candidate.

        If a `current` driver license is created for a candidate with an existing driver license marked `current`, the existing license will be updated to reflect that it is no longer `current`.

        If a `candidate_driver_license` exists with the `state` and `number` passed in with the POST request, a new license will not be created. The `current` and `issued_date` values of the existing license will be updated with on the parameters passed.

        **Note:** When a new driver license is created, Checkr will attempt to apply the new license information to resolve any existing exceptions for the candidate's most recent MVR screening if the screening has not yet produced reportable results.


        See [Driver License validation](#section/Reference/Driver-License-validation) in the Reference section for a list of valid driver license number input by state.


        POST /candidates/{candidate_id}/driver_licenses

        Args:
            issued_date: The issued date of the driver license.
            candidate_id: The Candidate's ID.
            current: Defines whether the driver license is the candidate's current license. `true` if the license is the candidate's current license, `false` otherwise.
            number: The driver license number.
            state: The state that issued the driver license.
            request_options: Additional options to customize the HTTP request

        Returns:
            Driver License was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.driver_licenses.create(
            candidate_id="string",
            current=True,
            number="F2222222",
            state="CA",
            issued_date="2010-01-30",
        )
        ```
        """
        _json = to_encodable(
            item={
                "issued_date": issued_date,
                "current": current,
                "number": number,
                "state": state,
            },
            dump_with=params._SerializerCandidatesDriverLicensesCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/candidates/{candidate_id}/driver_licenses",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.DriverLicense,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        candidate_id: str,
        driver_license_id: str,
        current: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        issued_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DriverLicense:
        """
        Update an existing Driver License

        Updates an existing Driver License for a given candidate.

        **Note**: Updating an existing license to `current: true` will set any existing `current` license to `current: false`.


        POST /candidates/{candidate_id}/driver_licenses/{driver_license_id}

        Args:
            current: The updated current status of the driver license. `true` if the license is the candidate's current license, `false` otherwise.
            issued_date: The updated issued date of the driver license.
            number: The updated number of the driver license.
            state: The updated state that issued the driver license.
            candidate_id: The Candidate's ID.
            driver_license_id: The Driver License ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Driver License was successfully updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.driver_licenses.update(
            candidate_id="string",
            driver_license_id="string",
            issued_date="2010-01-30",
            number="F1111111",
            state="CA",
        )
        ```
        """
        _json = to_encodable(
            item={
                "current": current,
                "issued_date": issued_date,
                "number": number,
                "state": state,
            },
            dump_with=params._SerializerCandidatesDriverLicensesUpdateBody,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/candidates/{candidate_id}/driver_licenses/{driver_license_id}",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.DriverLicense,
            request_options=request_options or default_request_options(),
        )
