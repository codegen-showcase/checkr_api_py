import pydantic
import typing


class EducationVerificationRecordsItemEventsItem(pydantic.BaseModel):
    """
    EducationVerificationRecordsItemEventsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    text: typing.Optional[str] = pydantic.Field(alias="text", default=None)
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
