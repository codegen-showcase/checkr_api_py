import pydantic
import typing
import typing_extensions


class CandidatePostalAddress(pydantic.BaseModel):
    """
    CandidatePostalAddress
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    candidate_id: typing.Optional[str] = pydantic.Field(
        alias="candidate_id", default=None
    )
    """
    ID of the resource.
    """
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    """
    City of the Candidate.
    
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Name of the Candidate.
    
    """
    object: typing.Optional[typing_extensions.Literal["candidate_postal_address"]] = (
        pydantic.Field(alias="object", default=None)
    )
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    """
    State of the Candidate.
    
    """
    street: typing.Optional[str] = pydantic.Field(alias="street", default=None)
    """
    Street address of the Candidate.
    
    """
    street2: typing.Optional[str] = pydantic.Field(alias="street2", default=None)
    """
    Additional street address of the Candidate.
    
    """
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    """
    URI of the resource.
    """
    zipcode: typing.Optional[str] = pydantic.Field(alias="zipcode", default=None)
    """
    5-digit zip code of the Candidate.
    
    """
