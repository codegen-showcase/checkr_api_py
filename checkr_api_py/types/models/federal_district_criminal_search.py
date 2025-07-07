import pydantic
import typing
import typing_extensions

from .federal_district_criminal_search_filtered_by_positive_adjudication_records_item import (
    FederalDistrictCriminalSearchFilteredByPositiveAdjudicationRecordsItem,
)
from .federal_district_criminal_search_records_hidden_by_assess_item import (
    FederalDistrictCriminalSearchRecordsHiddenByAssessItem,
)
from .federal_district_criminal_search_records_item import (
    FederalDistrictCriminalSearchRecordsItem,
)


class FederalDistrictCriminalSearch(pydantic.BaseModel):
    """
    FederalDistrictCriminalSearch
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    assessment: typing.Optional[
        typing_extensions.Literal["eligible", "escalated", "review"]
    ] = pydantic.Field(alias="assessment", default=None)
    """
    The assessment for this screening. This field will be non-null only for Assess-enabled accounts. For accounts with Assess enabled, it will be null for reports completed before Assess was enabled, and null for a short time after report completion while the account's Assess rules are applied.
    
    """
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
    filtered_by_positive_adjudication_records: typing.Optional[
        typing.List[
            FederalDistrictCriminalSearchFilteredByPositiveAdjudicationRecordsItem
        ]
    ] = pydantic.Field(alias="filtered_by_positive_adjudication_records", default=None)
    """
    Array of CriminalRecord objects filtered out by your account’s Positive Adjudication Matrix.
    """
    records: typing.Optional[typing.List[FederalDistrictCriminalSearchRecordsItem]] = (
        pydantic.Field(alias="records", default=None)
    )
    """
    Array of CriminalRecord objects.
    """
    records_hidden_by_assess: typing.Optional[
        typing.List[FederalDistrictCriminalSearchRecordsHiddenByAssessItem]
    ] = pydantic.Field(alias="records_hidden_by_assess", default=None)
    """
    Array of CriminalRecord objects filtered out by your account’s Assess configuration.
    """
