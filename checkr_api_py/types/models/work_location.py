import pydantic
import typing


class WorkLocation(pydantic.BaseModel):
    """
    WorkLocation
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    """
    Name of the city
    """
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    The country in ISO-3166 alpha-2 format.
    """
    state: str = pydantic.Field(
        alias="state",
    )
    """
    The two letter state code.
    """
