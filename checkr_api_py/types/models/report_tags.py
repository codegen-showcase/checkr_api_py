import pydantic
import typing
import typing_extensions

from .report_tags_data_item import ReportTagsDataItem


class ReportTags(pydantic.BaseModel):
    """
    ReportTags
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    count: typing.Optional[float] = pydantic.Field(alias="count", default=None)
    data: typing.Optional[typing.List[ReportTagsDataItem]] = pydantic.Field(
        alias="data", default=None
    )
    object: typing.Optional[typing_extensions.Literal["list"]] = pydantic.Field(
        alias="object", default=None
    )
