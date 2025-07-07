import pydantic
import typing
import typing_extensions

from .report_drug_screening import ReportDrugScreening
from .work_location import WorkLocation


class Report(pydantic.BaseModel):
    """
    Report
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    adjudication: typing.Optional[
        typing_extensions.Literal[
            "engaged", "post_adverse_action", "pre_adverse_action"
        ]
    ] = pydantic.Field(alias="adjudication", default=None)
    """
    The adjudication for the candidate. `Null` if no adjudication has been made.
    
    """
    archived: typing.Optional[bool] = pydantic.Field(alias="archived", default=None)
    """
    Returns `true` if the invitation is archived.
    """
    arrest_search_id: typing.Optional[str] = pydantic.Field(
        alias="arrest_search_id", default=None
    )
    """
    ID of the Arrest Search linked to the report.
    """
    assessment: typing.Optional[
        typing_extensions.Literal["eligible", "escalated", "review"]
    ] = pydantic.Field(alias="assessment", default=None)
    """
    The assessment for the report. This field will be non-null only for Assess-enabled accounts. For accounts with Assess enabled, it will be null for reports completed before Assess was enabled, and null for a short time after report completion while the account's Assess rules are applied.
    
    """
    candidate_id: typing.Optional[str] = pydantic.Field(
        alias="candidate_id", default=None
    )
    """
    ID of the candidate being screened.
    """
    candidate_story_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="candidate_story_ids", default=None
    )
    """
    Array of Candidate Story IDs linked to the Report.
    """
    completed_at: typing.Optional[str] = pydantic.Field(
        alias="completed_at", default=None
    )
    """
    Time at which the report was completed.
    
    """
    county_criminal_search_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="county_criminal_search_ids", default=None
    )
    """
    Array of County Criminal Search IDs linked to the Report.
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the report was created.
    
    """
    document_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="document_ids", default=None
    )
    """
    Array of Document IDs.
    """
    drug_alcohol_clearinghouse_id: typing.Optional[str] = pydantic.Field(
        alias="drug_alcohol_clearinghouse_id", default=None
    )
    """
    ID of the Drug & Alcohol Clearinghouse Search linked to the Report.
    """
    drug_screening: typing.Optional[ReportDrugScreening] = pydantic.Field(
        alias="drug_screening", default=None
    )
    """
    Embedded Drug Screening object
    """
    drug_screening_id: typing.Optional[str] = pydantic.Field(
        alias="drug_screening_id", default=None
    )
    """
    ID of the Drug Screening linked to the report.
    """
    estimated_completion_time: typing.Optional[str] = pydantic.Field(
        alias="estimated_completion_time", default=None
    )
    """
    Date at which the report is predicted to be finished. Despite the date-time format, we only estimate to the date. The time is not relevant.
    
    """
    facis_search_id: typing.Optional[str] = pydantic.Field(
        alias="facis_search_id", default=None
    )
    """
    ID of the FACIS Search linked to the Report.
    """
    federal_civil_search_id: typing.Optional[str] = pydantic.Field(
        alias="federal_civil_search_id", default=None
    )
    """
    ID of the Federal Civil Search linked to the Report.
    """
    federal_criminal_search_id: typing.Optional[str] = pydantic.Field(
        alias="federal_criminal_search_id", default=None
    )
    """
    ID of the Federal Criminal Search linked to the Report.
    """
    federal_district_civil_search_id: typing.Optional[str] = pydantic.Field(
        alias="federal_district_civil_search_id", default=None
    )
    """
    ID of the Federal District Civil Search linked to the Report.
    """
    federal_district_criminal_search_id: typing.Optional[str] = pydantic.Field(
        alias="federal_district_criminal_search_id", default=None
    )
    """
    ID of the Federal District Criminal Search linked to the Report.
    """
    geo_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="geo_ids", default=None
    )
    """
    Array of Geo IDs.
    """
    global_watchlist_search_id: typing.Optional[str] = pydantic.Field(
        alias="global_watchlist_search_id", default=None
    )
    """
    ID of the Global Watchlist Search linked to the Report.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    includes_canceled: typing.Optional[bool] = pydantic.Field(
        alias="includes_canceled", default=None
    )
    """
    Returns `true` if the report includes a canceled screening.
    """
    international_adverse_media_search_ids: typing.Optional[typing.List[str]] = (
        pydantic.Field(alias="international_adverse_media_search_ids", default=None)
    )
    """
    Array of International Adverse Media Search IDs linked to the Report. If no searches exists, this field is omitted.
    """
    international_criminal_searches_v2_ids: typing.Optional[typing.List[str]] = (
        pydantic.Field(alias="international_criminal_searches_v2_ids", default=None)
    )
    """
    Array of International Criminal Search IDs linked to the Report. If no searches exist, this field is omitted.
    """
    international_education_verification_id: typing.Optional[str] = pydantic.Field(
        alias="international_education_verification_id", default=None
    )
    """
    ID of an International Education Verification linked to the Report. If no verification exists, this field is omitted.
    """
    international_employment_verification_id: typing.Optional[str] = pydantic.Field(
        alias="international_employment_verification_id", default=None
    )
    """
    ID of an International Employment Verification linked to the Report. If no verification exists, this field is omitted.
    """
    international_global_watchlist_search_id: typing.Optional[str] = pydantic.Field(
        alias="international_global_watchlist_search_id", default=None
    )
    """
    ID of an International Global Watchlist Search linked to the Report. If no search exists, this field is omitted.
    """
    international_identity_document_validation_id: typing.Optional[str] = (
        pydantic.Field(
            alias="international_identity_document_validation_id", default=None
        )
    )
    """
    ID of an International Identity Document Validation linked to the Report. If no validation exists, this field is omitted.
    """
    motor_vehicle_report_id: typing.Optional[str] = pydantic.Field(
        alias="motor_vehicle_report_id", default=None
    )
    """
    ID of the Motor Vehicle Record Search linked to the Report.
    """
    national_criminal_search_id: typing.Optional[str] = pydantic.Field(
        alias="national_criminal_search_id", default=None
    )
    """
    ID of the National Criminal Search linked to the Report.
    """
    object: typing.Optional[typing_extensions.Literal["report"]] = pydantic.Field(
        alias="object", default=None
    )
    """
    Defines the object type: `report`.
    
    """
    occupational_health_screening_id: typing.Optional[str] = pydantic.Field(
        alias="occupational_health_screening_id", default=None
    )
    """
    ID of the Health Screening linked to the report.
    """
    package: typing.Optional[str] = pydantic.Field(alias="package", default=None)
    """
    Human-readable name of the Package.
    
    """
    personal_reference_verification_ids: typing.Optional[typing.List[str]] = (
        pydantic.Field(alias="personal_reference_verification_ids", default=None)
    )
    """
    Array of Personal Reference Verification IDs linked to the Report.
    """
    professional_license_verification_ids: typing.Optional[typing.List[str]] = (
        pydantic.Field(alias="professional_license_verification_ids", default=None)
    )
    """
    Array of Professional License Verification IDs linked to the Report.
    """
    professional_reference_verification_ids: typing.Optional[typing.List[str]] = (
        pydantic.Field(alias="professional_reference_verification_ids", default=None)
    )
    """
    Array of Professional Reference Verification IDs linked to the Report.
    """
    program_id: typing.Optional[str] = pydantic.Field(alias="program_id", default=None)
    """
    ID of the Program linked to the Report.
    
    """
    result: typing.Optional[typing_extensions.Literal["clear", "consider"]] = (
        pydantic.Field(alias="result", default=None)
    )
    """
    Outcome of the report.
    
    """
    revised_at: typing.Optional[str] = pydantic.Field(alias="revised_at", default=None)
    """
    Time at which the report was revised.
    
    """
    segment_stamps: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="segment_stamps", default=None
    )
    """
    Tier and name of the node the report was ordered with and tier|name information for all its parent nodes.
    
    """
    sex_offender_search_id: typing.Optional[str] = pydantic.Field(
        alias="sex_offender_search_id", default=None
    )
    """
    ID of the Sex Offender Registry Search linked to the Report.
    """
    source: typing.Optional[
        typing_extensions.Literal[
            "api", "continuous_check", "form", "manual_order", "recurrence", "web"
        ]
    ] = pydantic.Field(alias="source", default=None)
    """
    The method used to create the report. <br>`api` created from the Checkr API. <br>`continuous_check` created automatically from a Continuous Check return. <br>`form` created from the Checkr Hosted Invite/Apply flow. <br>`manual_order` created from a manual order (customer enters candidate's PII) originating in the Checkr Dashboard. <br>`recurrence` created from a Subscription. <br>`web` created from <b>Candidates > Order new Report </b> in the Checkr Dashboard.
    """
    ssn_trace_id: typing.Optional[str] = pydantic.Field(
        alias="ssn_trace_id", default=None
    )
    """
    ID of the SSN Trace linked to the Report.
    """
    state_criminal_searches: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="state_criminal_searches", default=None
    )
    """
    Array of State Criminal Search IDs linked to the Report.
    """
    status: typing.Optional[
        typing_extensions.Literal[
            "canceled", "complete", "dispute", "pending", "suspended"
        ]
    ] = pydantic.Field(alias="status", default=None)
    """
    Status of the report.
    
    `canceled` if and only if all screenings, including SSN Trace, within the report were canceled.
    `complete` if at least one screening was completed.
    
    """
    turnaround_time: typing.Optional[int] = pydantic.Field(
        alias="turnaround_time", default=None
    )
    """
    Number of seconds the report took to complete, calculated from `created_at` to `completed_at`.
    """
    upgraded_at: typing.Optional[str] = pydantic.Field(
        alias="upgraded_at", default=None
    )
    """
    Time at which the report was upgraded.
    
    """
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    """
    URI of the resource.
    """
    work_locations: typing.Optional[typing.List[WorkLocation]] = pydantic.Field(
        alias="work_locations", default=None
    )
    """
    Array of work locations set while ordering this report.
    
    """
