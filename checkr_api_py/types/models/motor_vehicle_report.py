import pydantic
import typing
import typing_extensions

from .motor_vehicle_report_accidents_item import MotorVehicleReportAccidentsItem
from .motor_vehicle_report_custom_rules import MotorVehicleReportCustomRules
from .motor_vehicle_report_license_reports_item import (
    MotorVehicleReportLicenseReportsItem,
)
from .motor_vehicle_report_suspensions_item import MotorVehicleReportSuspensionsItem
from .motor_vehicle_report_violations_item import MotorVehicleReportViolationsItem


class MotorVehicleReport(pydantic.BaseModel):
    """
    MotorVehicleReport
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    assessment: typing.Optional[
        typing_extensions.Literal["eligible", "escalated", "review"]
    ] = pydantic.Field(alias="assessment", default=None)
    """
    The assessment for this screening. This field will be non-null only for Assess-enabled accounts. For accounts with Assess enabled, it will be null for reports completed before Assess was enabled, and null for a short time after report completion while the account's Assess rules are applied.
    
    """
    cancellation_reason: typing.Optional[str] = pydantic.Field(
        alias="cancellation_reason", default=None
    )
    """
    See [cancellation reasons](#section/Reference/Cancellation-Reasons) section for possible values.
    """
    cancellation_reason_description: typing.Optional[str] = pydantic.Field(
        alias="cancellation_reason_description", default=None
    )
    """
    See [cancellation reasons](#section/Reference/Cancellation-Reasons) section for possible values.
    """
    completed_at: typing.Optional[str] = pydantic.Field(
        alias="completed_at", default=None
    )
    """
    Time at which the screening was completed.
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the screening was created.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    object: typing.Optional[typing.Any] = pydantic.Field(alias="object", default=None)
    result: typing.Optional[typing.Any] = pydantic.Field(alias="result", default=None)
    status: typing.Optional[typing.Any] = pydantic.Field(alias="status", default=None)
    turnaround_time: typing.Optional[typing.Any] = pydantic.Field(
        alias="turnaround_time", default=None
    )
    uri: typing.Optional[typing.Any] = pydantic.Field(alias="uri", default=None)
    accidents: typing.Optional[typing.List[MotorVehicleReportAccidentsItem]] = (
        pydantic.Field(alias="accidents", default=None)
    )
    """
    Array of Accident objects.
    """
    covid_extension: typing.Optional[bool] = pydantic.Field(
        alias="covid_extension", default=None
    )
    """
    Returns `true` when the MVR report has been automatically adjusted for DMV license expiration date extension. This field will be returned in the response data for impacted reports only.
    """
    custom_rules: typing.Optional[MotorVehicleReportCustomRules] = pydantic.Field(
        alias="custom_rules", default=None
    )
    """
    Object with custom rules applied to generate this MVR.
    """
    dob: typing.Optional[str] = pydantic.Field(alias="dob", default=None)
    """
    Date of Birth of the individual the license was issued to as returned by the DMV.
    """
    experience_failed: typing.Optional[bool] = pydantic.Field(
        alias="experience_failed", default=None
    )
    """
    If true, the MVR has an unsatisfied StrictExperience rule.
    """
    expiration_date: typing.Optional[str] = pydantic.Field(
        alias="expiration_date", default=None
    )
    """
    Date on which the license expires.
    """
    first_issued_date: typing.Optional[str] = pydantic.Field(
        alias="first_issued_date", default=None
    )
    """
    Date on which the license was first issued. Used to determine if the candidate meets minimum experience requirements.
    """
    full_name: typing.Optional[str] = pydantic.Field(alias="full_name", default=None)
    """
    Candidate’s full name, as listed with the DMV.
    """
    inferred_issued_date: typing.Optional[str] = pydantic.Field(
        alias="inferred_issued_date", default=None
    )
    """
    Checkr-inferred license issued date based on data returned by the DMV.
    """
    issued_date: typing.Optional[str] = pydantic.Field(
        alias="issued_date", default=None
    )
    """
    Date on which the license was issued.
    """
    license_class: typing.Optional[str] = pydantic.Field(
        alias="license_class", default=None
    )
    """
    Class of the license as returned by the DMV.
    """
    license_number: typing.Optional[str] = pydantic.Field(
        alias="license_number", default=None
    )
    """
    Candidate’s driver’s license number.
    """
    license_reports: typing.Optional[
        typing.List[MotorVehicleReportLicenseReportsItem]
    ] = pydantic.Field(alias="license_reports", default=None)
    """
    Array of license reports
    """
    license_state: typing.Optional[str] = pydantic.Field(
        alias="license_state", default=None
    )
    """
    Candidate’s driver’s license state of issue.
    """
    license_status: typing.Optional[str] = pydantic.Field(
        alias="license_status", default=None
    )
    """
    Status of the license as returned by the DMV if found, or status indicating the license is not found or not available.
    """
    license_type: typing.Optional[str] = pydantic.Field(
        alias="license_type", default=None
    )
    """
    Type of the license as returned by the DMV.
    """
    not_found: typing.Optional[bool] = pydantic.Field(alias="not_found", default=None)
    """
    No license found by the DMV matching the candidate's license number/state and PII.
    """
    previous_license_number: typing.Optional[str] = pydantic.Field(
        alias="previous_license_number", default=None
    )
    """
    Candidate’s previous driver’s license number.
    """
    previous_license_state: typing.Optional[str] = pydantic.Field(
        alias="previous_license_state", default=None
    )
    """
    Candidate’s previous driver’s license state of issue.
    """
    privilege_to_drive: typing.Optional[
        typing_extensions.Literal["invalid", "valid"]
    ] = pydantic.Field(alias="privilege_to_drive", default=None)
    """
    Displays the validity of the license, as determined by the returned `license_status`, `license_class`, and `expiration_date`. If one or more of these three fields indicates that the license is not valid, `privilege_to_drive` is `invalid`.
    """
    restrictions: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="restrictions", default=None
    )
    """
    Array of restrictions, as returned by the individual states' DMV.
    """
    suspensions: typing.Optional[typing.List[MotorVehicleReportSuspensionsItem]] = (
        pydantic.Field(alias="suspensions", default=None)
    )
    """
    Array of Suspension objects.
    """
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
    """
    MVR type.
    """
    violations: typing.Optional[typing.List[MotorVehicleReportViolationsItem]] = (
        pydantic.Field(alias="violations", default=None)
    )
    """
    Array of Violation objects.
    """
