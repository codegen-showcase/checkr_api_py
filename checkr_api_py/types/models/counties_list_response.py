import pydantic
import typing

from .counties_list_response_additional_props import CountiesListResponseAdditionalProps


class CountiesListResponse(pydantic.BaseModel):
    """
    CountiesListResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, CountiesListResponseAdditionalProps]
