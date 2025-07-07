import pydantic
import typing_extensions


class ReportsTagsCreateBody(typing_extensions.TypedDict):
    """
    ReportsTagsCreateBody
    """

    tag: typing_extensions.Required[str]


class _SerializerReportsTagsCreateBody(pydantic.BaseModel):
    """
    Serializer for ReportsTagsCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tag: str = pydantic.Field(
        alias="tag",
    )
