def pad(raw_data: bytes, block_size: int):
    """Pad raw_data to a multiple of block_size."""
    # Calculate the number of padding bytes required
    padding = block_size - (len(raw_data) % block_size)
    # Pad the data

    if padding == 0:
        return raw_data + bytes([block_size] * block_size)
    else:
        return raw_data + bytes([padding] * padding)


def remove_pad(data: bytes):
    """Remove PKCS#7 padding from data."""
    # Get the last byte
    last_byte = data[-1]
    # Check that the last byte is between 1 and 16
    if last_byte < 1 or last_byte > 16:
        raise ValueError("Invalid padding")
    # Check that the last n bytes are all equal to the last byte
    if data[-last_byte:] != bytes([last_byte] * last_byte):
        raise ValueError("Invalid padding")
    # Return the data without the padding
    return data[:-last_byte]
