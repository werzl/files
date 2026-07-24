# How do RESTful APIs Work?
The client contacts the server by using the API when it requires a resource. API developers explain how the client should use the REST API in the server application API documentation.

1. The client sends a request to the server, following the API documentation to format the request in a way the server will understand
2. The server authenticates the client and confirms that the client has the right to make the request
3. The server receives the request and processes it internally
4. The server returns a response to the client.  
  4.a. The response contains information that tells the client whether the request was successful, and the information that the client requested.


## REQUEST
- **Unique Resource Identifier** - Server identifies each resource with a unique identifier. Typically a URL. The URL specifies the path to the resource.
- **Method** - HTTP methods tells the server what it needs to do to the resrouce.
  - **GET** - Access resources
  - **POST** - Send data to the server
  - **PUT** - Update existing resources
  - **DELETE** - Remove resources
- **HTTP Headers** - Metadata exchanged between the client and server.
- **Data** - Requests may include data for the POST, PUT and other HTTP methods
- **Parameters** - Requests can include parameters that give the server more details about what needs to be done.
  - **Path** - Path to a resource IN the URL
  - **Query** - Requests more information about a resource
  - **Cookie** - Authenticate clients quickly


## RESTful API Authentication Methods
### HTTP Authentication
- Basic
- Bearer

### API Keys
API keys are another option for REST API authentication. In this approach, the server assigns a unique generated value to a first-time client. Whenever the client tries to access resources, it uses the unique API key to verify itself. API keys are less secure because the client has to transmit the key, which makes it vulnerable to network theft.


### OAuth
Combines passwords and tokens for highly secure login. The server first requests a password and then asks for an additional token o complete the authorisation process.

It can check the token at any time and also over time with a specific scope and lifetime.


## RESPONSE
### Status
3 digit code that indicates success or failure.
- **2xx** - Success
- **4xx**, **5xx** - Error
- **3xx** - URL redirection

### Response Body
The response body contains the resource representation.

The server selects an appropriate representation format based on what the request headers contain.

### Response Headers
The response also contains headers or metadata about the response. They give more context about the response and include information such as the server, encoding, date, and content type.


## References
- https://aws.amazon.com/what-is/restful-api/