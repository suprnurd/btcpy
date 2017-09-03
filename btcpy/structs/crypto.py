from binascii import hexlify, unhexlify
from base58 import b58decode_check
from ecdsa import SigningKey, SECP256k1
from ecdsa.util import sigencode_der

from ..lib.types import HexSerializable
from ..lib.codecs import Base58Codec
from .address import Address
from ..setup import is_mainnet


class PrivateKey(HexSerializable):

    highest_s = 0x7fffffffffffffffffffffffffffffff5d576e7357a4501ddfe92f46681b20a0

    @staticmethod
    def from_wif(wif):
        return PrivateKey(bytearray(b58decode_check(wif)[1:-1]))

    @staticmethod
    def from_bip32(bip32):
        if bip32[:4] not in {'xprv', 'tprv'}:
            raise ValueError("Key does not start with either 'xprv' or 'tprv'")
        decoded = Base58Codec.decode(bip32)
        if decoded[-33] != 0:
            raise ValueError('Byte -33 is not 0x00, {} instead'.format(decoded[-33]))
        return PrivateKey(decoded[-32:])

    @staticmethod
    def unhexlify(hexa):
        return PrivateKey(bytearray(unhexlify(hexa)))

    def __init__(self, priv):
        self.key = priv

    def pub(self, compressed=True):
        raw_pubkey = bytearray(SigningKey.from_string(self.key, curve=SECP256k1).get_verifying_key().to_string())
        uncompressed = PublicKey(bytearray([0x04]) + raw_pubkey)
        if compressed:
            return PublicKey(uncompressed.compressed)
        else:
            return uncompressed

    def serialize(self):
        return self.key

    def raw_sign(self, data):
        sig_key = SigningKey.from_string(self.key, curve=SECP256k1)
        r, s, order = sig_key.sign_digest(data, sigencode=lambda *x: x)
        if s < 0x01:
            raise ValueError('Too low s value for signature: {}'.format(s))
        # ref: https://github.com/bitcoin/bips/blob/master/bip-0062.mediawiki#Low_S_values_in_signatures
        if s > PrivateKey.highest_s:
            s = order - s
        if s.to_bytes(32, 'big')[0] > 0x7f:
            s = int.from_bytes(b'\x00' + s.to_bytes(32, 'big'), 'big')
        if r.to_bytes(32, 'big')[0] > 0x7f:
            r = int.from_bytes(b'\x00' + r.to_bytes(32, 'big'), 'big')
        return r, s, order

    def sign(self, data):
        return sigencode_der(*self.raw_sign(data))

    def __eq__(self, other):
        return self.key == other.key
    

class WrongPubKeyFormat(Exception):
    pass


class PublicKey(HexSerializable):

    p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
    uncompressed_bytes = 64
    compressed_bytes = uncompressed_bytes // 2
    types = {0x02: 'even',
             0x03: 'odd',
             0x04: 'uncompressed'}

    headers = {val: key for key, val in types.items()}

    @staticmethod
    def from_bip32(bip32):
        if bip32[:4] not in {'xpub', 'tpub'}:
            raise WrongPubKeyFormat("Key does not start with either 'xpub' or 'tpub'")
        decoded = Base58Codec.decode(bip32)
        return PublicKey(decoded[-33:])

    @staticmethod
    def unhexlify(hexa):
        return PublicKey(bytearray(unhexlify(hexa)))

    @staticmethod
    def from_priv(priv):
        return priv.pub()

    @staticmethod
    def uncompress(pubkey):
        header, *body = pubkey
        if header not in {0x02, 0x03}:
            raise WrongPubKeyFormat('Pubkey header does not indicate compressed key: 0x{:02x}'.format(header))
        PublicKey.check(pubkey)
        parity = header - 2  # if 0x02 parity is 0, if 0x03 parity is 1
        x = int.from_bytes(body, 'big')
        alpha = (pow(x, 3, PublicKey.p) + 7) % PublicKey.p
        y = pow(alpha, (PublicKey.p + 1)//4, PublicKey.p)
        if y % 2 != parity:
            y = -y % PublicKey.p
        return bytearray([0x04]) + bytearray(body) + bytearray(y.to_bytes(PublicKey.compressed_bytes, 'big'))

    @staticmethod
    def check(pubkey):
        if type(pubkey) not in {bytes, bytearray}:
            raise ValueError('Unexpected data type for pubkey: {}'.format(type(pubkey)))

        try:
            header, *body = pubkey
        except ValueError:
            raise WrongPubKeyFormat('Got only one byte')
        
        if header == 0x04:
            if len(body) != PublicKey.uncompressed_bytes:
                raise WrongPubKeyFormat('Unexpected length for uncompressed pubkey: {}'.format(len(body)))
        elif header in {0x02, 0x03}:
            if len(body) != PublicKey.compressed_bytes:
                raise WrongPubKeyFormat('Unexpected length for compressed pubkey: {}'.format(len(body)))
        else:
            raise WrongPubKeyFormat('Unknown pubkey header: 0x{:02x}'.format(header))

    def __init__(self, pubkey):
        self.__class__.check(pubkey)
        self.type = PublicKey.types[pubkey[0]]
        if self.type == 'uncompressed':
            self.uncompressed = pubkey
            header = 0x03 if self.uncompressed[-1] % 2 else 0x02
            self.compressed = bytearray([header]) + self.uncompressed[1:-PublicKey.compressed_bytes]
        else:
            self.compressed = pubkey
            self.uncompressed = PublicKey.uncompress(pubkey)

    def __str__(self):
        return self.hexlify()

    def __len__(self):
        return len(str(self)) // 2

    def hash(self):
        import hashlib
        original = self.uncompressed if self.type == 'uncompressed' else self.compressed
        sha = hashlib.sha256(original).digest()
        ripe = hashlib.new('ripemd160')
        ripe.update(sha)
        return bytearray(ripe.digest())
    
    def serialize(self):
        return self.uncompressed if self.type == 'uncompressed' else self.compressed

    def to_address(self, mainnet=None):
        if mainnet is None:
            mainnet = is_mainnet()
        return Address('p2pkh', self.hash(), mainnet)

    def to_segwit_address(self, mainnet=None):
        if mainnet is None:
            mainnet = is_mainnet()
        return Address('p2wpkh', self.hash(), mainnet)

    def __eq__(self, other):
        return (self.type, self.compressed, self.uncompressed) == (other.type, other.compressed, other.uncompressed)
