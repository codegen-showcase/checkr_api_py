import pydantic
import typing


class LicenseInfo(pydantic.BaseModel):
    """
    LicenseInfo
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Candidate’s driver license country of issue. **Format:** ISO 3166-2 2 letter alpha2 country code. **Example:** `CA`
    """
    expiration_date: typing.Optional[str] = pydantic.Field(
        alias="expiration_date", default=None
    )
    """
    Candidate’s driver license expiration date. **Date format:** "YYYY-MM-DD”
    """
    is_current: typing.Optional[bool] = pydantic.Field(alias="is_current", default=None)
    """
    Boolean that represents if it is the candidate’s current driver license
    """
    license_class: typing.Optional[str] = pydantic.Field(
        alias="license_class", default=None
    )
    """
    Candidate’s driver license class
    """
    license_number: typing.Optional[str] = pydantic.Field(
        alias="license_number", default=None
    )
    """
    Candidate’s driver license number; Format varies by subdivision (i.e. province)
    """
    subdivision: typing.Optional[str] = pydantic.Field(
        alias="subdivision", default=None
    )
    """
    Candidate's driver license subdivision of issue country. **Format:** ISO 3166-2 subdivision code. **Example:** `CA-AB`
    """
