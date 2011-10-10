The Open 311 Simple API
==

There are two basic classes of API methods: _list_ methods and _info_
methods. The former are meant return the minimum amount of data around a service
or incident to allow a user to perform a discrete action; the latter return all
the information available for a service or incident.

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

TBW

Dates
==

All dates are recorded using the [W3C DateTime format](http://www.w3.org/TR/NOTE-datetime).

Date Ranges
==

TBW.

Methods
==

[API methods are defined in a separate document.](https://github.com/straup/open311-simple/blob/master/api-methods.json)

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
