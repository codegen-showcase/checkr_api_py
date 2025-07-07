import pydantic
import typing
import typing_extensions

from .reports_tags_create_response_data_item import ReportsTagsCreateResponseDataItem


class ReportsTagsCreateResponse(pydantic.BaseModel):
    """
    ReportsTagsCreateResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    count: typing.Optional[float] = pydantic.Field(alias="count", default=None)
    data: typing.Optional[typing.List[ReportsTagsCreateResponseDataItem]] = (
        pydantic.Field(alias="data", default=None)
    )
    object: typing.Optional[typing_extensions.Literal["list"]] = pydantic.Field(
        alias="object", default=None
    )
