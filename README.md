Open 311 Simple
==

Introduction
--

This is a draft specification for a simplified Open 311 API. It is very much a
work in progress. Comments, patches and (gentle) cluebats are encouraged.

API
--

The Open 311 Simple API is designed to (3) things:

* allow citizens to discover municipal services for which they can report an
  incident

* report an incident (for a sevice)

* inquire about the status of a reported incident

Additionally, it should be possible for individual users to search for incident
reports. A search my be scoped to an individual user; by geographic location; by
service type or status; and so on.

That's it, really.

As such the API itself is short and simple, by design. General notes and statements of bias are discussed in detail in the [api.md](https://github.com/straup/open311-simple/blob/master/api.md) document. Individual methods and their request/response parameters are covered in the [api-methods.md](https://github.com/straup/open311-simple/blob/master/api.md) document.
