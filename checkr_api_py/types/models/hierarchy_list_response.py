import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .hierarchy_tree import HierarchyTree


class HierarchyListResponse(pydantic.BaseModel):
    """
    HierarchyListResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    nodes: typing.Optional[typing.List["HierarchyTree"]] = pydantic.Field(
        alias="nodes", default=None
    )
    sync_id: typing.Optional[str] = pydantic.Field(alias="sync_id", default=None)
    """
    The `uri_name` of the Account, plus a randomly generated hexadecimal ID, linked with a hyphen.
    """
    time: typing.Optional[str] = pydantic.Field(alias="time", default=None)
    """
    The date and time at which the ingestion job began.
    """
