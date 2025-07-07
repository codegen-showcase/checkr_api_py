import pydantic
import typing
import typing_extensions

from .professional_reference_verification_questions_item import (
    ProfessionalReferenceVerificationQuestionsItem,
)


class ProfessionalReferenceVerification(pydantic.BaseModel):
    """
    ProfessionalReferenceVerification
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
    id: typing.Optional[typing.Any] = pydantic.Field(alias="id", default=None)
    object: typing.Optional[typing.Any] = pydantic.Field(alias="object", default=None)
    result: typing.Optional[typing.Any] = pydantic.Field(alias="result", default=None)
    status: typing.Optional[typing.Any] = pydantic.Field(alias="status", default=None)
    turnaround_time: typing.Optional[typing.Any] = pydantic.Field(
        alias="turnaround_time", default=None
    )
    uri: typing.Optional[typing.Any] = pydantic.Field(alias="uri", default=None)
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    Professional Reference's email address.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Professional Reference's full name.
    """
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    Professional Reference's phone number.
    """
    questions: typing.Optional[
        typing.List[ProfessionalReferenceVerificationQuestionsItem]
    ] = pydantic.Field(alias="questions", default=None)
    """
    Array of questions and answers received from Professional Reference.
    """
    relationship: typing.Optional[str] = pydantic.Field(
        alias="relationship", default=None
    )
    """
    Relationship between Candidate and Professional Reference.
    """
