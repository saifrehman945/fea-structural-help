# apex.license

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.license.CheckoutStatus`: `NOT_LICENSED`, `AVAILABLE`, `CHECKED_OUT`, `FAILED_CHECKOUT`
  - Possible License Feature Checkout states

## Module functions

### `apex.license.checkinFeature(lpid: int) -> apex.license.CheckoutStatus`
Checkin a Custom License Feature.

- `lpid` — The license PID of the License Feature to checkin

Returns: CheckoutStatus of the License Feature after the checkin attempt

### `apex.license.checkoutFeature(lpid: int) -> apex.license.CheckoutStatus`
Checkout a Custom License Feature.

- `lpid` — The license PID of the License Feature to checkout

Returns: CheckoutStatus of the License Feature after the checkout attempt

### `apex.license.getCheckoutStatus(lpid: int) -> apex.license.CheckoutStatus`
Retrieves the current CheckoutStatus of a Custom License Feature.

- `lpid` — The license PID of the License Feature to query

Returns: CheckoutStatus of the License Feature

