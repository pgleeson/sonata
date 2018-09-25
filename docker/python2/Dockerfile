#
# A Docker image for installing SONATA and associated tools
#
# This image extends the basic "simulationx" image by adding support
# for libraries required for SONATA
#

# Use tagged version of neuralensemble/simulationx, e.g. Python 2, PyNN 0.9.1
FROM neuralensemble/simulationx:py2_pynn091
 
LABEL maintainer="p.gleeson@gmail.com" 

USER root

################################################################################
# Update some Python & Java libraries
RUN apt-get update && \
     apt-get install -y default-jdk python-tk python-lxml htop python-pip
# Required for BMTK
RUN pip install pandas


################################################################################
# Enable NEST, NEURON & Brian...

# Activate virtual env for neuralensemble libraries
RUN /bin/bash -c "source ~/env/neurosci/bin/activate"

# Set up NEURON (should be updated in neuralensemble/simulationx:py2...)
ENV PATH=$PATH:$HOME/env/neurosci/x86_64/bin
ENV NEURON_HOME=$HOME/env/neurosci/x86_64


################################################################################
# Install NeuroML Python libraries

RUN pip install git+https://github.com/NeuralEnsemble/libNeuroML.git@development
RUN git clone https://github.com/NeuroML/NeuroMLlite && cd NeuroMLlite && \
    python setup.py install && cd -

RUN pip install git+https://github.com/NeuroML/pyNeuroML


################################################################################
# Install NetPyNE

RUN git clone https://github.com/Neurosim-lab/netpyne.git && cd netpyne && \
    git checkout neuroml_export && python setup.py install && cd -


################################################################################
# Install BMTK

RUN $HOME/env/neurosci/bin/pip install Cython==0.23
RUN git clone https://github.com/AllenInstitute/bmtk.git && cd bmtk && \
    python setup.py install ; cd -


################################################################################
# Finish up

# Copy helper script for printing versions of packages
COPY versioninfo.py .

# Some aliases
RUN echo '\n\nalias cd..="cd .."\nalias h=history\nalias ll="ls -alt"' >> ~/.bashrc

RUN echo "Built the main SONATA Docker image!"



