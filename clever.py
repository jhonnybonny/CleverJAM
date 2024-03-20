#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import time
import json
import random
import xmlrpc.client
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CleverJAM')
    parser.add_argument('-s', '--host', dest='host', default='localhost',
            help='hostname to send RPC commands (default: "localhost")')
    parser.add_argument('-p', '--port', dest='port', default=8888,
            help='RPC server port (e.g: 8888 by default)')
    parser.add_argument('-f', '--file', dest='filepath', required=True,
            help='CleverJAM json file')
    parser.add_argument('-d', '--delay', dest='delay', default=2,
            help='Delay between each frequency to jam in sec (default: 2)')
    parser.add_argument('-b', '--Bandwidth', dest='Bandwidth', default=None,
            help='Define a static Bandwidth. Will also influence the sample rate. By default it will use the Bandwidth of the JSON file')

    t_freqs = {}
    args = parser.parse_args()
    
    host = args.host
    port = int(args.port)
    
    filepath = args.filepath
    delay = float(args.delay)
    Bandwidth = args.Bandwidth

    s = xmlrpc.client.ServerProxy("http://%s:%s" % (host, port))
    
    
    
    with open(filepath) as f:
        jamdata = json.load(f)
        
    for key, val in jamdata.items():
    
            findex = None
            cbandwidth = 10 # MHz
            
            if 'Freq' in val:
                #findex = val['Freq']
                cent_freq = val['Freq']
                
            if Bandwidth is not None:
                cbandwidth = Bandwidth
            else:
                if 'Bandwidth' in val:
                    cbandwidth = int(val['Bandwidth'].replace('MHz',''))    
            try:
                    t_freqs[key] = {    'Freq' : cent_freq,
                                        'Bandwidth' : cbandwidth } 
            except Exception as e:
                print (e)

###################################################PRINT SPACE###########################################################

    while True:
        for key, val in t_freqs.items():
            print ("\033[2;30;43m|JUMP|\033[0;0m\033[2;31;40m --- Jamming {cell} frequency at {Freq} with {Bandwidth} MHz bandwidth \033[0;0m".format(cell=key, Freq=val['Freq'], Bandwidth=val['Bandwidth']))
            #s.set_var_cent_freq(val['Freq']*1000000)
            s.set_var_cent_freq(val['Freq'])
            s.set_var_bandwidth(val['Bandwidth']*1000000)
            
            time.sleep(delay)
