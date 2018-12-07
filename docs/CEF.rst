The CEF File Format
===================

CEF files look like this:

.. literalinclude:: ../examples/basic.tsv

One CEF file contains observations of one variable from one station. It is a text file encoded as `UTF8 <https://en.wikipedia.org/wiki/UTF-8>`_. It is a `tab-separated values <https://en.wikipedia.org/wiki/Tab-separated_values>`_ file and should have a ``.tsv`` extension. This means it can be easily viewed and edited in any text editor or spreadsheet program (though care should be taken to preserve the tab structure and text encoding).

Header
------

The first 10 lines of the file are a series of headers, each given as a ``name``::``value`` pair separated by a tab. They must be in the order given. Missing values can be given as ``NA`` or left blank. The version number must be present.

   ``CEF``:
   The first three characters in the file must be ``CEF``. The associated value is the `semantic version <https://semver.org/>`_ of the format used. This enables software to recognise the format and read the rest of the file correctly. At the moment, only version 0.0 is in use.

   ``ID``: 
   `WIGOS <http://www.wmo.int/pages/prog/www/wigos/index_en.html>`_ compatible station identifier. "The local identifier may be up to 16 characters long. It must not contain blanks [...]. The local identifier may contain only lower-case or upper-case Latin letters, numbers or the characters: - (dash), _ (underscore) or . (full stop)." (`Source <https://library.wmo.int/opac/doc_num.php?explnum_id=4007>`_). This is the *machine readable* name of the station.

   ``Name``:
   Station name - any string (except no tabs or carriage returns). This is the *human readable* name of the station.

   ``Lat``:
   Latitude of the station (degrees north). 

   ``Lon``:
   Longitude of the station (degrees east). 

   ``Alt``:
   Altitude of the station (meters above sea-level). 

   ``Source``:
   Source identifier. This is for making collections of CEF files and identifies a group of files from the same source. It will be set by the collector.  Any string (except no tabs or carriage returns).

   ``Repo``:
   Link to the C3S DRS metadata repository. To be specified by Antonia.

   ``Var``:
   Name of the variable included in the file. There is a recommended list of standard variable names. Use this if possible.

   ``Meta``:
   Anything else. Comma-separated string of metadata entries. Each entry may be any string (except no tabs, commas, or carriage returns). There is a standard list of meaningful entries, but other entries can be added as necessary. Metadata specified here is assumed to apply to all observations in this file, unless overwritten by the observation-specific metadata entry.

Data table
----------

Lines 11 and onward in the file are a table of observations. Line 11 is a header, lines 12 and on are observations. Missing values can be given as ``NA`` or left blank. The table must contain these columns in this order:

   ``Year``: 
   Year in which the observation was made (UTC). An integer.

   ``Month``: 
   Month in which the observation was made (UTC). An integer (1-12).

   ``Day``: 
   Day of month in which the observation was made (UTC). An integer (1-31). 

   ``HHMM``: 
   Time of day at which the observation was made (UTC). A 4-digit integer where the first 2 digits give the hour of the observation, and the last two digits give the minute. If the hour of observation is less than 10, the first digit may be omitted. 

   ``TimeF``:
   Time period of observation (instantanious, integrated over previous 24 hours, ...). Integer code. There is a table of meaningful codes.

   ``Value``:
   The observation value.

   ``Meta``:
   Anything else. Comma-separated string of metadata entries. Each entry may be any string (except no tabs, commas, or carriage returns). There is a standard list of meaningful entries, but other entries can be added as necessary. Metadata specified here only applies to this observation, and overrides any file-wide specification.
