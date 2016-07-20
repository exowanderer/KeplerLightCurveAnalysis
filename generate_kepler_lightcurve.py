from astropy.table import vstack, Table
from glob import glob
import untrendy
from time import time

dirname = '/Users/jonathanfraine/Research/Planets/HATP11/data/kepler/'

kepfitsnames = glob(dirname + '*')

keptable     = Table.read(kepfitsnames[0])

for fname in kepfitsnames[1:]:
    keptable = vstack([keptable, Table.read(fname)])

start=time();
keplc_utd = untrendy.untrend(keptable['TIME'], keptable['SAP_FLUX'], keptable['SAP_FLUX_ERR']);
time()-start
