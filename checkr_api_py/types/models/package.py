import pydantic
import typing
import typing_extensions

from .package_screenings_item import PackageScreeningsItem


class Package(pydantic.BaseModel):
    """
    Package
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    apply_url: typing.Optional[str] = pydantic.Field(alias="apply_url", default=None)
    """
    URL at which candidates may apply for a background check with this Package.
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the Package was created.
    """
    deleted_at: typing.Optional[str] = pydantic.Field(alias="deleted_at", default=None)
    """
    Time at which the Package was deleted.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Human-readable name of the Package.
    """
    object: typing.Optional[typing_extensions.Literal["package"]] = pydantic.Field(
        alias="object", default=None
    )
    price: typing.Optional[int] = pydantic.Field(alias="price", default=None)
    """
    Package price in USD cents.
    """
    screenings: typing.Optional[typing.List[PackageScreeningsItem]] = pydantic.Field(
        alias="screenings", default=None
    )
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)
    """
    Unique key identifier of the Package.
    """
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    """
    URI of the resource.
    """
