import pydantic
import typing
import typing_extensions


class ReportsTagsUpdateBody(typing_extensions.TypedDict):
    """
    ReportsTagsUpdateBody
    """

    tags: typing_extensions.Required[typing.List[str]]


class _SerializerReportsTagsUpdateBody(pydantic.BaseModel):
    """
    Serializer for ReportsTagsUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tags: typing.List[str] = pydantic.Field(
        alias="tags",
    )
