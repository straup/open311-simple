Open 311 Simple
==

Introduction
--

This is a draft specification for a simplified Open 311 API. It is very much a
work in progress. Comments, patches and (gentle) cluebats are encouraged.

API
--

The Open 311 Simple API is designed to do (3) things:

* allow citizens to discover municipal services for which they can report an
  incident

* report an incident (for a sevice)

* inquire about the status of a reported incident

Additionally, it should be possible for individual users to search for incident
reports. A search my be scoped to an individual user; by geographic location; by
service type or status; and so on.

That's it, really. The API itself is short and simple, by design. One way to think about the API is that it doesn't do anything more than you might already be able to do over the telephone. As such editing incident reports or appending media items (photos, videos, etc.) are out of scope for the time being. There's nothing that would make it very hard to add either but in the interests of making the simplest _common_ platform that all cities can implement with a minimum of fuss they've been left out for the time being.

As of this writing API methods for administrative functions are not included. It's not clear that they should be part of the _core_ Open311 Simple specification. For the sake of discussion a base administrative API should be limited to:

* create and edit service types

* create and edit status types

* update incident reports

* create and edit incident notes

**Detailed notes and statements of bias are discussed in the [api.md](https://github.com/straup/open311-simple/blob/master/api.md) document.**

There is also a [reference implementation](https://github.com/straup/open311-simple-app) built using [Flamework](https://github.com/straup/flamework) (read: PHP and MySQL).
