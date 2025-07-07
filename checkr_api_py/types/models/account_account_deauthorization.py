import pydantic
import typing


class AccountAccountDeauthorization(pydantic.BaseModel):
    """
    Account deauthorization details if account has been deauthorized.

    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reason: typing.Optional[str] = pydantic.Field(alias="reason", default=None)
    """
    Reason for account deauthorization.
    """
