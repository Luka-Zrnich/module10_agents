Coach helps customers of the fictional All-Star Sports equipment store check an order's status using an order number.
The order records are a hardcoded Python dictionary, and order-status replies come from keyword rules rather than a live shipping system; other questions go to an Ollama model.
Customers can check one order at a time, and missing or unknown order numbers receive a helpful reply without inventing a status.
Refunds, returns, exchanges, cancellations, and address requests are referred to customer service because a person must verify the order before authorizing changes.
The human handoff is only a referral message in this demo; it does not send a message or open a support ticket.
If this used real customer data, someone guessing an order number could see another customer's order information unless identity checks were added.

The assistant keeps order lookups in code so statuses come from the order book instead of being invented by the model.
Refunds, returns, cancellations, and address changes stay in code because a person must verify and authorize them.
Other questions go to the model with store facts and instructions to admit when it does not know.
Tests use MockModel and SilentModel so they can run with Ollama switched off.

The model answered "What do you sell?" correctly and couldnt answer about free shipping because it doesnt have that information. I kept order look ups in the code so the assistant has something to use instead of making something up.