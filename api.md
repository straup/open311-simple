The Open 311 Simple API
==

There are two basic classes of API methods: _list_ methods and _info_
methods. The former are meant return the minimum amount of data around a service
or incident to allow a user to perform a discrete action; the latter return all
the information available for a service or incident.

Specification
==

The API method specification is defined as a JSON data structure containing basic metadata about each individual method such that it can be used by actual running code to delegate API requests and generate documentation.

Developers are still required to implement their own dispatching system in order to serve and process those API methods. The modeling of the API specification in JSON is simply meant as a language-agnostic configuration file that can be easily shared across programming languages (since they basically all have JSON decoders to translate the data in to native data structures).

API methods are defined in [api-methods.json](https://github.com/straup/open311-simple/blob/master/api-methods.json) document. The [api-methods.md](https://github.com/straup/open311-simple/blob/master/api-methods.md) document contains human-friendly documentation for the API.

Transport
==

All API requests and responses are delivered using [HTTP](http://www.w3.org/Protocols/). Wherever possible API requests are performed using the HTTP _GET_ method. In some cases where security considerations demand it (for example, reporting an incident) API requests are performed using the HTTP _POST_ method.

Successful API methods are returned using HTTP responses in the 200 range. All others are expected to return responses in the 400-500 range although this is left to the discretion of individual cities.

_The emphasis here is that, as much as possible, the API may be explored and tested by as many people as possible using nothing more complicated that a web browser._

Authentication
==

All API authentication will be performed using [OAuth2](http://oauth.net/2/).

Response formats
==

The default API response format is [JSON](http://www.json.org/).

Additional responses are left to the discretion of individual cities and are identified in API requested with the
_format_ parameter.

Pagination
==

If an API method is a _list_-style method (described above) then it will always paginate its responses. Pagination is simply a way to limit the number of responses returned for a single method call, as defined by a _per_page_ parameter (as in the number of results to return). Offsets are calculated by multiplying the _page_ and _per_page_ parameters (or attributes in the case of API responses).

Requests to paginated methods may pass the following parameters:

* **page** – the current offset (calculated by multiplying _page_ by _per_page_) to start fetching results from.

* **per_page** – the number of results to return for a given API request.

Default values are left to the discretion of individual cities.

Paginated responses will always return the following attributes:

* **total** – The total number of results for the query issued by the API method, regardless of pagination.

* **pages** – The total number of paginated results (or "pages") that will be returned by the API method. This number is calculated by dividing _total_ by the _per_page_ parameter (or default value, defined above).

* **page** – The current offset "page" for the total result set.

For example:

	GET example.com/api?method=open311.services.getList?page=2&per_page=2

	{
		"total": 5,
		"pages": 3,
		"page": 2,
		"services": [
			{ "id": 1, "name": "...", "type": "..." },
			{ "id": 2, "name": "...", "type": "..." },
		]
	}

Incidents
==

TBW.

	{
		"id": 999,
		"service_id": 2,
		"status_id": 1,
		"created": "2011-03-15T23:22:45Z",
		"modified": "2011-03-16T10:17:33Z",
		"latitude": 37.23,
		"longitude": -122.45,
		"description": "..."
	}

Tags
==

Tagging will follow the [OpenStreetMap (OSM) standard for tagging](https://wiki.openstreetmap.org/wiki/Any_tags_you_like) and encourage users, where
applicable, to follow [the guidelines and naming conventions that the OSM
community has developed](https://wiki.openstreetmap.org/wiki/Map_Features) and refined over time.

It has been proven to be both robust enough to be used to power the OSM map
renderer and flexible enough to meet the needs of tinkerers and playful enough
to encourage innovations no one even considered at the outset.

_TBD: Whether or not the “k=” and “v=” is used preserve the separation of subject and
value in two separate fields that can be indexed and searched independently._

Dates
==

All dates are recorded using the [W3C DateTime format](http://www.w3.org/TR/NOTE-datetime). 

All dates are passed a single-value reference to a date or date range, replacing
convential "start" and "stop" prefixes for the various date arguments.

Because the "-" and ":" characters are used by the W3C DateTime format date
ranges are separated using a semicolon (;) character.

Example values:

* A single, full day: 2010-05-26.

* A full week: 2010-05-23;2010-05-29.

* A single hour: 2010-05-26T21:00:00Z;2010-05-26T22:00:00Z.

Geo
==

All geographic data should be passed to (and returned from) the API using the
unprojected [WGS84](http://spatialreference.org/ref/epsg/4326/) datum. The phrase "unprojected WGS84 data" can be roughly translated as: _Plain-old latitude and longitude, the way those of us who don't study GIS think about things._

Geographic coordinates are expressed as latitude followed by longitude. Bounding boxes are expressed as a set of coordinates representing the South-West and North-East edges of the container.

The "where" argument
--

The "where" argument (used by the _open311.incidents.search_ method) wraps all geographic queries in a single
interface. Argument values are prefixed with a human-readable string followed by
a colon (":") followed a string representing a geographic location.

The prefix is used by parsers to determine how the rest of a "where" string
should be interpreted. For example:

* Bounding box: ?where=bbox:37.788,-122.344,37.857,-122.256

* Around a point: ?where=near:37.804376,-122.271180

* In a geohash: ?where=geohash:9q9p1dhf7

* In a zip code: ?where=zip:94612

The single parameter removes possible conflicts or overlaps between other
parameters, and introduces an extensible way to namespace "known" areas like zip
codes, countries and allow individual cities to introduce place types specific
to their jurisdiction (for example: housing lots or building identifiers).

**All Open311 Simple providers MUST implement the "bbox:" prefix to allow for geographic queries within a bounding box.** All other prefixes are left to the discretion (and technical infrastructure) of individual cities. API clients may request a list of supported prefixed using the _open311.where.getList_ API method.

To Do
==

* Finish documenting all API parameters

* Finish documenting OAuth stuff.

Questions:
==

* Privacy concerns related to returning information about the user who reported
  an incident; should that information be returned at all?

* Should there be a separate 'getIncidents' API method to return individual
  reports for a user (as identified by an OAuth token) or should the definition
  for the _search_ API method include to search for reports by user ID (see
  above) ?
