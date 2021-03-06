#!/usr/bin/env python3

"""
Python script that converts BibTeX
entries to CSV.
Input is via standard input.
Output is via standard output.
"""

from re import match
from re import search
from re import findall
from sys import stdin

ENTRIES = []
ENTRY = {}

#De enkelte elementer af den Bibtexstregn vi indlæser, klippes i stykker.
for line in stdin:
    if match('^@', line.strip()):
        if ENTRY != {}:
            ENTRIES.append(ENTRY)
            entry = {}
    elif match('url', line.strip()):
        value, = findall("\\s+", line)
        entry["url"] = value
    elif search('=', line.strip()):
        key, value = [v.strip(" {},\n") for v in line.split("=", 1)]
        entry[key] = value

#Listen ENTREES løbes igennem, alle værdier udskrives. Hvis elementet er tomt
#udskrives N/A (not avalible) på den tomme plads.
for entry in ENTRIES:
    try:
        issn = entry["ISSN"]
    except KeyError:
        issn = 'N/A'
    try:
        doi = entry["DOI"]
    except KeyError:
        doi = 'N/A'
    try:
        title = entry["Title"]
    except KeyError:
        title = 'N/A'
    try:
        oa = entry["OA"]
    except KeyError:
        oa = 'N/A'
    try:
        affiliation = entry["Affiliation"]
    except KeyError:
        affiliation = 'N/A'
    try:
        journal = entry["Journal"]
    except KeyError:
        journal = 'N/A'
    try:
        publisher = entry["Publisher"]
    except KeyError:
        publisher = 'N/A'
    try:
        funding = entry["Funding-acknowledgement"]
    except KeyError:
        funding = 'N/A'
    try:
        fundtext = entry["Funding-text"]
    except KeyError:
        fundtext = 'N/A'

    #Elementerne printes, såfremt vi specificerer stdout skrives til fil - ellers til skærm.
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}" \
    .format(issn, doi, title, oa, affiliation, journal, publisher, funding, fundtext))
