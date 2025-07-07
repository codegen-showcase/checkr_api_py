import pydantic
import typing

from .motor_vehicle_report_license_reports_item_medical_certificates_item_examiner import (
    MotorVehicleReportLicenseReportsItemMedicalCertificatesItemExaminer,
)


class MotorVehicleReportLicenseReportsItemMedicalCertificatesItem(pydantic.BaseModel):
    """
    MotorVehicleReportLicenseReportsItemMedicalCertificatesItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    examiner: typing.Optional[
        MotorVehicleReportLicenseReportsItemMedicalCertificatesItemExaminer
    ] = pydantic.Field(alias="examiner", default=None)
    expiration_date: typing.Optional[str] = pydantic.Field(
        alias="expiration_date", default=None
    )
    issued_date: typing.Optional[str] = pydantic.Field(
        alias="issued_date", default=None
    )
    self_certification: typing.Optional[str] = pydantic.Field(
        alias="self_certification", default=None
    )
    status: typing.Optional[str] = pydantic.Field(alias="status", default=None)
