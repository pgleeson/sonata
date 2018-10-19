import sys, os
from bmtk.simulator import bionet


def run(config_file):
    conf = bionet.Config.from_json(config_file, validate=True)
    conf.build_env()
    net = bionet.BioNetwork.from_config(conf)
    sim = bionet.BioSimulator.from_config(conf, network=net)
    sim.run()


run('config.json')
