import pydantic
import typing

from .hierarchy_status_list_response_latest_ingestion import (
    HierarchyStatusListResponseLatestIngestion,
)


class HierarchyStatusListResponse(pydantic.BaseModel):
    """
    HierarchyStatusListResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    hierarchy_pending: typing.Optional[bool] = pydantic.Field(
        alias="hierarchy_pending", default=None
    )
    """
    If `true`, a hierarchy ingestion request is currently processing.
    """
    hierarchy_present: typing.Optional[bool] = pydantic.Field(
        alias="hierarchy_present", default=None
    )
    """
    If `true`, a valid hierarchy exists for the account.
    """
    latest_ingestion: typing.Optional[HierarchyStatusListResponseLatestIngestion] = (
        pydantic.Field(alias="latest_ingestion", default=None)
    )
