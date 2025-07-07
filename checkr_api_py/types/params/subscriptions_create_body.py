import pydantic
import typing
import typing_extensions

from .work_location import WorkLocation, _SerializerWorkLocation


class SubscriptionsCreateBody(typing_extensions.TypedDict):
    """
    SubscriptionsCreateBody
    """

    candidate_id: typing_extensions.Required[str]
    """
    ID of the candidate being screened.
    """

    interval_count: typing_extensions.NotRequired[int]
    """
    The number of intervals between each recurrent background check.
    """

    interval_unit: typing_extensions.NotRequired[
        typing_extensions.Literal["day", "month", "week", "year"]
    ]
    """
    Interval at which the subscription will repeat.
    """

    node: typing_extensions.NotRequired[str]
    """
    <font color="red">Required</font> for hierarchy-enabled accounts.
    
    `custom_id` of the associated node.
    
    """

    package: typing_extensions.Required[str]
    """
    `slug` of the associated package.
    
    """

    start_date: typing_extensions.Required[str]
    """
    Start date for the subscription. This is the date on which the subscription will begin, and the first time the report will be run.
    """

    work_locations: typing_extensions.NotRequired[typing.List[WorkLocation]]
    """
    <font color="red">Required</font> for hierarchy-enabled accounts.
    Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.
    
    """


class _SerializerSubscriptionsCreateBody(pydantic.BaseModel):
    """
    Serializer for SubscriptionsCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    candidate_id: str = pydantic.Field(
        alias="candidate_id",
    )
    interval_count: typing.Optional[int] = pydantic.Field(
        alias="interval_count", default=None
    )
    interval_unit: typing.Optional[
        typing_extensions.Literal["day", "month", "week", "year"]
    ] = pydantic.Field(alias="interval_unit", default=None)
    node: typing.Optional[str] = pydantic.Field(alias="node", default=None)
    package: str = pydantic.Field(
        alias="package",
    )
    start_date: str = pydantic.Field(
        alias="start_date",
    )
    work_locations: typing.Optional[typing.List[_SerializerWorkLocation]] = (
        pydantic.Field(alias="work_locations", default=None)
    )
