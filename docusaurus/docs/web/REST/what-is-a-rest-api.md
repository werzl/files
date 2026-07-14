# What is a REST API?

## What is an API?
An application programming interface (API) defines the rules that you must follow to communicate with other software systems. Developers expose or create APIs so that other applications can communicate with their applications programmatically.

It's a set of protocols and definitions for integrating application software.

Or a contract between a data "consumer" (client) and a data "provider" (server).


## REST
REST (Representational State Transfer) is a set of architectural principles and guidelines for how to build a Web API. REST was initially created as a guideline to manage comms on complex networks like the internet. 

APIs that follow the REST architectural style are called **REST APIs**. Web services that implement REST architecture are called **RESTful web services**.

When a client request is made via a RESTful API, it transfers a representation of the state of the resource to the requester or endpoint.   
This information, or representation, is delivered in one of several formats via HTTP: JSON, HTML, XLT, Python, PHP, or plain text.   
JSON is the most generally popular file format to use because, despite its name, it’s language-agnostic, as well as readable by both humans and machines. 

Something else to keep in mind: **Headers** and **parameters** are also important in the HTTP methods of a RESTful API HTTP request.


## Uniform Interface
Indicates that the server transfers information in a standard format.

The formatted resource is called a representation in REST.

This format can be different from the internal representation of the resource on the server application.

### Uniform Interface Constraints:
- Requests should identify resources, using a URI (uniform resource identifier)
- Clients have enough info in the resource representation to modify or delete the resource if they want to
  - The server meets this condition by sending metadata that describes the resource
- Clients receive info about how to process the representation further
  - The server achieves this by sending self-descriptive messages that contain metadata about how the client can best use them
- Clients receive info about all other related resources they need to complete a task
  - The server achieves this by sending hyperlinks in the representation so taht clients can dynamically discover more resources


## Statelessness
In REST architecture, statelessness refers to the comms in which the server completes every request independently of all previous requests.

Clients can request resources in any order, and every request is stateless or isolated from other requests.


## Layered System
In a layered system architecture, the client can connect to other authorised intermediaries between the client and server, and still receive responses from the server.

Servers can also pass on requests to other servers.

You can design a RESTful web service to run on several servers with multiple layers (like security, application, business logic) which all work together to serve client requests.

These layers remain invisible to the client.


## Cache-ability
RESTful web services support caching to improve server response time.


## Code on demand (Optional)
In REST architectural style, servers can temporarily extend or customize client functionality by transferring software programming code to the client. For example, when you fill a registration form on any website, your browser immediately highlights any mistakes you make, such as incorrect phone numbers. It can do this because of the code sent by the server.


## Benefits of RESTful APIs
- Scalability
  - Server can scale efficiently because of REST optimisations.
  - Statelessness removes server load because it doesnt have to store information about requests.
  - Caching improves performance
- Maintainability
  - Client-Server separation
  - Simplified and decoupled components
  - Layered application functions allow for flexibility - e.g. developers can work on the database layer without rewriting business logic.
- Independence
  - REST APIs are independent of the tech used, you can write both client and server in different languages without affecting API design.

## References
- https://www.redhat.com/en/topics/api/what-is-a-rest-api
- https://aws.amazon.com/what-is/restful-api/