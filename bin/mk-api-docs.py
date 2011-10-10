#!/usr/bin/env python

import os.path
import json
import sys
import StringIO

import logging
logging.basicConfig(level=logging.DEBUG)

# TO DO: import py-markdown and generate other kinds of docs at the same time

if __name__ == '__main__':

    spec = sys.argv[1]

    path = os.path.abspath(spec)
    root = os.path.dirname(path)

    fh = open(spec, 'r')
    data = json.load(fh)

    out = StringIO.StringIO()

    out.write("API Methods\n")
    out.write("==\n\n")

    out.write("_This file is auto-generated using the [api-methods.json](https://github.com/straup/open311-simple/blob/master/api-methods.json) specification and the [mk-api-docs](https://github.com/straup/open311-simple/blob/master/bin/mk-api-docs.py) program and compliments the [general API notes](https://github.com/straup/open311-simple/blob/master/api.md)_.\n\n")

    for m in data['methods']:

        if not m['enabled']:
            logging.info("the '%s' method is disabled, skipping" % m['name'])
            continue

        if not m['documented']:
            logging.info("the '%s' method is enabled but undocumented, skipping" % m['name'])
            continue

        out.write("%s\n" % m['name'])
        out.write("--\n\n")

        if m['requires_auth']:
            out.write("**This method requires authentication**\n\n")

        out.write("%s\n\n" % m['description'])

        """
        method (HTTP)
        """

        out.write("**Method**\n\n")
        
        out.write("[%s](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)\n\n" % (m['method']))

        """
        method parameters
        """

        out.write("**Parameters**\n\n")

        if m.get('parameters', False):
        
            for p in m['parameters']:

                # guh...
                name = p['name'].replace("_", "\_")
                desc = p['description'].replace("_", "\_")
                
                out.write("* **%s** - %s" % (name, desc))
            
                if p['required']:
                    out.write(" - _Required_")

                out.write("\n")

        if m.get('paginated', False):

            out.write("* **page** - The page of results to return. If this argument is omitted, it defaults to 1.\n")
            out.write("* **per_page** - Number of results to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is left to the discretion of individual cities.\n")

        out.write("* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON\n")
        out.write("\n")

        """
        method notes
        """

        if m.get('notes', False):

            out.write("**Notes**\n\n")
            
            for n in m['notes']:
                out.write("* %s\n\n" % n)

        """
        example (need to work out how to squirt this into JSON...
        """

        out.write("**Example**\n\n")

        out.write("\t%s http://example.gov/open311-simple/?method=%s\n\n" % (m['method'], m['name']))
        out.write("\tTBW\n\n")

    md = out.getvalue()

    outfile = os.path.join(root, "api-methods.md")

    outfh = open(outfile, 'w')
    outfh.write(md)
    outfh.close()

    logging.info("Wrote new documentation (as markdown) to %s" % outfile)
