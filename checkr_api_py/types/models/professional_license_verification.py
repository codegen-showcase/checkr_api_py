import pydantic
import typing
import typing_extensions

from .document import Document
from .professional_license_verification_certifications_item import (
    ProfessionalLicenseVerificationCertificationsItem,
)


class ProfessionalLicenseVerification(pydantic.BaseModel):
    """
    ProfessionalLicenseVerification
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
    result: typing.Optional[typing_extensions.Literal["clear", "consider"]] = (
        pydantic.Field(alias="result", default=None)
    )
    """
    if `clear`, a valid active license was found matching the candidate's PII.
    """
    status: typing.Optional[
        typing_extensions.Literal["clear", "consider", "pending"]
    ] = pydantic.Field(alias="status", default=None)
    """
    if `clear` a valid active license was found matching the candidate's PII.
    """
    turnaround_time: typing.Optional[typing.Any] = pydantic.Field(
        alias="turnaround_time", default=None
    )
    uri: typing.Optional[typing.Any] = pydantic.Field(alias="uri", default=None)
    certifications: typing.Optional[
        typing.List[ProfessionalLicenseVerificationCertificationsItem]
    ] = pydantic.Field(alias="certifications", default=None)
    """
    An array of candidate input objects and license verification results objects.
    """
    documents: typing.Optional[typing.List[Document]] = pydantic.Field(
        alias="documents", default=None
    )
    """
    An array of documents captured for the Professional License Verification.
    """
