import pydantic
import typing


class Ssn(pydantic.BaseModel):
    """
    Ssn
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    encrypted_ssn: typing.Optional[str] = pydantic.Field(
        alias="encrypted_ssn", default=None
    )
    """
    The candidate's SSN: encrypted, then encoded using Base64. `Null` if no SSN exists for the candidate.
    """
