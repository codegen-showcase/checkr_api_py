import pydantic
import typing
import typing_extensions

from .school import School


class CandidatesSchoolsListResponse(pydantic.BaseModel):
    """
    CandidatesSchoolsListResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[School]] = pydantic.Field(
        alias="data", default=None
    )
    next_href: typing.Optional[str] = pydantic.Field(alias="next_href", default=None)
    object: typing.Optional[typing_extensions.Literal["list"]] = pydantic.Field(
        alias="object", default=None
    )
    """
    A list
    """
