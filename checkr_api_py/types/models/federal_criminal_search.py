import pydantic
import typing
import typing_extensions

from .federal_criminal_search_filtered_by_positive_adjudication_records_item import (
    FederalCriminalSearchFilteredByPositiveAdjudicationRecordsItem,
)
from .federal_criminal_search_records_item import FederalCriminalSearchRecordsItem


class FederalCriminalSearch(pydantic.BaseModel):
    """
    FederalCriminalSearch
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cancellation_reason: typing.Optional[str] = pydantic.Field(
        alias="cancellation_reason", default=None
    )
    """
    See [cancellation reasons](#section/Reference/Cancellation-Reasons) section for possible values.
    """
    cancellation_reason_description: typing.Optional[str] = pydantic.Field(
        alias="cancellation_reason_description", default=None
    )
    """
    See [cancellation reasons](#section/Reference/Cancellation-Reasons) section for possible values.
    """
    completed_at: typing.Optional[str] = pydantic.Field(
        alias="completed_at", default=None
    )
    """
    Time at which the screening was completed.
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the screening was created.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    object: typing.Optional[typing.Any] = pydantic.Field(alias="object", default=None)
    result: typing.Optional[typing.Any] = pydantic.Field(alias="result", default=None)
    status: typing.Optional[typing.Any] = pydantic.Field(alias="status", default=None)
    turnaround_time: typing.Optional[typing.Any] = pydantic.Field(
        alias="turnaround_time", default=None
    )
    uri: typing.Optional[typing.Any] = pydantic.Field(alias="uri", default=None)
    assessment: typing.Optional[
        typing_extensions.Literal["eligible", "escalated", "review"]
    ] = pydantic.Field(alias="assessment", default=None)
    """
    The assessment for this screening. This field will be non-null only for Assess-enabled accounts. For accounts with Assess enabled, it will be null for reports completed before Assess was enabled, and null for a short time after report completion while the account's Assess rules are applied.
    
    """
    filtered_by_positive_adjudication_records: typing.Optional[
        typing.List[FederalCriminalSearchFilteredByPositiveAdjudicationRecordsItem]
    ] = pydantic.Field(alias="filtered_by_positive_adjudication_records", default=None)
    """
    Array of CriminalRecord objects filtered out by your account’s Positive Adjudication Matrix or by your account’s Assess configuration.
    """
    records: typing.Optional[typing.List[FederalCriminalSearchRecordsItem]] = (
        pydantic.Field(alias="records", default=None)
    )
    """
    Array of CriminalRecord objects.
    """
