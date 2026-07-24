# REST vs GraphQL vs gRPC

## REST
REST is the best choice for APIs and public-facing developer platforms.

The tooling ecosystem is unmatched: OpenAPI specs generate documentation, SDKs, and mock servers automatically. Every programming language and HTTP client supports REST natively.

### Simple CRUD Operations
Simple CRUD operations. When your API maps cleanly to create, read, update, and delete operations on well-defined resources, REST’s resource-oriented model is natural and predictable.

### HTTP Caching
REST leverages HTTP caching semantics (ETags, Cache-Control, conditional requests) natively. For read-heavy APIs, this reduces server load and improves response times without application-level caching logic.

### Regulatory and Compliance
REST’s simplicity makes it easier to audit, document, and explain to non-technical stakeholders. OpenAPI specs serve as machine-readable contracts that compliance teams can review.

## GraphQL
TODO

## gRPC
TODO

### Use-cases
- **REST** for public APIs, webhooks and simple services
- **GraphQL** for frontend facing APIs where data flexibility matters
- **gRPC** for high-throughput internal service communication


## References
- https://talkthinkdo.com/guides/api-and-integration/rest-vs-graphql-vs-grpc-choosing-api-style/#:~:text=A%20common%20pattern%20is%20REST,service%20communication%20where%20performance%20matters.