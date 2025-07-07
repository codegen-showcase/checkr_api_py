import pydantic
import typing
import typing_extensions


class InternationalAdverseMediaSearch(pydantic.BaseModel):
    """
    InternationalAdverseMediaSearch
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
    turnaround_time: typing.Optional[int] = pydantic.Field(
        alias="turnaround_time", default=None
    )
    """
    Number of seconds the screening took to complete, calculated from `created_at` to `completed_at`.
    """
    uri: typing.Optional[typing.Any] = pydantic.Field(alias="uri", default=None)
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    ISO country code of the jurisdiction where the search was run
    """
    pdf_url: typing.Optional[str] = pydantic.Field(alias="pdf_url", default=None)
    """
    URL to PDF document containing screening result details
    """
