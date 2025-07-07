import pydantic
import typing
import typing_extensions

from .account_account_deauthorization import AccountAccountDeauthorization
from .account_company import AccountCompany


class Account(pydantic.BaseModel):
    """
    Account
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_deauthorization: typing.Optional[AccountAccountDeauthorization] = (
        pydantic.Field(alias="account_deauthorization", default=None)
    )
    """
    Account deauthorization details if account has been deauthorized.
    
    """
    adverse_action_email: typing.Optional[str] = pydantic.Field(
        alias="adverse_action_email", default=None
    )
    """
    Email used to send pre- and post- Adverse Action notices on behalf of the Account to candidates.
    This address will also receive undeliverable notices if an Adverse Action notice isn't deliverable to a candidate.
    
    """
    api_authorized: typing.Optional[bool] = pydantic.Field(
        alias="api_authorized", default=None
    )
    """
    Determines whether Account is authorized to use the API to order background checks.
    
    """
    authorized: typing.Optional[bool] = pydantic.Field(alias="authorized", default=None)
    """
    Determines whether Account is credentialed to order background checks.
    
    """
    available_screenings: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="available_screenings", default=None
    )
    """
    List of screening types available for the Account.
    
    """
    billing_email: typing.Optional[str] = pydantic.Field(
        alias="billing_email", default=None
    )
    """
    Email that is used for Checkr to contact you about invoices and other billing communication.
    
    """
    company: typing.Optional[AccountCompany] = pydantic.Field(
        alias="company", default=None
    )
    """
    Company details
    """
    compliance_contact_email: typing.Optional[str] = pydantic.Field(
        alias="compliance_contact_email", default=None
    )
    """
    Email for the main point of contact on your side to communicate with Checkr about
    compliance issues or updates. This is also where we'll send you the results of candidate
    disputes (for example, if we changed the information on a report).
    
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the Account was created.
    """
    default_compliance_city: typing.Optional[str] = pydantic.Field(
        alias="default_compliance_city", default=None
    )
    """
    Fallback compliance city if candidate location is not provided.
    
    """
    default_compliance_state: typing.Optional[str] = pydantic.Field(
        alias="default_compliance_state", default=None
    )
    """
    Fallback compliance state if candidate location is not provided. Format: `ISO 3166-2:US`.
    
    """
    geos_required: typing.Optional[bool] = pydantic.Field(
        alias="geos_required", default=None
    )
    """
    Determines whether a Geo must be provided to order a Report.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    The ID of the Account.
    
    <b>Note: </b>The returned Account ID is dependent on the API token used to make the call.
      * If an account-level API token is used, the ID of the account associated with the Live API Token will be returned.
      * If a partner OAuth token is used, the ID of the account (or customer's account) connected to the OAuth application will be returned.
    
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Name of Account displayed in the Dashboard.
    """
    object: typing.Optional[typing_extensions.Literal["account"]] = pydantic.Field(
        alias="object", default=None
    )
    purpose: typing.Optional[
        typing_extensions.Literal["business", "employment", "insurance", "tenant"]
    ] = pydantic.Field(alias="purpose", default=None)
    """
    Permissible purpose to run background checks.
    Determines which background checks the Account is credentialed for.
    
    """
    segmentation_enabled: typing.Optional[bool] = pydantic.Field(
        alias="segmentation_enabled", default=None
    )
    """
    Determines whether Hierarchy/Nodes is enabled on the Account.
    """
    support_email: typing.Optional[str] = pydantic.Field(
        alias="support_email", default=None
    )
    """
    Email address used for candidates to contact you if they need to supply evidence
    of rehabilitation or other context during the Adverse Action process.
    
    """
    support_phone: typing.Optional[str] = pydantic.Field(
        alias="support_phone", default=None
    )
    """
    Phone number used for candidates to contact you if they need to supply evidence of
    rehabilitation or other context during the Adverse Action process.
    
    """
    technical_contact_email: typing.Optional[str] = pydantic.Field(
        alias="technical_contact_email", default=None
    )
    """
    The main point of contact on your side to communicate with Checkr about technical issues or
    updates.
    
    """
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    """
    URI of the resource.
    """
    uri_name: typing.Optional[str] = pydantic.Field(alias="uri_name", default=None)
    """
    Unique slug referencing the Account. This appears in some Account-specific URL paths.
    
    """
