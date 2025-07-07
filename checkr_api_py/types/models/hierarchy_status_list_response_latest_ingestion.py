import pydantic
import typing


class HierarchyStatusListResponseLatestIngestion(pydantic.BaseModel):
    """
    HierarchyStatusListResponseLatestIngestion
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    errors: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="errors", default=None
    )
    """
    All error messages produced by the last hierarchy ingestion request.
    """
    successful: typing.Optional[bool] = pydantic.Field(alias="successful", default=None)
    """
    If `true`, the last hierarchy ingestion request contained no errors.
    """
    sync_id: typing.Optional[str] = pydantic.Field(alias="sync_id", default=None)
    """
    The `sync_id` of the last fully-processed ingestion request. `null` if no requests have processed.
    """
    time: typing.Optional[str] = pydantic.Field(alias="time", default=None)
    """
    The date and time of the start of the last fully-processed ingestion request. `null` if no requests have processed.
    """
