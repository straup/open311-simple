API methods
==

_[This document compliments the general "API"
documentation.](https://github.com/straup/open311-simple/blob/master/api.md)_

There are two basic classes of API methods: _list_ methods and _info_
methods. The former are meant return the minimum amount of data around a service
or incident to allow a user to perform a discrete action; the latter return all
the information available for a service or incident.

Questions:

* privacy concerns related to returning information about the user who reported
  an incident; should that information be returned at all?

* should there be a separate 'getIncidents' API method to return individual
  reports for a user (as identified by an OAuth token) or should the definition
  for the _search_ API method include to search for reports by user ID (see
  above) ?

open311.searvices.getList
--

Returns a list of services for which incidents may be reported. The types of
services and their meaning are left to the discretion of individual cities.

Parameters:

* **format** (optional)

Example:

	GET example.com/api?method=open311.services.getList

	{
	"services": [
		{ "id": 1, "name": "...", "type": "..." },
		{ "id": 2, "name": "...", "type": "..." },
		{ "id": 3, "name": "...", "type": "..." }
	]
	}

open311.services.getInfo
--

Returns basic information (as included in the _open311.services.getList_ method)
as well any additional details that may be relevant to the service.

Parameters:

* **id** (required)

* **format** (optional)

Example:

	GET example.com/api?method=open311.services.getInfo&id=1

	{
		"id": 1,
		"name": "...",
		"type": "...",
		"description": "..."
	}

open311.incidents.getStatuses
--

Return a list of valid statuses. The types of statuses and their meaning are
left to the discretion of individual cities.

Parameters:

* **format** (optional)

Example:

	GET example.com/api?method=open311.incidents.getStatuses

	{
	"statuses": [
		{ "id": 1, "label": "open", "description": "..." },
		{ "id": 2, "label": "pending", "description": "..." }
	]
	}

open311.incidents.report
--

TBW.

Returns a unique ID for the incident that may be used to call the
_open311.incidents.status_ API method.

Parameters:

* **service_id** (required)

* **format** (optional)

Photos (and other media enclosures):

TBW.

Authentication:

TBW. (OAuth 2)

Example:

	POST example.com/api?method=open311.incidents.report

open311.incidents.getInfo
--

TBW.

Parameters:

* **id** (required)

* **format** (optional)

All dates are recorded using the [W3C DateTime format](http://www.w3.org/TR/NOTE-datetime).

All geographic data is recorded as
[WGS84](http://spatialreference.org/ref/epsg/4326/) projection.

Example:

	GET example.com/api?method=open311.incidents.getInfo&id=1

	{
		"id": 999,
		"service_id": 23,
		"status_id": 1,
		"reported": "2011-02-10T08:23:55-0800",
		"closed": "",
		"last_updated": "2011-02-11T11:48:22-0800",
		"latitude": 37.765,
		"longitude": -122.419,
		"casenotes": [],
		"extras": {

		}
	}

open311.incidents.search
--

TBW.

Parameters:

* **format** (optional)

All dates should be passed to the API (and returned in results) using the [W3C DateTime format](http://www.w3.org/TR/NOTE-datetime).

Example:

	GET example.com/api?method=open311.incidents.getInfo&id=1

	{
	"incidents": [
		{"id": 999, "service_id": 23, "status_id": 1 }
		]
	}
