import typing
import typing_extensions

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


class EmployersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        candidate_id: str,
        employer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Employer:
        """
        Delete an existing Employer

        Deletes an existing Employer with the input `id`.


        DELETE /candidates/{candidate_id}/employers/{employer_id}

        Args:
            candidate_id: The Candidate's ID.
            employer_id: The Employer's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Employer was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.employers.delete(candidate_id="string", employer_id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/candidates/{candidate_id}/employers/{employer_id}",
            auth_names=["basic_auth"],
            cast_to=models.Employer,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        candidate_id: str,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatesEmployersListResponse:
        """
        List existing Employers

        Returns a list of existing Employers for the input `candidate_id`.


        GET /candidates/{candidate_id}/employers

        Args:
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            candidate_id: Returns the list of employers for the input `candidate_id`.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Employers

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.employers.list(candidate_id="string")
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
        return self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/employers",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.CandidatesEmployersListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        candidate_id: str,
        employer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Employer:
        """
        Retrieve an existing Employer

        Returns an existing Employer with the input `candidate_id` or `employer_id`.


        GET /candidates/{candidate_id}/employers/{employer_id}

        Args:
            candidate_id: The Candidate's ID.
            employer_id: The Employer's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Employer details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.employers.get(candidate_id="string", employer_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/employers/{employer_id}",
            auth_names=["basic_auth"],
            cast_to=models.Employer,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        address: params.Address,
        candidate_id_path: str,
        contract_type: typing_extensions.Literal[
            "contract", "full_time", "internship", "part_time"
        ],
        name: str,
        position: str,
        start_date: str,
        candidate_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        do_not_contact: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        employer_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        end_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        manager: typing.Union[
            typing.Optional[params.CandidatesEmployersCreateBodyManager],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        note: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        object: typing.Union[
            typing.Optional[typing_extensions.Literal["employer"]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        salary: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["employer", "gap"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Employer:
        """
        Create a new Employer

        Creates a new Employer resource.

        If the country is not US, the following parameters will be required in addition to those marked as required in the table below:

        - salary
        - address:
          - street
          - country
          - zipcode
        - manager:
          - name
          - title

        Validation for `start_date` and `end_date` is performed to ensure logical dates are provided. `end_date` must be after `start_date`, and both dates must be after 1900-01-01.


        POST /candidates/{candidate_id}/employers

        Args:
            candidate_id: ID of the Candidate being screened.
            do_not_contact: If `true`, the employer will not be contacted about the Candidate.
            employer_url: Employer’s website.
            end_date: Candidate’s end date with the employer.
            id: ID of the resource.
            manager: CandidatesEmployersCreateBodyManager
            note: A text note used to add context for an employment gap.
            object: typing_extensions.Literal["employer"]
            salary: Candidate’s gross salary in dollars annually.
            type: Type of employment history to be created.

        If type is set to `gap` only `start_date` is required, and only `start_date`, `end_date`, and `note` will be recorded.

            address: Address
            candidate_id_path: Create an employer for the input `candidate_id`.
            contract_type: Candidate’s contract type.
            name: Candidate’s employer’s name.
            position: Candidate’s position or title.
            start_date: Candidate’s start date with the employer.
            request_options: Additional options to customize the HTTP request

        Returns:
            Employer was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.employers.create(
            address={
                "city": "San Francisco",
                "country": "US",
                "state": "CA",
                "street": "123 Main St.",
                "unit": "2000",
                "zipcode": "90401",
            },
            candidate_id_path="string",
            contract_type="full_time",
            name="Checkr",
            position="Software Engineer",
            start_date="2016-06-01",
            candidate_id="xxx",
            do_not_contact=False,
            employer_url="www.employer.com",
            end_date="2017-05-01",
            note="Took time off to travel abroad.",
            salary=10000,
        )
        ```
        """
        _json = to_encodable(
            item={
                "candidate_id": candidate_id,
                "do_not_contact": do_not_contact,
                "employer_url": employer_url,
                "end_date": end_date,
                "id": id,
                "manager": manager,
                "note": note,
                "object": object,
                "salary": salary,
                "type_": type_,
                "address": address,
                "contract_type": contract_type,
                "name": name,
                "position": position,
                "start_date": start_date,
            },
            dump_with=params._SerializerCandidatesEmployersCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path=f"/candidates/{candidate_id_path}/employers",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Employer,
            request_options=request_options or default_request_options(),
        )


class AsyncEmployersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        candidate_id: str,
        employer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Employer:
        """
        Delete an existing Employer

        Deletes an existing Employer with the input `id`.


        DELETE /candidates/{candidate_id}/employers/{employer_id}

        Args:
            candidate_id: The Candidate's ID.
            employer_id: The Employer's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Employer was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.employers.delete(
            candidate_id="string", employer_id="string"
        )
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/candidates/{candidate_id}/employers/{employer_id}",
            auth_names=["basic_auth"],
            cast_to=models.Employer,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        candidate_id: str,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatesEmployersListResponse:
        """
        List existing Employers

        Returns a list of existing Employers for the input `candidate_id`.


        GET /candidates/{candidate_id}/employers

        Args:
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            candidate_id: Returns the list of employers for the input `candidate_id`.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Employers

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.employers.list(candidate_id="string")
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
        return await self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/employers",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.CandidatesEmployersListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        candidate_id: str,
        employer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Employer:
        """
        Retrieve an existing Employer

        Returns an existing Employer with the input `candidate_id` or `employer_id`.


        GET /candidates/{candidate_id}/employers/{employer_id}

        Args:
            candidate_id: The Candidate's ID.
            employer_id: The Employer's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Employer details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.employers.get(
            candidate_id="string", employer_id="string"
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/employers/{employer_id}",
            auth_names=["basic_auth"],
            cast_to=models.Employer,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        address: params.Address,
        candidate_id_path: str,
        contract_type: typing_extensions.Literal[
            "contract", "full_time", "internship", "part_time"
        ],
        name: str,
        position: str,
        start_date: str,
        candidate_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        do_not_contact: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        employer_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        end_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        manager: typing.Union[
            typing.Optional[params.CandidatesEmployersCreateBodyManager],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        note: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        object: typing.Union[
            typing.Optional[typing_extensions.Literal["employer"]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        salary: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["employer", "gap"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Employer:
        """
        Create a new Employer

        Creates a new Employer resource.

        If the country is not US, the following parameters will be required in addition to those marked as required in the table below:

        - salary
        - address:
          - street
          - country
          - zipcode
        - manager:
          - name
          - title

        Validation for `start_date` and `end_date` is performed to ensure logical dates are provided. `end_date` must be after `start_date`, and both dates must be after 1900-01-01.


        POST /candidates/{candidate_id}/employers

        Args:
            candidate_id: ID of the Candidate being screened.
            do_not_contact: If `true`, the employer will not be contacted about the Candidate.
            employer_url: Employer’s website.
            end_date: Candidate’s end date with the employer.
            id: ID of the resource.
            manager: CandidatesEmployersCreateBodyManager
            note: A text note used to add context for an employment gap.
            object: typing_extensions.Literal["employer"]
            salary: Candidate’s gross salary in dollars annually.
            type: Type of employment history to be created.

        If type is set to `gap` only `start_date` is required, and only `start_date`, `end_date`, and `note` will be recorded.

            address: Address
            candidate_id_path: Create an employer for the input `candidate_id`.
            contract_type: Candidate’s contract type.
            name: Candidate’s employer’s name.
            position: Candidate’s position or title.
            start_date: Candidate’s start date with the employer.
            request_options: Additional options to customize the HTTP request

        Returns:
            Employer was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.employers.create(
            address={
                "city": "San Francisco",
                "country": "US",
                "state": "CA",
                "street": "123 Main St.",
                "unit": "2000",
                "zipcode": "90401",
            },
            candidate_id_path="string",
            contract_type="full_time",
            name="Checkr",
            position="Software Engineer",
            start_date="2016-06-01",
            candidate_id="xxx",
            do_not_contact=False,
            employer_url="www.employer.com",
            end_date="2017-05-01",
            note="Took time off to travel abroad.",
            salary=10000,
        )
        ```
        """
        _json = to_encodable(
            item={
                "candidate_id": candidate_id,
                "do_not_contact": do_not_contact,
                "employer_url": employer_url,
                "end_date": end_date,
                "id": id,
                "manager": manager,
                "note": note,
                "object": object,
                "salary": salary,
                "type_": type_,
                "address": address,
                "contract_type": contract_type,
                "name": name,
                "position": position,
                "start_date": start_date,
            },
            dump_with=params._SerializerCandidatesEmployersCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/candidates/{candidate_id_path}/employers",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Employer,
            request_options=request_options or default_request_options(),
        )
