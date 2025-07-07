import pydantic
import typing
import typing_extensions


class Geo(pydantic.BaseModel):
    """
    Geo
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    """
    City for the Geo.
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the Geo was created.
    """
    deleted_at: typing.Optional[str] = pydantic.Field(alias="deleted_at", default=None)
    """
    Time at which the Geo was deleted.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Human-readable name of the Geo.
    """
    object: typing.Optional[typing_extensions.Literal["geo"]] = pydantic.Field(
        alias="object", default=None
    )
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    """
    State for the Geo.
    """
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    """
    URI of the resource.
    """
