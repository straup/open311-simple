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

    examples = os.path.join(root, 'api-methods-examples')

    fh = open(spec, 'r')
    spec = json.load(fh)

    out = StringIO.StringIO()

    out.write("API Methods\n")
    out.write("==\n\n")

    out.write("_This file is auto-generated using the [api-methods.json](https://github.com/straup/open311-simple/blob/master/api-methods.json) specification and the [mk-api-docs](https://github.com/straup/open311-simple/blob/master/bin/mk-api-docs.py) program and compliments the [general API notes](https://github.com/straup/open311-simple/blob/master/api.md)_.\n\n")

    """
    First group and sort methods by 'class'
    """

    classes = []
    methods = {}

    for fq_method in spec['methods'].keys():

        parts = fq_method.split(".")

        method_name = parts.pop()
        method_class = ".".join(parts)

        if not methods.get(method_class):
            methods[method_class] = []
            classes.append(method_class)            

        details = spec['methods'][fq_method]

        if not details['enabled']:
            logging.info("the '%s' method is disabled, skipping" % fq_method)
            continue

        if not details['documented']:
            logging.info("the '%s' method is enabled but undocumented, skipping" % fq_method)
            continue

        methods[method_class].append(fq_method)

    classes.sort()

    """
    Okay. Go!
    """

    for class_name in classes:

        class_methods = methods[class_name]

        # see above

        if len(class_methods) == 0:
            continue

        class_methods.sort()

        out.write("%s\n" % class_name)
        out.write("==\n\n")

        for fq_method in class_methods:

            details = spec['methods'][fq_method]

            out.write("%s\n" % fq_method)
            out.write("--\n\n")

            if details['requires_auth']:
                out.write("**This method requires authentication**\n\n")

            out.write("%s\n\n" % details['description'])

            """
            method (HTTP)
            """

            out.write("**Method**\n\n")
        
            out.write("[%s](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)\n\n" % (details['method']))

            """
            method parameters
            """

            out.write("**Parameters**\n\n")

            if details.get('parameters', False):
        
                for p in details['parameters']:

                    # guh...
                    name = p['name'].replace("_", "\_")
                    desc = p['description'].replace("_", "\_")
                
                    out.write("* **%s** - %s" % (name, desc))
            
                    if p['required']:
                        out.write(" - _Required_")

                    out.write("\n")

            if details.get('paginated', False):

                out.write("* **page** - The page of results to return. If this argument is omitted, it defaults to 1.\n")
                out.write("* **per_page** - Number of results to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is left to the discretion of individual cities.\n")

            out.write("* **format** - The encoding format for results. If this argument is omitted, it defaults to JSON\n")
            out.write("\n")

            """
            method notes
            """

            if details.get('notes', False):

                out.write("**Notes**\n\n")
            
                for n in details['notes']:
                    out.write("* %s\n\n" % n)

            """
            example
            """

            out.write("**Example**\n\n")

            out.write("\t%s http://example.gov/open311-simple/?method=%s\n\n" % (details['method'], fq_method))

            rsp = os.path.join(examples, "%s.json" % fq_method)

            if os.path.exists(rsp):

                fh = open(rsp, 'r')
                for ln in fh.readlines():
                    out.write("\t%s" % ln)

                out.write("\n")

    """
    write to disk
    """

    outfile = os.path.join(root, "api-methods.md")
    outfh = open(outfile, 'w')

    md = out.getvalue()
    outfh.write(md)
    outfh.close()

    logging.info("Wrote new documentation (as markdown) to %s" % outfile)
