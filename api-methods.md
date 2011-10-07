API methods
==

open311.searvices.getList
--

Returns a list of services for which incidents may be reported.

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

open311.incidents.report
--

TBW.

Returns a unique ID for the incident that may be used to call the
_open311.incidents.status_ API method.

Parameters:

* **service_id** (required)

* **format** (optional)

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

Example:

	GET example.com/api?method=open311.incidents.getInfo&id=1

	{
	"incidents": [
		{"id": 999, "service_id": 23, "status_id": 1 }
		]
	}

open311.incidents.getStatuses
--

TBW.

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
