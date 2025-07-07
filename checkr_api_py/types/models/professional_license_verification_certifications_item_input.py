import pydantic
import typing


class ProfessionalLicenseVerificationCertificationsItemInput(pydantic.BaseModel):
    """
    Candidate input for license verification.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    additional_text: typing.Optional[str] = pydantic.Field(
        alias="additional_text", default=None
    )
    """
    Additional information provided by the candidate for their manually entered license.
    """
    certification_issued_to: typing.Optional[str] = pydantic.Field(
        alias="certification_issued_to", default=None
    )
    """
    Candidate name used in application for professional license verification.
    """
    certification_issuer: typing.Optional[str] = pydantic.Field(
        alias="certification_issuer", default=None
    )
    """
    Certifying organization that issued the license. For example: "California: General".
    """
    certification_issuer_website: typing.Optional[str] = pydantic.Field(
        alias="certification_issuer_website", default=None
    )
    """
    Certifying organization's website.
    """
    license_number: typing.Optional[str] = pydantic.Field(
        alias="license_number", default=None
    )
    """
    Professional License Number.
    """
    license_type: typing.Optional[str] = pydantic.Field(
        alias="license_type", default=None
    )
    """
    Professional License type, as provided by the certification's issuer.
    """
