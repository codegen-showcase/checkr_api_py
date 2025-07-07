import pydantic
import typing
import typing_extensions


class Program(pydantic.BaseModel):
    """
    Program
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the resource was created.
    """
    deleted_at: typing.Optional[str] = pydantic.Field(alias="deleted_at", default=None)
    """
    Time at which the resource was deleted.
    """
    geo_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="geo_ids", default=None
    )
    """
    Array of associated Geo IDs.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Human-readable name of the Program.
    """
    object: typing.Optional[typing_extensions.Literal["program"]] = pydantic.Field(
        alias="object", default=None
    )
    package_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="package_ids", default=None
    )
    """
    Array of associated Package IDs.
    """
