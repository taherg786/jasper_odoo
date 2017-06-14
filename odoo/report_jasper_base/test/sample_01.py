# encoding: utf-8

import os
import sys

sys.path.insert(0, '../base')
from JasperInterface import JasperInterface

from jnius import autoclass

if __name__ == '__main__':
    files = {}
    files['main'] = open('JsonCustomersReportSingle.jrxml').read()
    
    jasper = JasperInterface(files, './')
    
    jsonstream = open('northwind.json').read()
    
    open('./JsonCustomersReportSingle.pdf', 'wb').write(jasper.generate(jsonstream))