import pydantic
import typing


class PersonalReferenceVerificationQuestionsItem(pydantic.BaseModel):
    """
    PersonalReferenceVerificationQuestionsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    answer: typing.Optional[str] = pydantic.Field(alias="answer", default=None)
    """
    Answer that Personal Reference gave as a response.
    """
    question: typing.Optional[str] = pydantic.Field(alias="question", default=None)
    """
    A question that was asked to a Personal Reference.
    """
