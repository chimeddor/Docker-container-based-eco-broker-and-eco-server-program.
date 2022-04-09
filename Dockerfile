FROM python 
WORKDIR /usr/src/app 
COPY . . 
RUN  apt-get -y update
RUN  apt-get -y install python3
RUN  apt-get -y install python3-pip
RUN  pip3 install jupyter
RUN  pip3 install python-socketio
#RUN  pip3 install simple-aml-library
RUN  pip3 install thread6
#RUN pip3 -m pip install --no-cache-dir -r requirements.txt
#FROM threading import *
#FROM  _thread import *
#     && import json \
 #    && import  os   \
  #   && from _thread import *
EXPOSE <port_number>

CMD python3 <echo_server> 

