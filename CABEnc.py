'''
Efficient Attribute-Based Comparable Data Access Control...
IEEE TRANSACTIONS ON COMPUTERS,
VOL. 64,
NO. 12,
DECEMBER 2015

Prototype Implementation
'''

from charm.toolbox.schemebase import *

class CABEnc(SchemeBase):
    def __init__(self):
        SchemeBase.__init__(self)
        SchemeBase._setProperty(self, scheme='ABEnc')  
        self.baseSecDefs = Enum('IND_AB_CPA', 'IND_AB_CCA', 'sIND_AB_CPA', 'sIND_AB_CCA') 

    def setup(self):
        raise NotImplementedError

    def keygen(self, pk, mk, object):
        raise NotImplementedError

    def encrypt(self, pk, M, object):
        raise NotImplementedError

    def decrypt(self, pk, sk, ct):
        raise NotImplementedError