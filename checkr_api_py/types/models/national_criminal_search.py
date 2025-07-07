import pydantic
import typing

from .national_criminal_search_records_item import NationalCriminalSearchRecordsItem


class NationalCriminalSearch(pydantic.BaseModel):
    """
    NationalCriminalSearch
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
    result: typing.Optional[str] = pydantic.Field(alias="result", default=None)
    """
    Outcome of the screening.  Screenings completed before April 2021 may return `"clear"` or `"consider"`.
    """
    status: typing.Optional[typing.Any] = pydantic.Field(alias="status", default=None)
    turnaround_time: typing.Optional[typing.Any] = pydantic.Field(
        alias="turnaround_time", default=None
    )
    uri: typing.Optional[typing.Any] = pydantic.Field(alias="uri", default=None)
    records: typing.Optional[typing.List[NationalCriminalSearchRecordsItem]] = (
        pydantic.Field(alias="records", default=None)
    )
    """
    Array of CriminalRecord objects.
    """
