# share_secret.py
from secretsharing import PlaintextToHexSecretSharer

# Hardcoded values for n and k
n = 4  # Number of shares
k = 3  # Threshold (minimum shares required to reconstruct the key)

# Split AES Key using Shamir’s Secret Sharing
def split_key(key):
    """
    Split the AES key into n shares with a threshold of k shares required to reconstruct the key.
    """
    # Convert the key to hex if it's in bytes
    if isinstance(key, bytes):
        key = key.hex()  # Convert bytes to hex string
    
    # Ensure k < n
    if k >= n:
        raise ValueError("Threshold (k) must be less than the number of shares (n).")
    
    # Use the secret sharing library to split the key
    shares = PlaintextToHexSecretSharer.split_secret(key, n, k)
    
    return shares

# Reconstruct AES Key from Shares
def reconstruct_key(shares):
    """
    Reconstruct the AES key from the given shares.
    """
    # Convert the shares into the correct format (x-y).
    formatted_shares = []
    for share in shares:
        # Ensure the share is in the expected 'x-y' format
        if '-' not in share:
            raise ValueError(f"Invalid share format: {share}. Share should be in 'x-y' format.")
        formatted_shares.append(share)
    
    # Recover the secret (AES key) from the shares
    key_hex = PlaintextToHexSecretSharer.recover_secret(formatted_shares)
    
    # Return the reconstructed key
    return bytes.fromhex(key_hex)

