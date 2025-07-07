import pydantic
import typing


class CandidateStoryRecord(pydantic.BaseModel):
    """
    Simplified representation of linked record.
    If `null`, Candidate Story is considered general information about the Candidate.

    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    case_number: typing.Optional[str] = pydantic.Field(
        alias="case_number", default=None
    )
    """
    Case number, if existing
    """
    charge: typing.Optional[str] = pydantic.Field(alias="charge", default=None)
    """
    Charge description, if existing
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Record ID
    """
    location: typing.Optional[str] = pydantic.Field(alias="location", default=None)
    """
    Location of the Record, can be a State, or a City and a State, if existing
    """
    offense_date: typing.Optional[str] = pydantic.Field(
        alias="offense_date", default=None
    )
    """
    Offense date, if existing
    """
