import sys

import neuron
print(">>>  NEURON:            version %s"%neuron.h.nrnversion())


try:
    import nest
    print(">>>  NEST:          version %s"%nest.version())
except Exception as e:
    print(">>>  No PyNEST:     %s"%e)


try:
    import brian
    print(">>>  Brian:         version %s"%brian.__version__)
except Exception as e:
    print(">>>  No Brian1:     %s"%e)


try:
    import brian2
    print(">>>  Brian2:        version %s"%brian2.__version__)
except Exception as e:
    print(">>>  No Brian2:     %s"%e)


try:
    import neuroml
    print(">>>  libNeuroML:    version %s"%neuroml.__version__)
except Exception as e:
    print(">>>  No libNeuroML: %s"%e)


try:
    import pyneuroml
    print(">>>  pyNeuroML:     version %s"%pyneuroml.__version__)
except Exception as e:
    print(">>>  No pyNeuroML:  %s"%e)

try:
    import neuromllite
    print(">>>  NeuroMLlite:   version %s"%neuromllite.__version__)
except Exception as e:
    print(">>>  No NeuroMLlite: %s"%e)


try:
    import netpyne
    print(">>>  NetPyNE:       version %s"%netpyne.__version__)
except Exception as e:
    print(">>>  No NetPyNE:    %s"%e)

try:
    import bmtk
    print(">>>  BMTK:          version %s"%bmtk.__version__)
except Exception as e: 
    print(">>>  No BMTK:       %s"%e)


try:
    import numpy
    print(">>>  Numpy:         version %s"%numpy.__version__)
except Exception as e:
    print(">>>  No Numpy:      %s"%e)
    
try:
    import tables
    print(">>>  pyTables:      version %s"%tables.__version__)
except Exception as e:
    print(">>>  No pyTables:   %s"%e)
try:
    import pandas
    print(">>>  pandas:        version %s"%pandas.__version__)
except Exception as e:
    print(">>>  No pandas:     %s"%e)
    
import pyNN
print(">>>  PyNN:          version %s"%pyNN.__version__)
    
print(">>>  Python         version %s"% sys.version)




