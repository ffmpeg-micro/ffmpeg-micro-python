# TranscodeStatus

Job lifecycle: `pending` (created, awaiting pickup) → `processing` → `completed` | `failed`; a user cancellation sets `canceled` (US spelling). Note there is no `queued` status — new jobs start as `pending`. 

## Enum

* `PENDING` (value: `'pending'`)

* `PROCESSING` (value: `'processing'`)

* `COMPLETED` (value: `'completed'`)

* `FAILED` (value: `'failed'`)

* `CANCELED` (value: `'canceled'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


