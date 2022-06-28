from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, GT, pair
from charm.toolbox.msp import MSP
import CABEnc

debug = False

# Type Annotations

# PUBLIC KEY Pk = (g, g2 , h , f , e(g,g)^alpha)
pk_t = {
    'g': G1,
    'g2': G2,
    'h': G1,
    'f': G1,
    'e_gg_alpha': GT
}


class CABE(CABEnc):

    def __init__(self, group_obj, verbose=False):
        CABEnc.__init__(self)
        self.group = group_obj
        self.util = MSP(self.group, verbose)

    def setup(self):
        """

        """

        if debug:
            print('CCP-CABE: setup')

    def keygen(self):
        """

        """

    def encdelegate(self):
        """

        """

    def encrypt(self):
        """

        """

    def decdelegate(self):
        """

        """

    def decrypt(self):
        """

        """
