import pydantic
import typing
import typing_extensions


class I9WorksitesUpdateResponse(pydantic.BaseModel):
    """
    I9WorksitesUpdateResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Worksite Id.
    """
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    """
    City of Worksite.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Worksite name.
    """
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    """
    State of Worksite.
    """
    street_line1: typing.Optional[str] = pydantic.Field(
        alias="street_line1", default=None
    )
    """
    Line one of Worksite address.
    """
    street_line2: typing.Optional[str] = pydantic.Field(
        alias="street_line2", default=None
    )
    """
    Line two of Worksite address.
    """
    zip_code: typing.Optional[str] = pydantic.Field(alias="zip_code", default=None)
    """
    ZIP Code of Worksite.
    """
    everify_status: typing.Optional[typing_extensions.Literal["active", "inactive"]] = (
        pydantic.Field(alias="everify_status", default=None)
    )
    """
    Worksite E-Verify Status.
    """
