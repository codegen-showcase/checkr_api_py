import pydantic
import typing
import typing_extensions

from .candidate_story_document import CandidateStoryDocument
from .candidate_story_record import CandidateStoryRecord


class CandidateStory(pydantic.BaseModel):
    """
    CandidateStory
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    content: typing.Optional[str] = pydantic.Field(alias="content", default=None)
    """
    Additional information provided by Candidate.
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the Candidate Story was created.
    """
    documents: typing.Optional[typing.List[CandidateStoryDocument]] = pydantic.Field(
        alias="documents", default=None
    )
    """
    Attached documents provided by Candidate.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    object: typing.Optional[typing_extensions.Literal["candidate_story"]] = (
        pydantic.Field(alias="object", default=None)
    )
    record: typing.Optional[CandidateStoryRecord] = pydantic.Field(
        alias="record", default=None
    )
    """
    Simplified representation of linked record.
    If `null`, Candidate Story is considered general information about the Candidate.
    
    """
    report_id: typing.Optional[str] = pydantic.Field(alias="report_id", default=None)
    """
    ID of the Report to which the Candidate Story is linked.
    """
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    """
    URI of the resource.
    """
