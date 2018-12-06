# (C) British Crown Copyright 2017, Met Office
#
# This code is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#

# Store a set of weather observations in a Copernicus Exchange Format (CEF) file

import io
import pandas

def write_file(obs,file_name):
    """Load all observations for one calendar month (for one variable)

    Data must be available in directory ../../data.

    Args:
        file_name (:obj:`str`): File (or 'open'able object)

    Returns:
        :obj:`dict`: Data as key:value pairs.

    Raises:
        ValueError: obs not a CEF structure
        IOError: Not a readable CEF file.

    |
    """

    try:    
       version=obs['CEF']
       iversion=[int(x) for x in version.split('.')]
       if iversion[0]>0 or iversion[1]>0:
           raise IOError("CEF versions > 0.0 are not supported")
    except:
       raise ValueError("This does not look like a CEF datastructure")

    f=io.open(file_name,'w',encoding='utf8')
    # Header first
    for header in ('CEF','ID','Name','Lat','Lon','Alt','Source','Repro',
                   'Var'):
        if(obs[header] is not None):
            f.write("%s\t%s\n" % (header,obs[header]))
        else:
            f.write("%s\t\n" % header)
    # Meta might need packing
    if obs['Meta'] is None:
        f.write("Meta\t\n")
    elif isinstance(obs['Meta'], basestring):
        f.write("Meta\t%s\n" % obs['Meta'])
    else:
        f.write("Meta\t%s\n" %  ','.join(obs['Meta']))
    # Add the data table
    obs['Data'].to_csv(f,sep='\t',columns=('Year','Month',
                                           'Day','HHMM',
                                           'TimeF','Value',
                                           'Meta'),
                       header=True)
    f.close()

