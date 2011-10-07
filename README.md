Open 311 Simple
--

This is a draft specification for a simplified Open 311 API. It is very much a
work in progress. Comments, patches and (gentle) cluebats are encouraged.

The Open 311 Simple API is designed to (3) things:

* allow citizens to discover municipal services for which they can report an
  incident

* report an incident (for a sevice)

* inquire about the status of a reported incident

Additionally, it should be possible for individual users to search for incident
reports. A search my be scoped to an individual user; by geographic location; by
service type or status; and so on.

As such the API itself is short and simple, by design. Individual methods and
their request/response parameters are [discussed in detail elsewhere](https://github.com/straup/open311-simple/blob/master/api-methods.md) but the
short version might look like this:

* open311.services.getList

* open311.services.getInfo

* open311.incidents.report

* open311.incidents.getInfo

* open311.incidents.search
