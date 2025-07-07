import pydantic
import typing
import typing_extensions


class SubscriptionCanceled(pydantic.BaseModel):
    """
    SubscriptionCanceled
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
