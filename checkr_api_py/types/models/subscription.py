import pydantic
import typing
import typing_extensions

from .work_location import WorkLocation


class Subscription(pydantic.BaseModel):
    """
    Subscription
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    canceled_at: typing.Optional[str] = pydantic.Field(
        alias="canceled_at", default=None
    )
    """
    Time at which the Subscription was canceled.
    """
    candidate_id: typing.Optional[str] = pydantic.Field(
        alias="candidate_id", default=None
    )
    """
    ID of the candidate screened.
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the Subscription was created.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    interval_count: typing.Optional[int] = pydantic.Field(
        alias="interval_count", default=None
    )
    """
    The number of intervals between each recurrent background check.
    """
    interval_unit: typing.Optional[
        typing_extensions.Literal["day", "month", "week", "year"]
    ] = pydantic.Field(alias="interval_unit", default=None)
    """
    Interval at which the Subscription will repeat.
    """
    next_occurrence_date: typing.Optional[str] = pydantic.Field(
        alias="next_occurrence_date", default=None
    )
    """
    The next date on which the Subscription will be run. This date is determined based on the `start_date`, `interval_unit`, `interval_count`, and the last date the subscription was run.
    """
    node: typing.Optional[str] = pydantic.Field(alias="node", default=None)
    """
    Node to be used when generating a report for this Subscription.
    """
    object: typing.Optional[typing_extensions.Literal["subscription"]] = pydantic.Field(
        alias="object", default=None
    )
    package: typing.Optional[str] = pydantic.Field(alias="package", default=None)
    """
    Package to run for the Subscription.
    """
    start_date: typing.Optional[str] = pydantic.Field(alias="start_date", default=None)
    """
    Start date for the Subscription. This is the date on which the Subscription will begin, and the first time the report will be run.
    """
    status: typing.Optional[typing_extensions.Literal["active", "inactive"]] = (
        pydantic.Field(alias="status", default=None)
    )
    """
    Status of the Subscription.
    """
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    """
    URI of the resource.
    """
    work_locations: typing.Optional[typing.List[WorkLocation]] = pydantic.Field(
        alias="work_locations", default=None
    )
    """
    Array of work locations to be used when generating a report for this Subscription.
    """
