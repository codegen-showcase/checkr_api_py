import pydantic
import typing
import typing_extensions

from .geo import Geo


class GeosListResponse(pydantic.BaseModel):
    """
    GeosListResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    count: typing.Optional[int] = pydantic.Field(alias="count", default=None)
    data: typing.Optional[typing.List[Geo]] = pydantic.Field(alias="data", default=None)
    next_href: typing.Optional[str] = pydantic.Field(alias="next_href", default=None)
    object: typing.Optional[typing_extensions.Literal["list"]] = pydantic.Field(
        alias="object", default=None
    )
    """
    A list
    """
    previous_href: typing.Optional[str] = pydantic.Field(
        alias="previous_href", default=None
    )
