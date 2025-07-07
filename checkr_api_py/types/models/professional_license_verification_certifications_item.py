import pydantic
import typing

from .document import Document
from .professional_license_verification_certifications_item_input import (
    ProfessionalLicenseVerificationCertificationsItemInput,
)
from .professional_license_verification_certifications_item_result import (
    ProfessionalLicenseVerificationCertificationsItemResult,
)


class ProfessionalLicenseVerificationCertificationsItem(pydantic.BaseModel):
    """
    ProfessionalLicenseVerificationCertificationsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    candidate_documents: typing.Optional[typing.List[Document]] = pydantic.Field(
        alias="candidate_documents", default=None
    )
    """
    An array of documents uploaded by the candidate
    """
    input: typing.Optional[ProfessionalLicenseVerificationCertificationsItemInput] = (
        pydantic.Field(alias="input", default=None)
    )
    """
    Candidate input for license verification.
    """
    result: typing.Optional[ProfessionalLicenseVerificationCertificationsItemResult] = (
        pydantic.Field(alias="result", default=None)
    )
    """
    Certification result.
    """
