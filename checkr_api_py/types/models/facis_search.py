import pydantic
import typing
import typing_extensions

from .facis_record import FacisRecord


class FacisSearch(pydantic.BaseModel):
    """
    FacisSearch
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
    object: typing.Optional[typing_extensions.Literal["facis_search"]] = pydantic.Field(
        alias="object", default=None
    )
    records: typing.Optional[typing.List[FacisRecord]] = pydantic.Field(
        alias="records", default=None
    )
    """
    Array of FacisRecord objects.
    """
    result: typing.Optional[typing.Any] = pydantic.Field(alias="result", default=None)
    status: typing.Optional[typing.Any] = pydantic.Field(alias="status", default=None)
    subtype: typing.Optional[typing_extensions.Literal["1", "3"]] = pydantic.Field(
        alias="subtype", default=None
    )
    """
    Level number representing the breadth of data sources searched
    """
    turnaround_time: typing.Optional[int] = pydantic.Field(
        alias="turnaround_time", default=None
    )
    """
    Number of seconds the screening took to complete, calculated from `created_at` to `completed_at`.
    """
