# HATEOAS (Hypertext As The Engine Of Application State)
HATEOAS is a constraint of REST API architectural design.

The point of hypermedia controls is that they tell us what we can do next, and the URI of the resource we need to manipulate to do it.


## Why Is this Not the Standard?
No one actually consumes REST APIs in a HATEOAS manner, even if you do add support it from the server side.


## Hypermedia links
The example below contains links to get or update the customer that's associated with the order.

```json
{
  "orderID":3,
  "productID":2,
  "quantity":4,
  "orderValue":16.60,
  "links": [
    {"rel":"product","href":"https://api.contoso.com/customers/3", "action":"GET" },
    {"rel":"product","href":"https://api.contoso.com/customers/3", "action":"PUT" }
  ]
}
```


## References
- See level 3 in the Richardson Maturity Model.
  - https://martinfowler.com/articles/richardsonMaturityModel.html
- https://en.wikipedia.org/wiki/HATEOAS
- https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#web-api-maturity-model