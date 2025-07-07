import pydantic
import typing


class InternationalEmploymentVerificationRecordsItemResultPosition(pydantic.BaseModel):
    """
    InternationalEmploymentVerificationRecordsItemResultPosition
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    comments: typing.Optional[typing.Any] = pydantic.Field(
        alias="comments", default=None
    )
    ignored: typing.Optional[typing.Any] = pydantic.Field(alias="ignored", default=None)
    verified: typing.Optional[typing.Any] = pydantic.Field(
        alias="verified", default=None
    )
