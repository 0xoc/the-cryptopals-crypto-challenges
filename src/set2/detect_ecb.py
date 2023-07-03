class ECBDetector:
    def __init__(self, ciphertext: bytes, block_size=16):
        self.block_size = block_size
        self.ciphertext = ciphertext

    def is_ecb(self):
        """Detect if the ciphertext is encrypted with ECB."""
        # Split the ciphertext into blocks
        blocks = [
            self.ciphertext[i : i + self.block_size]
            for i in range(0, len(self.ciphertext), self.block_size)
        ]
        # Count the number of duplicate blocks
        duplicate_blocks = len(blocks) - len(set(blocks))
        # Return True if there are duplicate blocks
        return duplicate_blocks > 0
