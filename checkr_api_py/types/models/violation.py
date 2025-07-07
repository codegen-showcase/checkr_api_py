import pydantic
import typing


class Violation(pydantic.BaseModel):
    """
    Violation
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    Description of the violation
    """
    issued_date: typing.Optional[str] = pydantic.Field(
        alias="issued_date", default=None
    )
    """
    Violation issuance date. <b>Date format:</b> "YYYY-MM-DD”
    """
