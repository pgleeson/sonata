import numpy as np
from neuron import h
from bmtk.builder import NetworkBuilder

net = NetworkBuilder("smallIClamp")

def generate_positions(N, x0=0.0, x1=300.0, y0=0.0, y1=100.0):
    X = np.random.uniform(x0, x1, N)
    Y = np.random.uniform(y0, y1, N)
    return X, Y

per_pop = 4

pos_x, pos_y = generate_positions(per_pop)

template = 'nest:iaf_psc_alpha'

net.add_nodes(N=per_pop, pop_name='LIF_exc', location='VisL4', ei='e',
              model_type='point_process',  # use point_process to indicate were are using point model cells
              model_template=template,
              x=pos_x, y=pos_y,
              dynamics_params='472363762_point.json')
              
pos_x, pos_y = generate_positions(per_pop)

net.add_nodes(N=per_pop, pop_name='LIF_inh', location='VisL4', ei='i',
              model_type='point_process',  # use point_process to indicate were are using point model cells
              model_template=template, 
              x=pos_x, y=pos_y,
              dynamics_params='472363762_point.json')
              
              
def recurrent_connections(src_cells, trg_cell, n_syns):
    if np.random.random() > 0.3:
        synapses = [n_syns]*len(src_cells)
    else:
        synapses = [None]*len(src_cells)
    return synapses


net.add_edges(source={'ei': 'e'}, target={'ei': 'i', 'model_type': 'point_process'},
              iterator='all_to_one',
              connection_rule=recurrent_connections,
              connection_params={'n_syns': 1},
              syn_weight=0.01,
              weight_function='wmax',
              delay=2.0,
              dynamics_params='ExcToInh.json',
              model_template='static_synapse')


net.build()
net.save(output_dir='network')

print 'done'
