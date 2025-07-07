import pydantic
import typing

from .county import County


class CountiesListResponseAdditionalProps(pydantic.BaseModel):
    """
    An array of counties
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    counties: typing.Optional[typing.List[County]] = pydantic.Field(
        alias="counties", default=None
    )
