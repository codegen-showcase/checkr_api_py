import pydantic
import typing


class ReportsTagsUpdateResponseDataItem(pydantic.BaseModel):
    """
    ReportsTagsUpdateResponseDataItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
