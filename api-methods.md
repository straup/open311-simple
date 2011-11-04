API Methods
==

_This file is auto-generated using the [api-methods.json](https://github.com/straup/open311-simple/blob/master/api-methods.json) specification and the [mk-api-docs](https://github.com/straup/open311-simple/blob/master/bin/mk-api-docs.py) program and compliments the [general API notes](https://github.com/straup/open311-simple/blob/master/api.md)_.

open311.incidents
==

open311.incidents.addNote
--

Add an additional note to an incident report.

**Method**

[POST](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)

**Parameters**

* **incident\_id** - The unique ID of the incident to add a note for. - _Required_
* **note** - The body of the note to add to the incident report. - _Required_
* **public** - Whether or not the note is publicly viewable. Default is false..
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Example**

	POST http://example.gov/open311-simple/?method=open311.incidents.addNote

open311.incidents.getInfo
--

Get the detailed information for an incident report.

**Method**

[GET](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)

**Parameters**

* **incident\_id** - The unique ID of the incident to get information about. - _Required_
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Notes**

* All dates are recorded using the [W3C DateTime format](http://www.w3.org/TR/NOTE-datetime) format.

* All geographic data is returned using the unprojected [WGS84](http://spatialreference.org/ref/epsg/4326/) datum (read: plain old latitudes and longitudes).

**Example**

	GET http://example.gov/open311-simple/?method=open311.incidents.getInfo

	{
		"incident": {
			"id": 999,
			"service_id": 2,
			"status_id": 1,
			"reported": "..."
		}
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
* **description** - A free-form text field in which the user reporting the incident may leave additional notes.
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Notes**

* All dates should be passed in using the [W3C DateTime format](http://www.w3.org/TR/NOTE-datetime) format.

* All geographic data is expected to be using the unprojected [WGS84](http://spatialreference.org/ref/epsg/4326/) datum (read: plain old latitudes and longitudes).

**Example**

	POST http://example.gov/open311-simple/?method=open311.incidents.report

	{
		"incident": {
			"id": 999,
			"service_id": 2,
			"status_id": 1,
			"reported": "..."
		}
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

* All geographic data should be passed to the API using the unprojected [WGS84](http://spatialreference.org/ref/epsg/4326/) datum (read: plain old latitudes and longitudes).

* If called with a valid OAuth token and signature then the query will be scoped to the user associated with that token.

* Parameterless searches are not permitted. You must define at least one search criteria.

**Example**

	GET http://example.gov/open311-simple/?method=open311.incidents.search

	{
		"total": 2,
		"per_page": 100,
		"page": 1,
		"incidents": [
			{ "id": 999, "service_id": 2, "status_id": 1, "reported": "..." },
			{ "id": 23, "service_id": 3, "status_id": 1, "reported": "..." },
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

	GET http://example.gov/open311-simple/?method=open311.services.getInfo

	{
		"service": {
			"id": 1,
			"name": "...",
			"description": "..."
		}
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

open311.statuses
==

open311.statuses.getList
--

Return a list of valid statuses for incidents. The types of statuses and their meaning are left to the discretion of individual cities.

**Method**

[GET](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)

**Parameters**

* **page** - The page of results to return. If this argument is omitted, it defaults to 1.
* **per_page** - Number of results to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is left to the discretion of individual cities.
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Example**

	GET http://example.gov/open311-simple/?method=open311.statuses.getList

open311.where
==

open311.where.getList
--

Returns a list of geographic prefixes that may be used to query for incident reports using the 'open311.incidents.search' API method.

**Method**

[GET](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)

**Parameters**

* **page** - The page of results to return. If this argument is omitted, it defaults to 1.
* **per_page** - Number of results to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is left to the discretion of individual cities.
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Example**

	GET http://example.gov/open311-simple/?method=open311.where.getList

	{
		"total": 3,
		"per_page": 100,
		"page": 1,
		"terms": [
			{ "prefix": "bbox", "description": "...", "example": "bbox:37.788,-122.344,37.857,-122.256" },
			{ "prefix": "near", "description": "...", "example": "near:37.804376,-122.271180" },
			{ "prefix": "zip", "description": "...", "example": "zip:94110" }
		]
	}

