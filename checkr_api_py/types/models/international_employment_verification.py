import pydantic
import typing
import typing_extensions

from .international_employment_verification_records_item import (
    InternationalEmploymentVerificationRecordsItem,
)


class InternationalEmploymentVerification(pydantic.BaseModel):
    """
    InternationalEmploymentVerification
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

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
    result: typing.Optional[typing_extensions.Literal["clear", "consider"]] = (
        pydantic.Field(alias="result", default=None)
    )
    """
    Result of the screening.
    """
    status: typing.Optional[
        typing_extensions.Literal["canceled", "complete", "pending", "suspended"]
    ] = pydantic.Field(alias="status", default=None)
    """
    Status of the screening.
    
    """
    turnaround_time: typing.Optional[typing.Any] = pydantic.Field(
        alias="turnaround_time", default=None
    )
    uri: typing.Optional[typing.Any] = pydantic.Field(alias="uri", default=None)
    records: typing.Optional[
        typing.List[InternationalEmploymentVerificationRecordsItem]
    ] = pydantic.Field(alias="records", default=None)
    """
    Array of CandidateEmploymentHistory objects.
    """
