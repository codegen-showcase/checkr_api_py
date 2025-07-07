import pydantic
import typing
import typing_extensions

from .work_location import WorkLocation, _SerializerWorkLocation


class SubscriptionsUpdateBody(typing_extensions.TypedDict):
    """
    SubscriptionsUpdateBody
    """

    candidate_id: typing_extensions.NotRequired[str]
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
    `custom_id` of the associated node.
    
    """

    package: typing_extensions.NotRequired[str]
    """
    Package to run for the Report.
    """

    start_date: typing_extensions.NotRequired[str]
    """
    Start date for the subscription. This is the date on which the subscription will begin, and the first time the report will be run.
    """

    work_locations: typing_extensions.NotRequired[typing.List[WorkLocation]]
    """
    Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.
    
    """


class _SerializerSubscriptionsUpdateBody(pydantic.BaseModel):
    """
    Serializer for SubscriptionsUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    candidate_id: typing.Optional[str] = pydantic.Field(
        alias="candidate_id", default=None
    )
    interval_count: typing.Optional[int] = pydantic.Field(
        alias="interval_count", default=None
    )
    interval_unit: typing.Optional[
        typing_extensions.Literal["day", "month", "week", "year"]
    ] = pydantic.Field(alias="interval_unit", default=None)
    node: typing.Optional[str] = pydantic.Field(alias="node", default=None)
    package: typing.Optional[str] = pydantic.Field(alias="package", default=None)
    start_date: typing.Optional[str] = pydantic.Field(alias="start_date", default=None)
    work_locations: typing.Optional[typing.List[_SerializerWorkLocation]] = (
        pydantic.Field(alias="work_locations", default=None)
    )
