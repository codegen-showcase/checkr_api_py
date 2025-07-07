import pydantic
import typing
import typing_extensions

from .motor_vehicle_report_license_reports_item_accidents_item import (
    MotorVehicleReportLicenseReportsItemAccidentsItem,
)
from .motor_vehicle_report_license_reports_item_medical_certificates_item import (
    MotorVehicleReportLicenseReportsItemMedicalCertificatesItem,
)
from .motor_vehicle_report_license_reports_item_suspensions_item import (
    MotorVehicleReportLicenseReportsItemSuspensionsItem,
)
from .motor_vehicle_report_license_reports_item_violations_item import (
    MotorVehicleReportLicenseReportsItemViolationsItem,
)


class MotorVehicleReportLicenseReportsItem(pydantic.BaseModel):
    """
    MotorVehicleReportLicenseReportsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    accidents: typing.Optional[
        typing.List[MotorVehicleReportLicenseReportsItemAccidentsItem]
    ] = pydantic.Field(alias="accidents", default=None)
    """
    Array of Accident objects.
    """
    class_: typing.Optional[str] = pydantic.Field(alias="class", default=None)
    """
    Class of the license as returned by the DMV.
    """
    current_license: typing.Optional[bool] = pydantic.Field(
        alias="current_license", default=None
    )
    """
    True when this is the current license in use
    """
    dob: typing.Optional[str] = pydantic.Field(alias="dob", default=None)
    """
    Date of Birth of the individual the license was issued to as returned by the DMV.
    """
    endorsements: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="endorsements", default=None
    )
    """
    Array of Endorsements
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
    issued_date: typing.Optional[str] = pydantic.Field(
        alias="issued_date", default=None
    )
    """
    Date on which the license was issued.
    """
    medical_certificates: typing.Optional[
        typing.List[MotorVehicleReportLicenseReportsItemMedicalCertificatesItem]
    ] = pydantic.Field(alias="medical_certificates", default=None)
    """
    Array of Medical Certificate objects. Only available for commercial MVR.
    """
    number: typing.Optional[str] = pydantic.Field(alias="number", default=None)
    """
    Candidate’s driver’s license number.
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
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    """
    Candidate’s driver’s license state of issue.
    """
    status: typing.Optional[str] = pydantic.Field(alias="status", default=None)
    """
    Status of the license as returned by the DMV if found, or status indicating the license is not found or not available.
    """
    suspensions: typing.Optional[
        typing.List[MotorVehicleReportLicenseReportsItemSuspensionsItem]
    ] = pydantic.Field(alias="suspensions", default=None)
    """
    Array of Suspension objects.
    """
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
    """
    Type of the license as returned by the DMV.
    """
    violations: typing.Optional[
        typing.List[MotorVehicleReportLicenseReportsItemViolationsItem]
    ] = pydantic.Field(alias="violations", default=None)
    """
    Array of Violation objects.
    """
