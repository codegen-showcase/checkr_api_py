import pydantic
import typing


class FacisSanction(pydantic.BaseModel):
    """
    FacisSanction
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    acquisition_date: typing.Optional[str] = pydantic.Field(
        alias="acquisition_date", default=None
    )
    case_number: typing.Optional[str] = pydantic.Field(
        alias="case_number", default=None
    )
    entry_date: typing.Optional[str] = pydantic.Field(alias="entry_date", default=None)
    publication_date: typing.Optional[str] = pydantic.Field(
        alias="publication_date", default=None
    )
    saction: typing.Optional[str] = pydantic.Field(alias="saction", default=None)
    """
    Text describing sanction
    """
