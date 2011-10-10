#!/usr/bin/env python

import os.path
import json
import sys
import StringIO

import logging
logging.basicConfig(level=logging.DEBUG)

# TO DO: import py-markdown and generate other kinds of docs

if __name__ == '__main__':

    spec = sys.argv[1]

    path = os.path.abspath(spec)
    root = os.path.dirname(path)

    fh = open(spec, 'r')
    data = json.load(fh)

    out = StringIO.StringIO()

    out.write("API Methods\n")
    out.write("==\n\n")

    out.write("_This file is auto-generated using the []() program_\n\n")

    for m in data['methods']:

        if not m['enabled']:
            logging.notice("%s is disabled, skipping" % m['name'])
            continue

        if not m['documented']:
            logging.notice("%s is enabled but undocumented, skipping" % m['name'])
            continue

        out.write("%s\n" % m['name'])
        out.write("--\n\n")

        if m['requires_auth']:
            out.write("**This method requires authentication**\n\n")

        out.write("%s\n\n" % m['description'])

        """
        method parameters
        """

        if m.get('parameters', False):

            out.write("Parameters\n\n")
        
            for p in m['parameters']:

                out.write("* **%s** - %s" % (p['name'], p['description']))
            
                if p['required']:
                    out.write(" _required_")

                out.write("\n")

        if m.get('paginated', False):

            out.write("* **page** - TBW. Default is 1.\n")
            out.write("* **per_page** - TBW.\n")

        out.write("* **format** - TBW. Default is JSON\n")
        out.write("\n")

        """
        method notes
        """

        if m.get('notes', False):

            out.write("Notes\n\n")
            
            for n in m['notes']:
                out.write("%s\n\n" % n)

        """
        example (need to work out how to squirt this into JSON...
        """

        out.write("Example\n\n")
        out.write("TBW\n\n")

    md = out.getvalue()

    outfile = os.path.join(root, "api-methods.md")
    outfh = open(outfile, 'w')
    outfh.write(md)
    outfh.close()
