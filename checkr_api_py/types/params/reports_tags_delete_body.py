import pydantic
import typing_extensions


class ReportsTagsDeleteBody(typing_extensions.TypedDict):
    """
    ReportsTagsDeleteBody
    """

    tag: typing_extensions.Required[str]


class _SerializerReportsTagsDeleteBody(pydantic.BaseModel):
    """
    Serializer for ReportsTagsDeleteBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tag: str = pydantic.Field(
        alias="tag",
    )
