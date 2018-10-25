import sys, os
from bmtk.simulator import bionet
from bmtk.analyzer.visualization.spikes import plot_spikes


def run(config_file):
    conf = bionet.Config.from_json(config_file, validate=True)
    conf.build_env()
    net = bionet.BioNetwork.from_config(conf)
    sim = bionet.BioSimulator.from_config(conf, network=net)
    sim.run()
    #bionet.nrn.quit_execution()
    plot_spikes('network/v1_nodes.h5', 'network/v1_node_types.csv', 'output/spikes.h5', group_key='pop_name')


run('config.json')
