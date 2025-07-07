import pydantic
import typing
import typing_extensions

from .work_location import WorkLocation, _SerializerWorkLocation


class CandidatesContinuousChecksCreateBody(typing_extensions.TypedDict):
    """
    CandidatesContinuousChecksCreateBody
    """

    node: typing_extensions.NotRequired[str]
    """
    <font color="red">Required</font> for hierarchy-enabled accounts with Nodes.
    
    `custom_id` of the associated node.
    
    """

    type_: typing_extensions.Required[typing_extensions.Literal["criminal", "mvr"]]
    """
    Defines the screening type(s) for this Continuous Check.
    """

    work_locations: typing_extensions.NotRequired[typing.List[WorkLocation]]
    """
    <font color="red">Required</font> for hierarchy-enabled accounts.
    
    Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.
    
    """


class _SerializerCandidatesContinuousChecksCreateBody(pydantic.BaseModel):
    """
    Serializer for CandidatesContinuousChecksCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    node: typing.Optional[str] = pydantic.Field(alias="node", default=None)
    type_: typing_extensions.Literal["criminal", "mvr"] = pydantic.Field(
        alias="type",
    )
    work_locations: typing.Optional[typing.List[_SerializerWorkLocation]] = (
        pydantic.Field(alias="work_locations", default=None)
    )
