import typing
import typing_extensions

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from checkr_api_py.types import models, params


class SchoolsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        candidate_id: str,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.School:
        """
        Delete an existing School

        Deletes an existing School with the input `school_id`.


        DELETE /candidates/{candidate_id}/schools/{id}

        Args:
            candidate_id: The Candidate's ID.
            id: The School's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            School was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.schools.delete(candidate_id="string", id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/candidates/{candidate_id}/schools/{id}",
            auth_names=["basic_auth"],
            cast_to=models.School,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        candidate_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatesSchoolsListResponse:
        """
        List existing Schools

        Returns a list of existing Schools for the input `candidate_id`.


        GET /candidates/{candidate_id}/schools

        Args:
            candidate_id: Returns the list of schools for the input `candidate_id`.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Schools

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.schools.list(candidate_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/schools",
            auth_names=["basic_auth"],
            cast_to=models.CandidatesSchoolsListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        candidate_id: str,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.School:
        """
        Retrieve an existing School

        Returns an existing School with the input `school_id`.


        GET /candidates/{candidate_id}/schools/{id}

        Args:
            candidate_id: The Candidate's ID.
            id: The School's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            School details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.schools.get(candidate_id="string", id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/schools/{id}",
            auth_names=["basic_auth"],
            cast_to=models.School,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        address: params.Address,
        candidate_id_path: str,
        degree: str,
        major: str,
        name: str,
        candidate_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        current: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        end_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        minor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        object: typing.Union[
            typing.Optional[typing_extensions.Literal["school"]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        phone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        school_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        start_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        year_awarded: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.School:
        """
        Create a new School

        Creates a new School resource.

        Validation for `start_date` and `end_date` is performed to ensure logical dates are provided. `end_date` must be after `start_date`, and both dates must be after 1900-01-01.

        If the country is not US, the following parameters are required in addition to those marked as required below:

        - year_awarded
        - phone
        - minor
        - start_date
        - end_date
        - current
        - address
          - street
          - city
          - zipcode
          - state
          - country


        POST /candidates/{candidate_id}/schools

        Args:
            candidate_id: Candidate linked to this School resource.
            current: Defines whether the Candidate is currently enrolled.
            end_date: Candidate’s end date with the School.
            id: ID of the resource.
            minor: Candidate’s minor.
            object: typing_extensions.Literal["school"]
            phone: School's phone number.
            school_url: School’s website.
            start_date: Candidate’s start date with the School.
            year_awarded: Year in which the degree was awarded.
            address: Address
            candidate_id_path: Creates a School for the input `candidate_id`.
            degree: Degree awarded to the Candidate.
            major: Candidate’s major.
            name: Name of the School.
            request_options: Additional options to customize the HTTP request

        Returns:
            School was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.schools.create(
            address={
                "city": "San Francisco",
                "country": "US",
                "state": "CA",
                "street": "123 Main St.",
                "unit": "2000",
                "zipcode": "90401",
            },
            candidate_id_path="string",
            degree="BA",
            major="Russian Literature",
            name="College University",
            candidate_id="83ebeagdec0948690863766f792ead24d61fe3f9",
            end_date="2017-05-10",
            minor="Background Checks",
            phone="415-111-1111",
            school_url="www.collegeuniversity.com",
            start_date="2012-09-22",
            year_awarded=2017,
        )
        ```
        """
        _json = to_encodable(
            item={
                "candidate_id": candidate_id,
                "current": current,
                "end_date": end_date,
                "id": id,
                "minor": minor,
                "object": object,
                "phone": phone,
                "school_url": school_url,
                "start_date": start_date,
                "year_awarded": year_awarded,
                "address": address,
                "degree": degree,
                "major": major,
                "name": name,
            },
            dump_with=params._SerializerCandidatesSchoolsCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path=f"/candidates/{candidate_id_path}/schools",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.School,
            request_options=request_options or default_request_options(),
        )


class AsyncSchoolsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        candidate_id: str,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.School:
        """
        Delete an existing School

        Deletes an existing School with the input `school_id`.


        DELETE /candidates/{candidate_id}/schools/{id}

        Args:
            candidate_id: The Candidate's ID.
            id: The School's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            School was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.schools.delete(candidate_id="string", id="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/candidates/{candidate_id}/schools/{id}",
            auth_names=["basic_auth"],
            cast_to=models.School,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        candidate_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatesSchoolsListResponse:
        """
        List existing Schools

        Returns a list of existing Schools for the input `candidate_id`.


        GET /candidates/{candidate_id}/schools

        Args:
            candidate_id: Returns the list of schools for the input `candidate_id`.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Schools

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.schools.list(candidate_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/schools",
            auth_names=["basic_auth"],
            cast_to=models.CandidatesSchoolsListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        candidate_id: str,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.School:
        """
        Retrieve an existing School

        Returns an existing School with the input `school_id`.


        GET /candidates/{candidate_id}/schools/{id}

        Args:
            candidate_id: The Candidate's ID.
            id: The School's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            School details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.schools.get(candidate_id="string", id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/schools/{id}",
            auth_names=["basic_auth"],
            cast_to=models.School,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        address: params.Address,
        candidate_id_path: str,
        degree: str,
        major: str,
        name: str,
        candidate_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        current: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        end_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        minor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        object: typing.Union[
            typing.Optional[typing_extensions.Literal["school"]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        phone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        school_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        start_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        year_awarded: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.School:
        """
        Create a new School

        Creates a new School resource.

        Validation for `start_date` and `end_date` is performed to ensure logical dates are provided. `end_date` must be after `start_date`, and both dates must be after 1900-01-01.

        If the country is not US, the following parameters are required in addition to those marked as required below:

        - year_awarded
        - phone
        - minor
        - start_date
        - end_date
        - current
        - address
          - street
          - city
          - zipcode
          - state
          - country


        POST /candidates/{candidate_id}/schools

        Args:
            candidate_id: Candidate linked to this School resource.
            current: Defines whether the Candidate is currently enrolled.
            end_date: Candidate’s end date with the School.
            id: ID of the resource.
            minor: Candidate’s minor.
            object: typing_extensions.Literal["school"]
            phone: School's phone number.
            school_url: School’s website.
            start_date: Candidate’s start date with the School.
            year_awarded: Year in which the degree was awarded.
            address: Address
            candidate_id_path: Creates a School for the input `candidate_id`.
            degree: Degree awarded to the Candidate.
            major: Candidate’s major.
            name: Name of the School.
            request_options: Additional options to customize the HTTP request

        Returns:
            School was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.schools.create(
            address={
                "city": "San Francisco",
                "country": "US",
                "state": "CA",
                "street": "123 Main St.",
                "unit": "2000",
                "zipcode": "90401",
            },
            candidate_id_path="string",
            degree="BA",
            major="Russian Literature",
            name="College University",
            candidate_id="83ebeagdec0948690863766f792ead24d61fe3f9",
            end_date="2017-05-10",
            minor="Background Checks",
            phone="415-111-1111",
            school_url="www.collegeuniversity.com",
            start_date="2012-09-22",
            year_awarded=2017,
        )
        ```
        """
        _json = to_encodable(
            item={
                "candidate_id": candidate_id,
                "current": current,
                "end_date": end_date,
                "id": id,
                "minor": minor,
                "object": object,
                "phone": phone,
                "school_url": school_url,
                "start_date": start_date,
                "year_awarded": year_awarded,
                "address": address,
                "degree": degree,
                "major": major,
                "name": name,
            },
            dump_with=params._SerializerCandidatesSchoolsCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/candidates/{candidate_id_path}/schools",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.School,
            request_options=request_options or default_request_options(),
        )
