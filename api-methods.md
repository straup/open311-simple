API Methods
==

_This file is auto-generated using the [api-methods.json](https://github.com/straup/open311-simple/blob/master/api-methods.json) specification and the [mk-api-docs](https://github.com/straup/open311-simple/blob/master/bin/mk-api-docs.py) program and compliments the [general API notes](https://github.com/straup/open311-simple/blob/master/api.md)_.

open311.services.getList
--

Returns a list of services for which incidents may be reported. The types of services and their meaning are left to the discretion of individual cities.

**Parameters**

* **page** - The page of results to return. If this argument is omitted, it defaults to 1..
* **per_page** - Number of results to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is left to the discretion of individual cities.
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Example**

_TBW_

open311.services.getInfo
--

Returns basic information (as included in the _open311.services.getList_ method) as well any additional details that may be relevant to the service.

**Parameters**

* **service\_id** -  _required_
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Example**

_TBW_

open311.incidents.getStatuses
--

Return a list of valid statuses. The types of statuses and their meaning are left to the discretion of individual cities.

**Parameters**

* **page** - The page of results to return. If this argument is omitted, it defaults to 1..
* **per_page** - Number of results to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is left to the discretion of individual cities.
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Example**

_TBW_

open311.incidents.report
--

**This method requires authentication**

Report an incident for a given service. Returns a unique ID for the incident that may be used to call the _open311.incidents.status_ API method.

**Parameters**

* **service\_id** - A valid service_id as defined by the city operating the Open 311 (Simple) API _required_
* **latitude** - A valid WGS84 coordinate _required_
* **longitude** - A valid WGS84 coordinate _required_
* **notes** - A free-form text field in which the user reporting the incident may leave additional notes.
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Notes**

All geographic data is expected to be using the [WGS84](http://spatialreference.org/ref/epsg/4326/) projection.

**Example**

_TBW_

open311.incidents.getInfo
--



**Parameters**

* **incident\_id** - The unique ID of the incident to get information about. _required_
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Notes**

All dates are recorded using the [W3C DateTime format](http://www.w3.org/TR/NOTE-datetime).

All geographic data is returned using the [WGS84](http://spatialreference.org/ref/epsg/4326/) projection.

**Example**

_TBW_

open311.incidents.search
--

Returns a list of incidents matching a search criteria as defined by the API request.

**Parameters**

* **incident\_id** - TBW
* **status\_id** - TBW
* **page** - The page of results to return. If this argument is omitted, it defaults to 1..
* **per_page** - Number of results to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is left to the discretion of individual cities.
* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON

**Notes**

All dates should be passed to the API (and returned in results) using the [W3C DateTime format](http://www.w3.org/TR/NOTE-datetime).

**Example**

_TBW_

