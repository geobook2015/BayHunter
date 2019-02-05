import numpy as np
import os.path as op
from BayHunter import SynthObs

# idx = 1
# h = [34, 0]
# vs = [3.5, 4.4]

# idx = 2
# h = [5, 29, 0]
# vs = [3.4, 3.8, 4.5]

idx = 3
h = [5, 23, 8, 0]
vs = [2.7, 3.6, 3.8, 4.4]

path = 'observed'
datafile = op.join(path, 'st%d_%s.dat' % (idx, '%s'))

# surface waves
sw_x = np.linspace(1, 41, 21)
swdata = SynthObs.return_swddata(h, vs, vpvs=1.73, x=sw_x)
SynthObs.save_data(swdata, outfile=datafile)

for slowness in [5.2, 7.0, 8.5]:
    datafile = op.join(path, 'st%d_%s_%.2f.dat' % (idx, '%s', slowness))
    rfdata = SynthObs.return_rfdata(
        h, vs, vpvs=1.73, pars={'p': slowness}, x=None)
    SynthObs.save_data(rfdata, outfile=datafile)

modfile = op.join(path, 'st%d_mod.dat' % idx)
SynthObs.save_model(h, vs, vpvs=1.73, outfile=modfile)
