import pydantic
import typing


class County(pydantic.BaseModel):
    """
    County
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    fips_code: typing.Optional[str] = pydantic.Field(alias="fips_code", default=None)
    """
    The 2+3 digit FIPS code for the county (2-digit state + 3-digit county FIPS code).
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    The county's common name.
    """
