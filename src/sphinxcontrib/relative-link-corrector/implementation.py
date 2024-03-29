# Copyright 2020 Nokia
# Licensed under the Apache License 2.0.
# SPDX-License-Identifier: Apache-2.0

# © 2020 Nokia
#
# Licensed under the Apache License 2.0
#
# SPDX-License-Identifier: Apache-2.0

###
# A sphinx extension to support the relative linking of html files.
# Inspired by and partly copyed from 
# https://github.com/firegurafiku/sphinxcontrib-divparams/
###

import sphinx
from sphinx.util import logging
import bs4
import shutil
import os
import re

logger = logging.getLogger(__name__)

# NoUri was moved in 3.0 https://www.sphinx-doc.org/en/master/extdev/deprecated.html#dev-deprecated-apis

if sphinx.version_info [:2] < (3, 0):
    from sphinx.environment import NoUri
else:
    from sphinx.errors import NoUri

def transform_html(soup):
    links = soup.find_all("a")
    for link in links:
        #logger.info("l: " + str(link))
        if link.has_attr("href"):
            logger.debug(__name__ + ": line " + str(link['href']))
            if "://" not in link['href']:
                res = re.search("(\.md\#|\.md$)", link['href'])
                if res:
                    corect_link = link['href'].replace(".md", ".html")
                    logger.debug(__name__ + ": corrected link is " + corect_link)
                    link['href'] = corect_link
                else: 
                    logger.debug(__name__ + ": there no match of .md")
            else: 
                logger.debug(__name__ + ": this is an absolulte link")
        
        logger.debug(__name__ + ": link correction")

def relative_link_corrector(app, exception):
    logger.info("relative-link-corrector starts to correct relative links")

    # Don't risk doing anything if Sphinx failed in building HTML.
    if exception is not None:
        return

    # Find all files eligible for DOM transform.
    # See also: http://stackoverflow.com/a/33640970/1447225
    target_files = []
    for doc in app.env.found_docs:
        target_filename = "#"
        try:
            target_filename = app.builder.get_target_uri(doc)
        except NoUri:
            continue
        if '#' in target_filename:
            logger.info("Skipping")
            continue

#        logger.info("tfn1: " + target_filename)
        target_filename = os.path.join(app.outdir, target_filename)
#        logger.info("tfn2: " + target_filename)
        target_filename = os.path.abspath(target_filename)
#        logger.info("tfn3: " + target_filename)
        target_files.append(target_filename)

    for fn in target_files:
        try:
            with open(fn, mode="rb") as f:
                soup = bs4.BeautifulSoup(f.read(), "html.parser")

            transform_html(soup)
            html = soup.prettify(encoding=app.config.html_output_encoding)

            with open(fn, mode='wb') as f:
                f.write(html)

        except Exception as exc:
            app.warning(__name__ + ": Exception raised during HTML tweaking: " + str(exc))

