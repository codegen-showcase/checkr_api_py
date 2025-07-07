import pydantic
import typing


class HierarchyCreateResponse(pydantic.BaseModel):
    """
    HierarchyCreateResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    sync_id: typing.Optional[str] = pydantic.Field(alias="sync_id", default=None)
    """
    The `uri_name` of the Account, plus a randomly generated hexadecimal ID, linked with a hyphen.
    """
    time: typing.Optional[str] = pydantic.Field(alias="time", default=None)
    """
    The date and time at which the ingestion job began.
    """
