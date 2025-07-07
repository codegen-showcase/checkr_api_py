import pydantic
import typing
import typing_extensions

from .work_location import WorkLocation, _SerializerWorkLocation


class ContinuousChecksCreateBody(typing_extensions.TypedDict):
    """
    ContinuousChecksCreateBody
    """

    node: typing_extensions.NotRequired[str]
    """
    `custom_id` of the associated node.
    
    """

    work_locations: typing_extensions.NotRequired[typing.List[WorkLocation]]
    """
    Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.
    
    """


class _SerializerContinuousChecksCreateBody(pydantic.BaseModel):
    """
    Serializer for ContinuousChecksCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    node: typing.Optional[str] = pydantic.Field(alias="node", default=None)
    work_locations: typing.Optional[typing.List[_SerializerWorkLocation]] = (
        pydantic.Field(alias="work_locations", default=None)
    )
