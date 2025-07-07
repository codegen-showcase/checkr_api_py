import pydantic
import typing


class MotorVehicleReportLicenseReportsItemMedicalCertificatesItemExaminer(
    pydantic.BaseModel
):
    """
    MotorVehicleReportLicenseReportsItemMedicalCertificatesItemExaminer
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    full_name: typing.Optional[str] = pydantic.Field(alias="full_name", default=None)
    license_number: typing.Optional[str] = pydantic.Field(
        alias="license_number", default=None
    )
    license_state: typing.Optional[str] = pydantic.Field(
        alias="license_state", default=None
    )
    registration_number: typing.Optional[str] = pydantic.Field(
        alias="registration_number", default=None
    )
