import pydantic
import typing
import typing_extensions


class CandidatesPostalAddressCreateBody(typing_extensions.TypedDict):
    """
    CandidatesPostalAddressCreateBody
    """

    city: typing_extensions.Required[str]
    """
    City of the Candidate.
    
    """

    name: typing_extensions.Required[str]
    """
    Name of the Candidate.
    
    """

    object: typing_extensions.NotRequired[typing_extensions.Literal["postal_address"]]

    state: typing_extensions.Required[str]
    """
    State of the Candidate.
    
    """

    street: typing_extensions.Required[str]
    """
    Street address of the Candidate.
    
    """

    street2: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Additional street address of the Candidate.
    
    """

    zipcode: typing_extensions.Required[str]
    """
    5-digit zip code of the Candidate.
    
    """


class _SerializerCandidatesPostalAddressCreateBody(pydantic.BaseModel):
    """
    Serializer for CandidatesPostalAddressCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    city: str = pydantic.Field(
        alias="city",
    )
    name: str = pydantic.Field(
        alias="name",
    )
    object: typing.Optional[typing_extensions.Literal["postal_address"]] = (
        pydantic.Field(alias="object", default=None)
    )
    state: str = pydantic.Field(
        alias="state",
    )
    street: str = pydantic.Field(
        alias="street",
    )
    street2: typing.Optional[str] = pydantic.Field(alias="street2", default=None)
    zipcode: str = pydantic.Field(
        alias="zipcode",
    )
