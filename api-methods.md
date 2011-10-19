API Methods
==

_This file is auto-generated using the [api-methods.json](https://github.com/straup/open311-simple/blob/master/api-methods.json) specification and the [mk-api-docs](https://github.com/straup/open311-simple/blob/master/bin/mk-api-docs.py) program and compliments the [general API notes](https://github.com/straup/open311-simple/blob/master/api.md)_.

open311.incidents
==

open311.incidents.getInfo
--



**Method**

[GET](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)

**Parameters**

* **incident\_id** - The unique ID of the incident to get information about. - _Required_
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Notes**

* All dates are recorded using the [W3C DateTime format](http://www.w3.org/TR/NOTE-datetime) format.

* All geographic data is returned using the [WGS84](http://spatialreference.org/ref/epsg/4326/) projection.

**Example**

	GET http://example.gov/open311-simple/?method=open311.services.getList

	{
		"total": 3,
		"per_page": 100,
		"page": 1,
		"services": [
			{ "id": 1, "name": "..." },
			{ "id": 2, "name": "..." },
			{ "id": 3, "name": "..." }
		]
	}

open311.incidents.getStatuses
--

Return a list of valid statuses. The types of statuses and their meaning are left to the discretion of individual cities.

**Method**

[GET](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)

**Parameters**

* **page** - The page of results to return. If this argument is omitted, it defaults to 1.
* **per_page** - Number of results to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is left to the discretion of individual cities.
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Example**

	GET http://example.gov/open311-simple/?method=open311.services.getList

	{
		"total": 3,
		"per_page": 100,
		"page": 1,
		"services": [
			{ "id": 1, "name": "..." },
			{ "id": 2, "name": "..." },
			{ "id": 3, "name": "..." }
		]
	}

open311.incidents.report
--

**This method requires authentication**

Report an incident for a given service. Returns a unique ID for the incident that may be used to call the _open311.incidents.status_ API method.

**Method**

[POST](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)

**Parameters**

* **service\_id** - A valid service\_id as defined by the city operating the Open 311 (Simple) API - _Required_
* **latitude** - A valid WGS84 coordinate - _Required_
* **longitude** - A valid WGS84 coordinate - _Required_
* **notes** - A free-form text field in which the user reporting the incident may leave additional notes.
* **photo** - A photograph documenting the reported incident
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Notes**

* All dates should be passed in using the [W3C DateTime format](http://www.w3.org/TR/NOTE-datetime) format.

* All geographic data is expected to be using the [WGS84](http://spatialreference.org/ref/epsg/4326/) projection.

**Example**

	POST http://example.gov/open311-simple/?method=open311.services.getList

	{
		"total": 3,
		"per_page": 100,
		"page": 1,
		"services": [
			{ "id": 1, "name": "..." },
			{ "id": 2, "name": "..." },
			{ "id": 3, "name": "..." }
		]
	}

open311.incidents.search
--

Returns a list of incidents matching a search criteria as defined by the API request.

**Method**

[GET](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)

**Parameters**

* **service\_id** - The unique ID of the service type to search for. Multiple services may be passed in as a comma-separated list.
* **incident\_id** - The unique ID of the incident to search for. Multiple incidents may be passed in as a comma-separated list.
* **status\_id** - The unique ID of a status type to search for. Multiple statuses may be passed in as a comma-separated list.
* **created** - The date or date range (see [api.md](https://github.com/straup/open311-simple/blob/master/api.md) for details) of when an incident was reported.
* **modified** - The date or date range (see [api.md](https://github.com/straup/open311-simple/blob/master/api.md) for details) of when an incident was last modified.
* **where** - A geopgraphic location or extent (see [api.md]((https://github.com/straup/open311-simple/blob/master/api.md) for details) for details) in which to scope the query.
* **page** - The page of results to return. If this argument is omitted, it defaults to 1.
* **per_page** - Number of results to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is left to the discretion of individual cities.
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Notes**

* All dates should be passed to the API (and returned in results) using the [W3C DateTime format](http://www.w3.org/TR/NOTE-datetime).

* All geographic data should be passed to the API using the [WGS84](http://spatialreference.org/ref/epsg/4326/) projection.

* If called with a valid OAuth token and signature then the query will be scoped to the user associated with that token.

* Parameterless searches are not permitted. You must define at least one search criteria.

**Example**

	GET http://example.gov/open311-simple/?method=open311.services.getList

	{
		"total": 3,
		"per_page": 100,
		"page": 1,
		"services": [
			{ "id": 1, "name": "..." },
			{ "id": 2, "name": "..." },
			{ "id": 3, "name": "..." }
		]
	}

open311.services
==

open311.services.getInfo
--

Returns basic information (as included in the _open311.services.getList_ method) as well any additional details that may be relevant to the service.

**Method**

[GET](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)

**Parameters**

* **service\_id** - A valid service\_id to get information about. - _Required_
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Example**

	GET http://example.gov/open311-simple/?method=open311.services.getList

	{
		"total": 3,
		"per_page": 100,
		"page": 1,
		"services": [
			{ "id": 1, "name": "..." },
			{ "id": 2, "name": "..." },
			{ "id": 3, "name": "..." }
		]
	}

open311.services.getList
--

Returns a list of services for which incidents may be reported. The types of services and their meaning are left to the discretion of individual cities.

**Method**

[GET](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)

**Parameters**

* **page** - The page of results to return. If this argument is omitted, it defaults to 1.
* **per_page** - Number of results to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is left to the discretion of individual cities.
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Example**

	GET http://example.gov/open311-simple/?method=open311.services.getList

	{
		"total": 3,
		"per_page": 100,
		"page": 1,
		"services": [
			{ "id": 1, "name": "..." },
			{ "id": 2, "name": "..." },
			{ "id": 3, "name": "..." }
		]
	}

