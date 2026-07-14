# REST API Design Best Practices

- Use JSON for Request/Response Bodies
- Use nouns instead of verbs in endpoint paths
- Nesting resources for hierarchical objects
- Hypermedia links
- Handle errors gracefully and return standard error codes
- Allow filtering, sorting, and pagination
- Maintain Good Security Practices
- Cache data to improve performance
- Versioning our APIs


## Use JSON for Request/Response Bodies
Where possible, REST APIs should accept JSON in the request payload and also respond with JSON.

JSON is the standard for transferring data, almost every networked technology can use it.

There are other options, like XML, and form-data. These are rarely more usable than JSON however.

To make sure that when our REST API app responds with JSON that clients interpret it as such, we should set `Content-Type` in the response header to `application/json`.

The only exception is if we’re trying to **send and receive files** between client and server. Then we need to handle file responses and send form data from client to server.


## Use nouns instead of verbs in endpoint paths
The verbs map to CRUD operations.

We should create routes like `GET /articles/` for getting news articles. Likewise, `POST /articles/` is for adding a new article , `PUT /articles/:id` is for updating the article with the given id. `DELETE /articles/:id` is for deleting an existing article with the given ID.


## Nesting resources for hierarchical objects
When designing endpoints, it makes sense to group data when one object can contain another object.

This is good practice even if the data isn't structured like this in the database, 

For example, if we want an endpoint to get the comments for a news article, we should append the `/comments` path to the end of the `/articles` path.
```
GET /articles/:id/comments
```

### When Nesting Goes too Far
Nesting can get overwhelming, after about the second or third level.

Consider using **hypermedia links instead**.


## Hypermedia links
REST APIs can be driven by hypermedia links that are contained in each resource representation. The example below contains links to get or update the customer that's associated with the order.

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


## Handle errors gracefully and return standard error codes
Handle errors gracefully and return HTTP response codes that indicate what kind of error occurred.

For example, return a 400 response status when we want to reject based on the request, and an error message that indicates this - `"User already exists"`


## Allow filtering, sorting, and pagination
The databases behind a REST API can get very large. Sometimes, there's so much data that it shouldn’t be returned all at once because it’s way too slow or will bring down our systems. Therefore, we need ways to filter items.


## Maintain good security practices
Most communication between client and server should be private since we often send and receive private information. Therefore, using SSL/TLS for security is a must.

A SSL certificate isn't too difficult to load onto a server and the cost is free or very low. There's no reason not to make our REST APIs communicate over secure channels instead of in the open.

**Principle of least privilege** - People shouldn't be able to access more information that they requested. For example, a normal user shouldn't be able to access information of another user. They also shouldn't be able to access data of admins.


## Cache data to improve performance
There are many kinds of caching solutions like Redis, in-memory caching, and more. We can change the way data is cached as our needs change.

If you are using caching, you should also include [Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) information in your headers. This will help users effectively use your caching system.


## Versioning our APIs
We should have different versions of API if we're making any changes to them that may break clients.

The v1 endpoint can stay active for people who don’t want to change, while the v2, with its shiny new features, can serve those who are ready to upgrade. This is especially important if our API is public. We should version them so that we won't break third party apps that use our APIs.

Versioning is usually done with `/v1/`, `/v2` added at the start of the API path.


## References
- https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/
