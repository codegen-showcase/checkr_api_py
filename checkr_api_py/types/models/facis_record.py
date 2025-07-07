import pydantic
import typing

from .facis_sanction import FacisSanction


class FacisRecord(pydantic.BaseModel):
    """
    FacisRecord
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    authority: typing.Optional[str] = pydantic.Field(alias="authority", default=None)
    database_registry: typing.Optional[str] = pydantic.Field(
        alias="database_registry", default=None
    )
    dob: typing.Optional[str] = pydantic.Field(alias="dob", default=None)
    full_name: typing.Optional[str] = pydantic.Field(alias="full_name", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    sactions: typing.Optional[typing.List[FacisSanction]] = pydantic.Field(
        alias="sactions", default=None
    )
    """
    Array of FacisSanction objects
    """
