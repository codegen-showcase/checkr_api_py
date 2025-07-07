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
from checkr_api_py.resources.candidates.continuous_checks import (
    AsyncContinuousChecksClient,
    ContinuousChecksClient,
)
from checkr_api_py.resources.candidates.documents import (
    AsyncDocumentsClient,
    DocumentsClient,
)
from checkr_api_py.resources.candidates.driver_licenses import (
    AsyncDriverLicensesClient,
    DriverLicensesClient,
)
from checkr_api_py.resources.candidates.employers import (
    AsyncEmployersClient,
    EmployersClient,
)
from checkr_api_py.resources.candidates.pii import AsyncPiiClient, PiiClient
from checkr_api_py.resources.candidates.postal_address import (
    AsyncPostalAddressClient,
    PostalAddressClient,
)
from checkr_api_py.resources.candidates.professional_licenses import (
    AsyncProfessionalLicensesClient,
    ProfessionalLicensesClient,
)
from checkr_api_py.resources.candidates.schools import AsyncSchoolsClient, SchoolsClient
from checkr_api_py.resources.candidates.ssn import AsyncSsnClient, SsnClient
from checkr_api_py.types import models, params


class CandidatesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.driver_licenses = DriverLicensesClient(base_client=self._base_client)
        self.employers = EmployersClient(base_client=self._base_client)
        self.professional_licenses = ProfessionalLicensesClient(
            base_client=self._base_client
        )
        self.schools = SchoolsClient(base_client=self._base_client)
        self.pii = PiiClient(base_client=self._base_client)
        self.continuous_checks = ContinuousChecksClient(base_client=self._base_client)
        self.documents = DocumentsClient(base_client=self._base_client)
        self.postal_address = PostalAddressClient(base_client=self._base_client)
        self.ssn = SsnClient(base_client=self._base_client)

    def list(
        self,
        *,
        adjudication: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        custom_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        driver_license_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        full_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        geo_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        program_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        report_adjudicated_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        report_adjudicated_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        report_adjudicator_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        report_revised_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        report_revised_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatesListResponse:
        """
        List existing Candidates

        Lists existing Candidates with the input parameters.

        <b>Note: </b>This call will not return candidates with non-US `work_locations`. Use [GET /candidates/{id}](#operation/getCandidate) to retrieve candidates outside the US.


        GET /candidates

        Args:
            adjudication: Returns candidates with the input adjudication. `Null` if no adjudication has been made.
            created_after: Returns candidates created after the input date.
            created_before: Returns candidates created before the input date.
            custom_id: Returns candidates with the input `custom_id`.
            driver_license_number: Returns candidates with the input `driver_license_number`.
            email: Returns candidates with the input email address.
            full_name: Returns candidates with the input `full_name`.
            geo_id: Returns candidates with the input `geo_id`.
            metadata: Returns candidates matching the input key-values. Input keys will be matched exactly. Input values will be pre- and post-pended with wildcards. (For example: A query for 1234 will return results for *1234*.)
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            program_id: Returns candidates with the input `program_id`.
            report_adjudicated_after: Returns candidates adjudicated after the input date.
            report_adjudicated_before: Returns candidates adjudicated before the input date.
            report_adjudicator_email: Returns candidates with a report adjudicated by someone with input `adjudicator_email`.
            report_revised_after: Returns candidates with a report revised after the input date.
            report_revised_before: Returns candidates with a report revised before the input date.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Candidates

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(adjudication, type_utils.NotGiven):
            encode_query_param(
                _query,
                "adjudication",
                to_encodable(item=adjudication, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(created_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created_after",
                to_encodable(item=created_after, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(created_before, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created_before",
                to_encodable(item=created_before, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(custom_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "custom_id",
                to_encodable(item=custom_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(driver_license_number, type_utils.NotGiven):
            encode_query_param(
                _query,
                "driver_license_number",
                to_encodable(item=driver_license_number, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(email, type_utils.NotGiven):
            encode_query_param(
                _query,
                "email",
                to_encodable(item=email, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(full_name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "full_name",
                to_encodable(item=full_name, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(geo_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "geo_id",
                to_encodable(item=geo_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(metadata, type_utils.NotGiven):
            encode_query_param(
                _query,
                "metadata",
                to_encodable(item=metadata, dump_with=typing.Dict[str, typing.Any]),
                style="form",
                explode=True,
            )
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
        if not isinstance(program_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "program_id",
                to_encodable(item=program_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(report_adjudicated_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "report_adjudicated_after",
                to_encodable(item=report_adjudicated_after, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(report_adjudicated_before, type_utils.NotGiven):
            encode_query_param(
                _query,
                "report_adjudicated_before",
                to_encodable(item=report_adjudicated_before, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(report_adjudicator_email, type_utils.NotGiven):
            encode_query_param(
                _query,
                "report_adjudicator_email",
                to_encodable(item=report_adjudicator_email, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(report_revised_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "report_revised_after",
                to_encodable(item=report_revised_after, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(report_revised_before, type_utils.NotGiven):
            encode_query_param(
                _query,
                "report_revised_before",
                to_encodable(item=report_revised_before, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/candidates",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.CandidatesListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        id: str,
        include: typing.Union[
            typing.Optional[typing_extensions.Literal["geos", "reports"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Candidate:
        """
        Retrieve an existing Candidate

        Retrieves an existing Candidate.


        GET /candidates/{id}

        Args:
            include: Comma delimited string specifying the resources to be embedded in the returned Candidate object. See [Embedding Resources](#section/Reference/Embedding-Resources).
            id: The Candidate's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.get(id="string", include="reports")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(include, type_utils.NotGiven):
            encode_query_param(
                _query,
                "include",
                to_encodable(
                    item=include, dump_with=typing_extensions.Literal["geos", "reports"]
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/candidates/{id}",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.Candidate,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        email: str,
        copy_requested: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        custom_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        dob: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        driver_license_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        driver_license_state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        first_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        geo_ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        middle_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mother_maiden_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        no_middle_name: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        object: typing.Union[
            typing.Optional[typing_extensions.Literal["candidate"]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        phone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        postal_address: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        previous_driver_license_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        previous_driver_license_state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        report_ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ssn: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        work_locations: typing.Union[
            typing.Optional[typing.List[params.WorkLocation]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        zipcode: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Candidate:
        """
        Create a new Candidate

        Creates a new Candidate resource.

        ### Required attributes

        The Candidate resource’s required attributes vary depending on its intended use. If this resource is to be used in conjunction with the Invitations API (in which the invitation apply form collects the Candidate's personal information), the only strictly required Candidate attribute is `email`.

        If this resource is to be used to generate any other report type, other personal information is also required.

        Attributes required to generate a Report include:
        - `first_name`
        - `middle_name` or `no_middle_name`
        - `last_name`
        - `dob`

        Attributes required to generate a Report with a criminal check screening:
        - `ssn`
        - `zipcode`

        Attributes required to generate a report with a Motor Vehicle Record (MVR) screening:
        - `driver_license_number`
        - `driver_license_state`

        See [Driver License validation](#section/Reference/Driver-License-validation) in the Reference section for a list of valid input by state.

        Attributes recommended to generate a report with an Identity Document Verification screening:
        - `phone` (mobile phone number)

        Validation for these attributes is performed when requesting a Report, as the requirements depend on the Package.

        Checkr's product incorporates SSN field controls designed to not accept SSNs with the following characteristics:

          - SSNs without exactly 9 numeric characters
          - SSNs that start with 666 (666-34-3768)
          - SSNs that start with 9 (967-65-4325)
          - SSNs that are a single digit (111-11-1111)
          - SSNs that are sequential digits (123-45-6789)


        POST /candidates

        Args:
            copy_requested: If `true`, the candidate has asked to receive a copy of their report.
            custom_id: Client-assigned unique ID for the Candidate. Can be used to map Checkr Candidate IDs to your internal tracking system, and to search for Candidates through both the Dashboard and the API.
            dob: Candidate’s date of birth.
            driver_license_number: Candidate’s driver license number.
            driver_license_state: Candidate’s driver license state of issue.
        Format: `ISO 3166-2:US`.

            first_name: Candidate’s first name.

            geo_ids: Array of Geo IDs.
            last_name: Candidate’s last name.
            metadata: Up to 50 customer-defined key-value pairs. Use this parameter to store additional information on your candidate. For example: Use the key to map candidates to `job_req_id`, `application_id`, or `branch_id`. Keys must be 40 characters or less. Values must be 500 characters or less.
        For example: { "job_req_id": "12345" }
            middle_name: Candidate’s middle name. This field is required if `no_middle_name` is `false`.

            mother_maiden_name: Candidate’s mother’s maiden name.

            no_middle_name: Required if no `middle_name` is provided. `true` if the candidate has no middle name.

            object: typing_extensions.Literal["candidate"]
            phone: Candidate’s phone number.
            postal_address: The candidate postal address is the address Checkr will use to send postal mail to the candidate. Each candidate can be associated with only one postal address.
            previous_driver_license_number: Candidate’s previous driver license number.
            previous_driver_license_state: State that issued the candidate’s previous driver license.
        Format: `ISO 3166-2:US`.

            report_ids: Array of Report IDs.
            ssn: Candidate’s Social Security Number. This value will be redacted in all return calls, except for the last four digits.
            work_locations: <font color="red">Required</font> for non-US candidates.

        Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.

            zipcode: Candidate’s 5-digit zip code.
            email: Candidate’s email address.

            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.create(
            email="john.smith@gmail.com",
            custom_id="HRIS-27",
            dob="1970-01-22",
            driver_license_number="F2111655",
            driver_license_state="CA",
            first_name="John",
            last_name="Smith",
            middle_name="Alfred",
            mother_maiden_name="Jones",
            phone="5555555555",
            postal_address={
                "city": "San Francisco",
                "name": "John Alfred Smith",
                "state": "CA",
                "street": "123 Main Street",
                "street2": "APT A",
                "zipcode": "94108",
            },
            previous_driver_license_number="F1501739",
            previous_driver_license_state="MD",
            ssn="XXX-XX-4645",
            zipcode="90401",
        )
        ```
        """
        _json = to_encodable(
            item={
                "copy_requested": copy_requested,
                "custom_id": custom_id,
                "dob": dob,
                "driver_license_number": driver_license_number,
                "driver_license_state": driver_license_state,
                "first_name": first_name,
                "geo_ids": geo_ids,
                "last_name": last_name,
                "metadata": metadata,
                "middle_name": middle_name,
                "mother_maiden_name": mother_maiden_name,
                "no_middle_name": no_middle_name,
                "object": object,
                "phone": phone,
                "postal_address": postal_address,
                "previous_driver_license_number": previous_driver_license_number,
                "previous_driver_license_state": previous_driver_license_state,
                "report_ids": report_ids,
                "ssn": ssn,
                "work_locations": work_locations,
                "zipcode": zipcode,
                "email": email,
            },
            dump_with=params._SerializerCandidatesCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/candidates",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Candidate,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        id_path: str,
        adjudication: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "engaged", "post_adverse_action", "pre_adverse_action"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        copy_requested: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        custom_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        dob: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        driver_license_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        driver_license_state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        first_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        geo_ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        middle_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mother_maiden_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        no_middle_name: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        object: typing.Union[
            typing.Optional[typing_extensions.Literal["candidate"]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        phone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        postal_address: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        previous_driver_license_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        previous_driver_license_state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        report_ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ssn: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        uri: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        zipcode: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Candidate:
        """
        Update an existing Candidate

        Updates an existing Candidate.

        Attempts to update a field that cannot be updated will return a 400 error stating "... cannot be updated”. For example, attempting to update an SSN will return 400 stating "Candidate SSN can not be updated because it has reports”.

        Updating `geo_ids` will **replace** all existing Geos. To keep existing geos, include their IDs in the update request. `geo_ids` cannot be updated if the candidate's work location is outside the US.
        Only fields with `null` values can be updated after a Report has been ordered for a Candidate with the exception of the following fields:
        - email
        - phone
        - previous_driver_license_number
        - previous_driver_license_state
        - copy_requested
        - custom_id
        - geo_ids

        Updating metadata with an empty value (null or empty object) will delete existing metadata. Individual keys may also be set and unset.
        - Adding a new key-value pair will maintain all existing key-value pairs.
        - Providing a new value for an existing key will update the old value to the new value.
        - Providing an empty value for an existing key will remove that key from the metadata object.
        - When all keys in the metadata object have empty values, the object will be deleted.


        POST /candidates/{id}

        Args:
            adjudication: The adjudication for the Candidate’s most recently created Report.
            copy_requested: If `true`, the candidate has asked to receive a copy of their report.
            custom_id: Client-assigned unique ID for the Candidate. Can be used to map Checkr Candidate IDs to your internal tracking system, and to search for Candidates through both the Dashboard and the API.
            dob: Candidate’s date of birth.
            driver_license_number: Candidate’s driver license number.
            driver_license_state: Candidate’s driver license state of issue.
        Format: `ISO 3166-2:US`.

            email: Candidate’s email address.

            first_name: Candidate’s first name.

            geo_ids: Array of Geo IDs.
            id: ID of the resource.
            last_name: Candidate’s last name.
            metadata: Up to 50 customer-defined key-value pairs. Use this parameter to store additional information on your candidate. For example: Use the key to map candidates to `job_req_id`, `application_id`, or `branch_id`. Keys must be 40 characters or less. Values must be 500 characters or less.
        For example: { "job_req_id": "12345" }
            middle_name: Candidate’s middle name. This field is required if `no_middle_name` is `false`.

            mother_maiden_name: Candidate’s mother’s maiden name.

            no_middle_name: Required if no `middle_name` is provided. `true` if the candidate has no middle name.

            object: typing_extensions.Literal["candidate"]
            phone: Candidate’s phone number.
            postal_address: Candidate's postal address.
            previous_driver_license_number: Candidate’s previous driver license number.
            previous_driver_license_state: State that issued the candidate’s previous driver license.
        Format: `ISO 3166-2:US`.

            report_ids: Array of Report IDs.
            ssn: Candidate’s Social Security Number. This value will be redacted in all return calls, except for the last four digits.
            uri: URI of the resource.
            zipcode: Candidate’s 5-digit zip code.
            id_path: The Candidate's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate was successfully updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.update(
            id_path="string",
            dob="1970-01-22",
            driver_license_number="F2111655",
            driver_license_state="CA",
            email="john.smith@gmail.com",
            first_name="John",
            last_name="Smith",
            middle_name="Alfred",
            mother_maiden_name="Jones",
            phone="5555555555",
            postal_address={
                "city": "San Francisco",
                "name": "John Alfred Smith",
                "state": "CA",
                "street": "123 Main Street",
                "street2": "APT A",
                "zipcode": "94108",
            },
            previous_driver_license_number="F1501739",
            previous_driver_license_state="MD",
            ssn="XXX-XX-4645",
            uri="/v1/candidates/e44aa283528e6fde7d542194",
            zipcode="90401",
        )
        ```
        """
        _json = to_encodable(
            item={
                "adjudication": adjudication,
                "copy_requested": copy_requested,
                "custom_id": custom_id,
                "dob": dob,
                "driver_license_number": driver_license_number,
                "driver_license_state": driver_license_state,
                "email": email,
                "first_name": first_name,
                "geo_ids": geo_ids,
                "id": id,
                "last_name": last_name,
                "metadata": metadata,
                "middle_name": middle_name,
                "mother_maiden_name": mother_maiden_name,
                "no_middle_name": no_middle_name,
                "object": object,
                "phone": phone,
                "postal_address": postal_address,
                "previous_driver_license_number": previous_driver_license_number,
                "previous_driver_license_state": previous_driver_license_state,
                "report_ids": report_ids,
                "ssn": ssn,
                "uri": uri,
                "zipcode": zipcode,
            },
            dump_with=params._SerializerCandidate,
        )
        return self._base_client.request(
            method="POST",
            path=f"/candidates/{id_path}",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Candidate,
            request_options=request_options or default_request_options(),
        )


class AsyncCandidatesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.driver_licenses = AsyncDriverLicensesClient(base_client=self._base_client)
        self.employers = AsyncEmployersClient(base_client=self._base_client)
        self.professional_licenses = AsyncProfessionalLicensesClient(
            base_client=self._base_client
        )
        self.schools = AsyncSchoolsClient(base_client=self._base_client)
        self.pii = AsyncPiiClient(base_client=self._base_client)
        self.continuous_checks = AsyncContinuousChecksClient(
            base_client=self._base_client
        )
        self.documents = AsyncDocumentsClient(base_client=self._base_client)
        self.postal_address = AsyncPostalAddressClient(base_client=self._base_client)
        self.ssn = AsyncSsnClient(base_client=self._base_client)

    async def list(
        self,
        *,
        adjudication: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        custom_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        driver_license_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        full_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        geo_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        program_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        report_adjudicated_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        report_adjudicated_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        report_adjudicator_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        report_revised_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        report_revised_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatesListResponse:
        """
        List existing Candidates

        Lists existing Candidates with the input parameters.

        <b>Note: </b>This call will not return candidates with non-US `work_locations`. Use [GET /candidates/{id}](#operation/getCandidate) to retrieve candidates outside the US.


        GET /candidates

        Args:
            adjudication: Returns candidates with the input adjudication. `Null` if no adjudication has been made.
            created_after: Returns candidates created after the input date.
            created_before: Returns candidates created before the input date.
            custom_id: Returns candidates with the input `custom_id`.
            driver_license_number: Returns candidates with the input `driver_license_number`.
            email: Returns candidates with the input email address.
            full_name: Returns candidates with the input `full_name`.
            geo_id: Returns candidates with the input `geo_id`.
            metadata: Returns candidates matching the input key-values. Input keys will be matched exactly. Input values will be pre- and post-pended with wildcards. (For example: A query for 1234 will return results for *1234*.)
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            program_id: Returns candidates with the input `program_id`.
            report_adjudicated_after: Returns candidates adjudicated after the input date.
            report_adjudicated_before: Returns candidates adjudicated before the input date.
            report_adjudicator_email: Returns candidates with a report adjudicated by someone with input `adjudicator_email`.
            report_revised_after: Returns candidates with a report revised after the input date.
            report_revised_before: Returns candidates with a report revised before the input date.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Candidates

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(adjudication, type_utils.NotGiven):
            encode_query_param(
                _query,
                "adjudication",
                to_encodable(item=adjudication, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(created_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created_after",
                to_encodable(item=created_after, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(created_before, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created_before",
                to_encodable(item=created_before, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(custom_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "custom_id",
                to_encodable(item=custom_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(driver_license_number, type_utils.NotGiven):
            encode_query_param(
                _query,
                "driver_license_number",
                to_encodable(item=driver_license_number, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(email, type_utils.NotGiven):
            encode_query_param(
                _query,
                "email",
                to_encodable(item=email, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(full_name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "full_name",
                to_encodable(item=full_name, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(geo_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "geo_id",
                to_encodable(item=geo_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(metadata, type_utils.NotGiven):
            encode_query_param(
                _query,
                "metadata",
                to_encodable(item=metadata, dump_with=typing.Dict[str, typing.Any]),
                style="form",
                explode=True,
            )
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
        if not isinstance(program_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "program_id",
                to_encodable(item=program_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(report_adjudicated_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "report_adjudicated_after",
                to_encodable(item=report_adjudicated_after, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(report_adjudicated_before, type_utils.NotGiven):
            encode_query_param(
                _query,
                "report_adjudicated_before",
                to_encodable(item=report_adjudicated_before, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(report_adjudicator_email, type_utils.NotGiven):
            encode_query_param(
                _query,
                "report_adjudicator_email",
                to_encodable(item=report_adjudicator_email, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(report_revised_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "report_revised_after",
                to_encodable(item=report_revised_after, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(report_revised_before, type_utils.NotGiven):
            encode_query_param(
                _query,
                "report_revised_before",
                to_encodable(item=report_revised_before, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/candidates",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.CandidatesListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        id: str,
        include: typing.Union[
            typing.Optional[typing_extensions.Literal["geos", "reports"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Candidate:
        """
        Retrieve an existing Candidate

        Retrieves an existing Candidate.


        GET /candidates/{id}

        Args:
            include: Comma delimited string specifying the resources to be embedded in the returned Candidate object. See [Embedding Resources](#section/Reference/Embedding-Resources).
            id: The Candidate's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.get(id="string", include="reports")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(include, type_utils.NotGiven):
            encode_query_param(
                _query,
                "include",
                to_encodable(
                    item=include, dump_with=typing_extensions.Literal["geos", "reports"]
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/candidates/{id}",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.Candidate,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        email: str,
        copy_requested: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        custom_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        dob: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        driver_license_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        driver_license_state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        first_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        geo_ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        middle_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mother_maiden_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        no_middle_name: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        object: typing.Union[
            typing.Optional[typing_extensions.Literal["candidate"]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        phone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        postal_address: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        previous_driver_license_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        previous_driver_license_state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        report_ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ssn: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        work_locations: typing.Union[
            typing.Optional[typing.List[params.WorkLocation]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        zipcode: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Candidate:
        """
        Create a new Candidate

        Creates a new Candidate resource.

        ### Required attributes

        The Candidate resource’s required attributes vary depending on its intended use. If this resource is to be used in conjunction with the Invitations API (in which the invitation apply form collects the Candidate's personal information), the only strictly required Candidate attribute is `email`.

        If this resource is to be used to generate any other report type, other personal information is also required.

        Attributes required to generate a Report include:
        - `first_name`
        - `middle_name` or `no_middle_name`
        - `last_name`
        - `dob`

        Attributes required to generate a Report with a criminal check screening:
        - `ssn`
        - `zipcode`

        Attributes required to generate a report with a Motor Vehicle Record (MVR) screening:
        - `driver_license_number`
        - `driver_license_state`

        See [Driver License validation](#section/Reference/Driver-License-validation) in the Reference section for a list of valid input by state.

        Attributes recommended to generate a report with an Identity Document Verification screening:
        - `phone` (mobile phone number)

        Validation for these attributes is performed when requesting a Report, as the requirements depend on the Package.

        Checkr's product incorporates SSN field controls designed to not accept SSNs with the following characteristics:

          - SSNs without exactly 9 numeric characters
          - SSNs that start with 666 (666-34-3768)
          - SSNs that start with 9 (967-65-4325)
          - SSNs that are a single digit (111-11-1111)
          - SSNs that are sequential digits (123-45-6789)


        POST /candidates

        Args:
            copy_requested: If `true`, the candidate has asked to receive a copy of their report.
            custom_id: Client-assigned unique ID for the Candidate. Can be used to map Checkr Candidate IDs to your internal tracking system, and to search for Candidates through both the Dashboard and the API.
            dob: Candidate’s date of birth.
            driver_license_number: Candidate’s driver license number.
            driver_license_state: Candidate’s driver license state of issue.
        Format: `ISO 3166-2:US`.

            first_name: Candidate’s first name.

            geo_ids: Array of Geo IDs.
            last_name: Candidate’s last name.
            metadata: Up to 50 customer-defined key-value pairs. Use this parameter to store additional information on your candidate. For example: Use the key to map candidates to `job_req_id`, `application_id`, or `branch_id`. Keys must be 40 characters or less. Values must be 500 characters or less.
        For example: { "job_req_id": "12345" }
            middle_name: Candidate’s middle name. This field is required if `no_middle_name` is `false`.

            mother_maiden_name: Candidate’s mother’s maiden name.

            no_middle_name: Required if no `middle_name` is provided. `true` if the candidate has no middle name.

            object: typing_extensions.Literal["candidate"]
            phone: Candidate’s phone number.
            postal_address: The candidate postal address is the address Checkr will use to send postal mail to the candidate. Each candidate can be associated with only one postal address.
            previous_driver_license_number: Candidate’s previous driver license number.
            previous_driver_license_state: State that issued the candidate’s previous driver license.
        Format: `ISO 3166-2:US`.

            report_ids: Array of Report IDs.
            ssn: Candidate’s Social Security Number. This value will be redacted in all return calls, except for the last four digits.
            work_locations: <font color="red">Required</font> for non-US candidates.

        Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.

            zipcode: Candidate’s 5-digit zip code.
            email: Candidate’s email address.

            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.create(
            email="john.smith@gmail.com",
            custom_id="HRIS-27",
            dob="1970-01-22",
            driver_license_number="F2111655",
            driver_license_state="CA",
            first_name="John",
            last_name="Smith",
            middle_name="Alfred",
            mother_maiden_name="Jones",
            phone="5555555555",
            postal_address={
                "city": "San Francisco",
                "name": "John Alfred Smith",
                "state": "CA",
                "street": "123 Main Street",
                "street2": "APT A",
                "zipcode": "94108",
            },
            previous_driver_license_number="F1501739",
            previous_driver_license_state="MD",
            ssn="XXX-XX-4645",
            zipcode="90401",
        )
        ```
        """
        _json = to_encodable(
            item={
                "copy_requested": copy_requested,
                "custom_id": custom_id,
                "dob": dob,
                "driver_license_number": driver_license_number,
                "driver_license_state": driver_license_state,
                "first_name": first_name,
                "geo_ids": geo_ids,
                "last_name": last_name,
                "metadata": metadata,
                "middle_name": middle_name,
                "mother_maiden_name": mother_maiden_name,
                "no_middle_name": no_middle_name,
                "object": object,
                "phone": phone,
                "postal_address": postal_address,
                "previous_driver_license_number": previous_driver_license_number,
                "previous_driver_license_state": previous_driver_license_state,
                "report_ids": report_ids,
                "ssn": ssn,
                "work_locations": work_locations,
                "zipcode": zipcode,
                "email": email,
            },
            dump_with=params._SerializerCandidatesCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/candidates",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Candidate,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        id_path: str,
        adjudication: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "engaged", "post_adverse_action", "pre_adverse_action"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        copy_requested: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        custom_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        dob: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        driver_license_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        driver_license_state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        first_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        geo_ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        middle_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mother_maiden_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        no_middle_name: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        object: typing.Union[
            typing.Optional[typing_extensions.Literal["candidate"]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        phone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        postal_address: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        previous_driver_license_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        previous_driver_license_state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        report_ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ssn: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        uri: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        zipcode: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Candidate:
        """
        Update an existing Candidate

        Updates an existing Candidate.

        Attempts to update a field that cannot be updated will return a 400 error stating "... cannot be updated”. For example, attempting to update an SSN will return 400 stating "Candidate SSN can not be updated because it has reports”.

        Updating `geo_ids` will **replace** all existing Geos. To keep existing geos, include their IDs in the update request. `geo_ids` cannot be updated if the candidate's work location is outside the US.
        Only fields with `null` values can be updated after a Report has been ordered for a Candidate with the exception of the following fields:
        - email
        - phone
        - previous_driver_license_number
        - previous_driver_license_state
        - copy_requested
        - custom_id
        - geo_ids

        Updating metadata with an empty value (null or empty object) will delete existing metadata. Individual keys may also be set and unset.
        - Adding a new key-value pair will maintain all existing key-value pairs.
        - Providing a new value for an existing key will update the old value to the new value.
        - Providing an empty value for an existing key will remove that key from the metadata object.
        - When all keys in the metadata object have empty values, the object will be deleted.


        POST /candidates/{id}

        Args:
            adjudication: The adjudication for the Candidate’s most recently created Report.
            copy_requested: If `true`, the candidate has asked to receive a copy of their report.
            custom_id: Client-assigned unique ID for the Candidate. Can be used to map Checkr Candidate IDs to your internal tracking system, and to search for Candidates through both the Dashboard and the API.
            dob: Candidate’s date of birth.
            driver_license_number: Candidate’s driver license number.
            driver_license_state: Candidate’s driver license state of issue.
        Format: `ISO 3166-2:US`.

            email: Candidate’s email address.

            first_name: Candidate’s first name.

            geo_ids: Array of Geo IDs.
            id: ID of the resource.
            last_name: Candidate’s last name.
            metadata: Up to 50 customer-defined key-value pairs. Use this parameter to store additional information on your candidate. For example: Use the key to map candidates to `job_req_id`, `application_id`, or `branch_id`. Keys must be 40 characters or less. Values must be 500 characters or less.
        For example: { "job_req_id": "12345" }
            middle_name: Candidate’s middle name. This field is required if `no_middle_name` is `false`.

            mother_maiden_name: Candidate’s mother’s maiden name.

            no_middle_name: Required if no `middle_name` is provided. `true` if the candidate has no middle name.

            object: typing_extensions.Literal["candidate"]
            phone: Candidate’s phone number.
            postal_address: Candidate's postal address.
            previous_driver_license_number: Candidate’s previous driver license number.
            previous_driver_license_state: State that issued the candidate’s previous driver license.
        Format: `ISO 3166-2:US`.

            report_ids: Array of Report IDs.
            ssn: Candidate’s Social Security Number. This value will be redacted in all return calls, except for the last four digits.
            uri: URI of the resource.
            zipcode: Candidate’s 5-digit zip code.
            id_path: The Candidate's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate was successfully updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.update(
            id_path="string",
            dob="1970-01-22",
            driver_license_number="F2111655",
            driver_license_state="CA",
            email="john.smith@gmail.com",
            first_name="John",
            last_name="Smith",
            middle_name="Alfred",
            mother_maiden_name="Jones",
            phone="5555555555",
            postal_address={
                "city": "San Francisco",
                "name": "John Alfred Smith",
                "state": "CA",
                "street": "123 Main Street",
                "street2": "APT A",
                "zipcode": "94108",
            },
            previous_driver_license_number="F1501739",
            previous_driver_license_state="MD",
            ssn="XXX-XX-4645",
            uri="/v1/candidates/e44aa283528e6fde7d542194",
            zipcode="90401",
        )
        ```
        """
        _json = to_encodable(
            item={
                "adjudication": adjudication,
                "copy_requested": copy_requested,
                "custom_id": custom_id,
                "dob": dob,
                "driver_license_number": driver_license_number,
                "driver_license_state": driver_license_state,
                "email": email,
                "first_name": first_name,
                "geo_ids": geo_ids,
                "id": id,
                "last_name": last_name,
                "metadata": metadata,
                "middle_name": middle_name,
                "mother_maiden_name": mother_maiden_name,
                "no_middle_name": no_middle_name,
                "object": object,
                "phone": phone,
                "postal_address": postal_address,
                "previous_driver_license_number": previous_driver_license_number,
                "previous_driver_license_state": previous_driver_license_state,
                "report_ids": report_ids,
                "ssn": ssn,
                "uri": uri,
                "zipcode": zipcode,
            },
            dump_with=params._SerializerCandidate,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/candidates/{id_path}",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Candidate,
            request_options=request_options or default_request_options(),
        )
