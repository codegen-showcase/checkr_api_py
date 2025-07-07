import pydantic
import typing
import typing_extensions

from .work_location import WorkLocation


class ContinuousCheck(pydantic.BaseModel):
    """
    ContinuousCheck
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    candidate_id: typing.Optional[str] = pydantic.Field(
        alias="candidate_id", default=None
    )
    """
    ID of the Candidate enrolled in Continuous Check.
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the Continuous Check was created.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    node: typing.Optional[str] = pydantic.Field(alias="node", default=None)
    """
    Custom ID of the Node associated with the Continuous Check.
    """
    object: typing.Optional[typing_extensions.Literal["continuous_check"]] = (
        pydantic.Field(alias="object", default=None)
    )
    type_: typing.Optional[typing_extensions.Literal["criminal", "mvr"]] = (
        pydantic.Field(alias="type", default=None)
    )
    """
    Type of Continuous Check.
    """
    work_locations: typing.Optional[typing.List[WorkLocation]] = pydantic.Field(
        alias="work_locations", default=None
    )
    """
    Array of work locations associated with the Continuous Check.
    """
