import hashlib

SUPPORTED_HASHES = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha224": hashlib.sha224,
    "sha256": hashlib.sha256,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512,
    "blake2b": hashlib.blake2b,
    "blake2s": hashlib.blake2s,
    "sha3_224": hashlib.sha3_224,
    "sha3_256": hashlib.sha3_256,
    "sha3_384": hashlib.sha3_384,
    "sha3_512": hashlib.sha3_512,
}


def hash_text(text: str, algorithm: str = "sha256") -> str:
    algorithm = algorithm.lower()

    if algorithm not in SUPPORTED_HASHES:
        raise ValueError("Unsupported hash algorithm.")

    hasher = SUPPORTED_HASHES[algorithm]()
    hasher.update(text.encode("utf-8"))

    return hasher.hexdigest()