import pydantic
import typing
import typing_extensions

from .professional_license_verification_certifications_item_result_sub_checks_item import (
    ProfessionalLicenseVerificationCertificationsItemResultSubChecksItem,
)
from .professional_license_verification_certifications_item_result_sub_results_item import (
    ProfessionalLicenseVerificationCertificationsItemResultSubResultsItem,
)


class ProfessionalLicenseVerificationCertificationsItemResult(pydantic.BaseModel):
    """
    Certification result.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    certification_expiration: typing.Optional[str] = pydantic.Field(
        alias="certification_expiration", default=None
    )
    """
    Certification's expiration date in MM/DD/YYYY format. Present only if certification is found.
    """
    certification_issued_to: typing.Optional[str] = pydantic.Field(
        alias="certification_issued_to", default=None
    )
    """
    Certification Holder.
    """
    certification_issuer: typing.Optional[str] = pydantic.Field(
        alias="certification_issuer", default=None
    )
    """
    Certifying organization that issued the license. For example: "California: General".
    """
    certification_issuer_region: typing.Optional[str] = pydantic.Field(
        alias="certification_issuer_region", default=None
    )
    """
    Certifying organization's region or state.
    """
    sub_checks: typing.Optional[
        typing.List[
            ProfessionalLicenseVerificationCertificationsItemResultSubChecksItem
        ]
    ] = pydantic.Field(alias="sub_checks", default=None)
    """
    An array of objects describing the results of specific verification criteria.
    """
    sub_results: typing.Optional[
        typing.List[
            ProfessionalLicenseVerificationCertificationsItemResultSubResultsItem
        ]
    ] = pydantic.Field(alias="sub_results", default=None)
    """
    An array of objects describing the results of verification data.
    """
    verified_by: typing.Optional[typing_extensions.Literal["none", "partner"]] = (
        pydantic.Field(alias="verified_by", default=None)
    )
    """
    Entity that verified the license.
    
    `partner`: Verified by one of Checkr's Professional License partners (most common).<br>
    `none`: Candidate's license was manually entered, and has not been verified.<br>
    
    """
