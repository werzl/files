# Multi-tenant Web APIs
A multi-tenant WEB API is one shared by multiple tenants (organisations that have their own groups of users).

Multi-tenancy changes how web APIs are designed because it changes how resources are accessed and discovered across multiple `tenants` within a single API.

- Clearly define how tenants are identified in requests
  - Can be done with subdomains, paths, headers, tokens


## Map Requests to Tenants in a Multi-tenant Solution
Whenever a request arrives into your application, you need to determine the **tenant context** (the tenant making the request).

When you have tenant-specific infrastructure that might be hosted in different geographic regions, you need to match the incoming request to a tenant.

Then, you must forward the request to the physical infrastructure that hosts that tenant's resources.

Approaches to identify tenants:
- **Domain names** - Tenant-specific domains or subdomains can be used to easily map tenants to the correct infrastrcuture.
  - The `Host`, `X-Forwarded-Host` or some other HTTP header that includes the original hostname of each request could be used to identiy a tenant.
  - Need to make sure the user knows which domain name to use
  - May not work with a central entry point / portal login
  - May not play nicely with things like Authorisation tokens - which may need to match the tenant-specific domain name
- **HTTP request properties** 
  - **URL path** (`www.test.com/tenantname/`)
  - **Query string** (`www.test.com?tenant=tenantname`)
  - **Custom HTTP header** (Tenant-Id: tenantname)
- **Token claims** - If using claims-based authentication and authorisation (like OAuth 2.0 or SAML), the authorisation token will include `claims`. Claims can be used to map a user to a tenant - **e.g** a email address which can be used to look up a tenant.
- **API Keys** - You could record the tenant ID for which an API key was generated for, then look up the tenant when the key is used.
- **Client certificates** - `mTLS` is commonly used for service-service comms, and similar to auth tokens - client certificates provide `attributes` which can be used to figure which tenant the cert belongs to.
  - **e.g** - the `subject` of the certificate might contain an email address which can be used to look up a tenant.
  - These are complex to work with, infra is required to manage and issue certificates, also cert rotation would be a problem.
- **Reverse proxies** - These can be used to route HTTP requests. The proxy accepts a request from an ingress, then forward to the correct backend endpoint.
  - Many reverse proxies can use the properties of the request to make a decision about which tenant to route to.
  - They can inspect the destination **domain name**, **URL path**, **query string**, **HTTP headers**, and even **claims** within tokens or parts of the **request body**.
  - `nginx`, `Traefik`, `HAProxy`

### Using subdomain or domain-based isolation (DNS-level tenancy)
This approach uses `tenant-specific domains` to allow tenants to use their own domains.

You can use **Wildcard** (`tenant.microsoft.com`) domains, or **Custom** (`service.tenant.com`) domains, both rely on DNS config including `A` and `CNAME` records to direct traffic to the correct infrastructure.

[Host name preservation](https://learn.microsoft.com/en-us/azure/architecture/best-practices/host-name-preservation) is recommended to ensure auth, session state, cookies and redirect URLs work properly. 

### Request Validation
It is important that your application validates that any requests that it receives are authorized for the tenant.

For example, if your application uses a custom domain name to map requests to the tenant, then you must still check that each request is authorized for that tenant.

When you use `OAuth 2.0`, you perform the validation by inspecting the audience and scope claims.

### Performance
Consider scalability, checking the DB for the tenant lookup, or decrypting a token can be expensive at massive scale.

- Use `Session cookies` to reduce the performance overhead, perform the tenant mapping at the start of the session and then provide a session cookie to the client. The cookie is then sent back by the client on the next request

### Tenant Migration
Tenants often need to be moved to new infrastructure as part of the `tenant lifecycle`.

When a tenant is moved to a new deployment, the HTTP endpoints they access might change. 



## Enable Distributed Tracing and Trace Context
Use headers such as `Correlation-ID`, `X-Request-ID` and `X-Trace-ID`.

These can be used to propagate trace context in API requests. It's a best practice for eng-to-end visibility.

Observability improvements like this make it easier to track requests and debug issues.


## References
- https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#multitenant-web-apis
- https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/map-requests
- https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenant-life-cycle
- https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/domain-names
