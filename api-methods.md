API methods
==

open311.searvices.getList
--

Returns a list of services for which incidents may be reported.

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

Example:

	GET example.com/api?method=open311.services.getInfo&id=1

	{
		"id": 1,
		"name": "...",
		"type": "...",
		"description": "..."
	}

open311.incident.report
--

TBW.

Returns a unique ID for the incident that may be used to call the
_open311.incidents.status_ API method.

Example:

	POST example.com/api?method=open311.incident.getInfo&id=1

open311.incident.getInfo
--

TBW.

Example:

	GET example.com/api?method=open311.incident.getInfo&id=1

open311.incident.search
--

TBW.

Example:

	GET example.com/api?method=open311.incident.getInfo&id=1
