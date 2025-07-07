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
from checkr_api_py.resources.reports.addresses import (
    AddressesClient,
    AsyncAddressesClient,
)
from checkr_api_py.resources.reports.adverse_actions import (
    AdverseActionsClient,
    AsyncAdverseActionsClient,
)
from checkr_api_py.resources.reports.adverse_items import (
    AdverseItemsClient,
    AsyncAdverseItemsClient,
)
from checkr_api_py.resources.reports.assessments import (
    AssessmentsClient,
    AsyncAssessmentsClient,
)
from checkr_api_py.resources.reports.candidate_stories import (
    AsyncCandidateStoriesClient,
    CandidateStoriesClient,
)
from checkr_api_py.resources.reports.complete import AsyncCompleteClient, CompleteClient
from checkr_api_py.resources.reports.eta import AsyncEtaClient, EtaClient
from checkr_api_py.resources.reports.tags import AsyncTagsClient, TagsClient
from checkr_api_py.resources.reports.verifications import (
    AsyncVerificationsClient,
    VerificationsClient,
)
from checkr_api_py.types import models, params


class ReportsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.tags = TagsClient(base_client=self._base_client)
        self.eta = EtaClient(base_client=self._base_client)
        self.addresses = AddressesClient(base_client=self._base_client)
        self.adverse_items = AdverseItemsClient(base_client=self._base_client)
        self.assessments = AssessmentsClient(base_client=self._base_client)
        self.verifications = VerificationsClient(base_client=self._base_client)
        self.complete = CompleteClient(base_client=self._base_client)
        self.adverse_actions = AdverseActionsClient(base_client=self._base_client)
        self.candidate_stories = CandidateStoriesClient(base_client=self._base_client)

    def get(
        self,
        *,
        id: str,
        include: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "arrest_search",
                    "candidate",
                    "candidate_stories",
                    "county_civil_searches",
                    "county_criminal_searches",
                    "credit_report",
                    "dispute_comments",
                    "documents",
                    "drug_alcohol_clearinghouse",
                    "drug_screening",
                    "education_verification",
                    "employment_verification",
                    "eviction_search",
                    "facis_search",
                    "federal_civil_search",
                    "federal_criminal_search",
                    "geos",
                    "global_watchlist_search",
                    "international_adverse_media_searches",
                    "international_criminal_searches",
                    "international_criminal_searches_v2",
                    "international_education_verification",
                    "international_employment_verification",
                    "international_global_watchlist_search",
                    "international_identity_document_validation",
                    "motor_vehicle_report",
                    "municipal_criminal_searches",
                    "national_criminal_search",
                    "occupational_health_screening",
                    "personal_reference_verifications",
                    "photo_verification",
                    "pointer_state_criminal_searches",
                    "professional_license_verifications",
                    "professional_reference_verifications",
                    "program",
                    "public_comments",
                    "self_disclosures",
                    "sex_offender_search",
                    "ssn_trace",
                    "state_criminal_searches",
                    "terrorist_watchlist_search",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Report:
        """
        Retrieve an existing Report

        Returns an existing Report with the input ID.


        GET /reports/{id}

        Args:
            include: Comma delimited string specifying the resources to be embedded in the returned Report object. See [Embedding Resources](#section/Reference/Embedding-Resources).
            id: The Report's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Report details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.get(id="string", include="candidate")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(include, type_utils.NotGiven):
            encode_query_param(
                _query,
                "include",
                to_encodable(
                    item=include,
                    dump_with=typing_extensions.Literal[
                        "arrest_search",
                        "candidate",
                        "candidate_stories",
                        "county_civil_searches",
                        "county_criminal_searches",
                        "credit_report",
                        "dispute_comments",
                        "documents",
                        "drug_alcohol_clearinghouse",
                        "drug_screening",
                        "education_verification",
                        "employment_verification",
                        "eviction_search",
                        "facis_search",
                        "federal_civil_search",
                        "federal_criminal_search",
                        "geos",
                        "global_watchlist_search",
                        "international_adverse_media_searches",
                        "international_criminal_searches",
                        "international_criminal_searches_v2",
                        "international_education_verification",
                        "international_employment_verification",
                        "international_global_watchlist_search",
                        "international_identity_document_validation",
                        "motor_vehicle_report",
                        "municipal_criminal_searches",
                        "national_criminal_search",
                        "occupational_health_screening",
                        "personal_reference_verifications",
                        "photo_verification",
                        "pointer_state_criminal_searches",
                        "professional_license_verifications",
                        "professional_reference_verifications",
                        "program",
                        "public_comments",
                        "self_disclosures",
                        "sex_offender_search",
                        "ssn_trace",
                        "state_criminal_searches",
                        "terrorist_watchlist_search",
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/reports/{id}",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.Report,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        candidate_id: str,
        package: str,
        node: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        self_disclosures: typing.Union[
            typing.Optional[typing.List[params.SelfDisclosure]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tags: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        work_locations: typing.Union[
            typing.Optional[typing.List[params.WorkLocation]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Report:
        """
        Create a new Report

        Creates a new Report resource.

        <b>Notes: </b>
        - This resource does not support the creation of reports which include international Packages. Use the [`/invitations` API](#tag/invitations) to order these reports.
        - Employment Verifications, Education Verifications, and Credit Checks may not be initiated using the `/reports` API. Please use the [`/invitations` API](#tag/invitations) to initiate the [Checkr-Hosted Apply Flow](/#section/Getting-Started/Create-an-Invitation) when ordering background checks that include any of these screening types.
        - Creating a Report which includes an Occupational Health or Drug
        Check will automatically issue an email invitation to the candidate to schedule their appointment at a clinic of their choice.


        POST /reports

        Args:
            node: <font color="red">Required</font> for hierarchy-enabled accounts.

        `custom_id` of the associated node.

            self_disclosures: Array of SelfDisclosures

        **Note:** Self Disclosures may not be added, updated, or deleted after a Report has been created. The information provided in a Self Disclosure will not be included in the completed Report, and may be retrieved using [GET](#operation/getReport) `/v1/reports/{id}?include=documents`. See the [Documents](#tag/Documents) resource for more information.

        Removing the requirement for the description, date, and location parameters greatly reduces the value of Self Disclosures. If your system mandates that these parameters be optional, work with your Checkr Customer Success Manager to disable the requirement.

            tags: Array of tags for the Report.
            work_locations: <font color="red">Required</font> for hierarchy-enabled accounts.

        Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.

            candidate_id: ID of the Candidate screened.
            package: `slug` of the associated package.
        Example: `driver_pro`

            request_options: Additional options to customize the HTTP request

        Returns:
            Report was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.create(candidate_id="e44aa283528e6fde7d542194", package="string")
        ```
        """
        _json = to_encodable(
            item={
                "node": node,
                "self_disclosures": self_disclosures,
                "tags": tags,
                "work_locations": work_locations,
                "candidate_id": candidate_id,
                "package": package,
            },
            dump_with=params._SerializerReportsCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/reports",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Report,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        id: str,
        adjudication: typing.Union[
            typing.Optional[typing_extensions.Literal["engaged"]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        package: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Report:
        """
        Update an existing Report

        Updates the `package` or `adjudication` for an existing Report resource.

        Use this endpoint to update reports which include the candidate's Social Security Number. To update a Report which does not include an SSN, first use the [update Candidate](#operation/updateCandidate) request to add the candidate’s SSN before updating the report.

        Either `package` or `adjudication` is required.

        <b>Note: </b>This endpoint may also be used to update international reports for candidates which do not include an SSN.
        <div class="alert alert-info">

          **Note**: The Package of a Report cannot be updated if it has an Adverse Action with the status: `complete` or `dispute`. To proceed, cancel the Adverse Action or create a new Report.

        </div>


        POST /reports/{id}

        Args:
            adjudication: typing_extensions.Literal["engaged"]
            package: Slug of the Package.

            id: The Report's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Report was successfully updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.update(id="string", adjudication="engaged", package="driver_pro")
        ```
        """
        _json = to_encodable(
            item={"adjudication": adjudication, "package": package},
            dump_with=params._SerializerReportsUpdateBody,
        )
        return self._base_client.request(
            method="POST",
            path=f"/reports/{id}",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Report,
            request_options=request_options or default_request_options(),
        )


class AsyncReportsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.tags = AsyncTagsClient(base_client=self._base_client)
        self.eta = AsyncEtaClient(base_client=self._base_client)
        self.addresses = AsyncAddressesClient(base_client=self._base_client)
        self.adverse_items = AsyncAdverseItemsClient(base_client=self._base_client)
        self.assessments = AsyncAssessmentsClient(base_client=self._base_client)
        self.verifications = AsyncVerificationsClient(base_client=self._base_client)
        self.complete = AsyncCompleteClient(base_client=self._base_client)
        self.adverse_actions = AsyncAdverseActionsClient(base_client=self._base_client)
        self.candidate_stories = AsyncCandidateStoriesClient(
            base_client=self._base_client
        )

    async def get(
        self,
        *,
        id: str,
        include: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "arrest_search",
                    "candidate",
                    "candidate_stories",
                    "county_civil_searches",
                    "county_criminal_searches",
                    "credit_report",
                    "dispute_comments",
                    "documents",
                    "drug_alcohol_clearinghouse",
                    "drug_screening",
                    "education_verification",
                    "employment_verification",
                    "eviction_search",
                    "facis_search",
                    "federal_civil_search",
                    "federal_criminal_search",
                    "geos",
                    "global_watchlist_search",
                    "international_adverse_media_searches",
                    "international_criminal_searches",
                    "international_criminal_searches_v2",
                    "international_education_verification",
                    "international_employment_verification",
                    "international_global_watchlist_search",
                    "international_identity_document_validation",
                    "motor_vehicle_report",
                    "municipal_criminal_searches",
                    "national_criminal_search",
                    "occupational_health_screening",
                    "personal_reference_verifications",
                    "photo_verification",
                    "pointer_state_criminal_searches",
                    "professional_license_verifications",
                    "professional_reference_verifications",
                    "program",
                    "public_comments",
                    "self_disclosures",
                    "sex_offender_search",
                    "ssn_trace",
                    "state_criminal_searches",
                    "terrorist_watchlist_search",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Report:
        """
        Retrieve an existing Report

        Returns an existing Report with the input ID.


        GET /reports/{id}

        Args:
            include: Comma delimited string specifying the resources to be embedded in the returned Report object. See [Embedding Resources](#section/Reference/Embedding-Resources).
            id: The Report's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Report details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.get(id="string", include="candidate")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(include, type_utils.NotGiven):
            encode_query_param(
                _query,
                "include",
                to_encodable(
                    item=include,
                    dump_with=typing_extensions.Literal[
                        "arrest_search",
                        "candidate",
                        "candidate_stories",
                        "county_civil_searches",
                        "county_criminal_searches",
                        "credit_report",
                        "dispute_comments",
                        "documents",
                        "drug_alcohol_clearinghouse",
                        "drug_screening",
                        "education_verification",
                        "employment_verification",
                        "eviction_search",
                        "facis_search",
                        "federal_civil_search",
                        "federal_criminal_search",
                        "geos",
                        "global_watchlist_search",
                        "international_adverse_media_searches",
                        "international_criminal_searches",
                        "international_criminal_searches_v2",
                        "international_education_verification",
                        "international_employment_verification",
                        "international_global_watchlist_search",
                        "international_identity_document_validation",
                        "motor_vehicle_report",
                        "municipal_criminal_searches",
                        "national_criminal_search",
                        "occupational_health_screening",
                        "personal_reference_verifications",
                        "photo_verification",
                        "pointer_state_criminal_searches",
                        "professional_license_verifications",
                        "professional_reference_verifications",
                        "program",
                        "public_comments",
                        "self_disclosures",
                        "sex_offender_search",
                        "ssn_trace",
                        "state_criminal_searches",
                        "terrorist_watchlist_search",
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/reports/{id}",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.Report,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        candidate_id: str,
        package: str,
        node: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        self_disclosures: typing.Union[
            typing.Optional[typing.List[params.SelfDisclosure]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tags: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        work_locations: typing.Union[
            typing.Optional[typing.List[params.WorkLocation]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Report:
        """
        Create a new Report

        Creates a new Report resource.

        <b>Notes: </b>
        - This resource does not support the creation of reports which include international Packages. Use the [`/invitations` API](#tag/invitations) to order these reports.
        - Employment Verifications, Education Verifications, and Credit Checks may not be initiated using the `/reports` API. Please use the [`/invitations` API](#tag/invitations) to initiate the [Checkr-Hosted Apply Flow](/#section/Getting-Started/Create-an-Invitation) when ordering background checks that include any of these screening types.
        - Creating a Report which includes an Occupational Health or Drug
        Check will automatically issue an email invitation to the candidate to schedule their appointment at a clinic of their choice.


        POST /reports

        Args:
            node: <font color="red">Required</font> for hierarchy-enabled accounts.

        `custom_id` of the associated node.

            self_disclosures: Array of SelfDisclosures

        **Note:** Self Disclosures may not be added, updated, or deleted after a Report has been created. The information provided in a Self Disclosure will not be included in the completed Report, and may be retrieved using [GET](#operation/getReport) `/v1/reports/{id}?include=documents`. See the [Documents](#tag/Documents) resource for more information.

        Removing the requirement for the description, date, and location parameters greatly reduces the value of Self Disclosures. If your system mandates that these parameters be optional, work with your Checkr Customer Success Manager to disable the requirement.

            tags: Array of tags for the Report.
            work_locations: <font color="red">Required</font> for hierarchy-enabled accounts.

        Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.

            candidate_id: ID of the Candidate screened.
            package: `slug` of the associated package.
        Example: `driver_pro`

            request_options: Additional options to customize the HTTP request

        Returns:
            Report was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.create(
            candidate_id="e44aa283528e6fde7d542194", package="string"
        )
        ```
        """
        _json = to_encodable(
            item={
                "node": node,
                "self_disclosures": self_disclosures,
                "tags": tags,
                "work_locations": work_locations,
                "candidate_id": candidate_id,
                "package": package,
            },
            dump_with=params._SerializerReportsCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/reports",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Report,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        id: str,
        adjudication: typing.Union[
            typing.Optional[typing_extensions.Literal["engaged"]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        package: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Report:
        """
        Update an existing Report

        Updates the `package` or `adjudication` for an existing Report resource.

        Use this endpoint to update reports which include the candidate's Social Security Number. To update a Report which does not include an SSN, first use the [update Candidate](#operation/updateCandidate) request to add the candidate’s SSN before updating the report.

        Either `package` or `adjudication` is required.

        <b>Note: </b>This endpoint may also be used to update international reports for candidates which do not include an SSN.
        <div class="alert alert-info">

          **Note**: The Package of a Report cannot be updated if it has an Adverse Action with the status: `complete` or `dispute`. To proceed, cancel the Adverse Action or create a new Report.

        </div>


        POST /reports/{id}

        Args:
            adjudication: typing_extensions.Literal["engaged"]
            package: Slug of the Package.

            id: The Report's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Report was successfully updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.update(
            id="string", adjudication="engaged", package="driver_pro"
        )
        ```
        """
        _json = to_encodable(
            item={"adjudication": adjudication, "package": package},
            dump_with=params._SerializerReportsUpdateBody,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/reports/{id}",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Report,
            request_options=request_options or default_request_options(),
        )
