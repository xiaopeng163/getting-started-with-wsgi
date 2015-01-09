# Middleware

Middleware use to filter `Request` and `Response`.

Component that acts like an application from the server's point of view:

    – It is a callable that accepts environ and start_response;
    – Calls start_repsonse once with status and headers, etc.
    – Returns an iterable
    
Looks like a server to another piece of middleware or an application

    – Provides start_response and environ dictionaries
    – Expects a response
