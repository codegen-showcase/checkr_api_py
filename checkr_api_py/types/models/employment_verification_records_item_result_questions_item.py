import pydantic
import typing


class EmploymentVerificationRecordsItemResultQuestionsItem(pydantic.BaseModel):
    """
    EmploymentVerificationRecordsItemResultQuestionsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    response: typing.Optional[str] = pydantic.Field(alias="response", default=None)
    """
    The answer received in response to the question.
    """
    sort_number: typing.Optional[int] = pydantic.Field(
        alias="sort_number", default=None
    )
    """
    The position of the question within the list.
    """
    text: typing.Optional[str] = pydantic.Field(alias="text", default=None)
    """
    The question that was asked.
    """
