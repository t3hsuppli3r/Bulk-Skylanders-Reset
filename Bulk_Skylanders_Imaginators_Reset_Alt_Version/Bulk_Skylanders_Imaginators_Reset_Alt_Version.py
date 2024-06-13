import os

def read_nfc_dump(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    sectors = [data[i:i + 64] for i in range(0, len(data), 64)]
    return sectors

def write_nfc_dump(file_path, sectors):
    with open(file_path, 'wb') as f:
        for sector in sectors:
            f.write(sector)

def zero_non_preserved_blocks(sectors):
    for sector_index, sector in enumerate(sectors):
        if sector_index == 0:
            continue

        blocks = [sector[i:i + 16] for i in range(0, len(sector), 16)]
        for block_index in range(4):
            if block_index != 3:
                blocks[block_index] = bytes(16)
        sectors[sector_index] = b''.join(blocks)
    return sectors

output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

def sectors2blocks(sectors):
    sk = []
    for sector in sectors:
        sc = []
        for i in range(4):
            sc.append(sector[i*16:(i+1)*16])
        pass
        sk.append(sc)
    return sk
    pass

def blocks2sectors(blocks):
    sk = []
    for sector in blocks:
        sk.append(b''.join(sector))
    return sk
    pass

def create_clear():
    return [b'\x00' * 64 for i in range(16)]
    pass

def TEST_imaginator_clear(in_skylander):
    in_skylander_block = sectors2blocks(in_skylander)
    out_skylander = sectors2blocks(create_clear())
    for block in range(4):
        out_skylander[0][block] = in_skylander_block[0][block]
    out_skylander[1][0] = in_skylander_block[1][0]
    out_skylander[8][2] = in_skylander_block[8][2]
    out_skylander[15][2] = in_skylander_block[15][2]
    for sector in range(16):
        out_skylander[sector][3] = in_skylander_block[sector][3]
    return blocks2sectors(out_skylander)

input_dir = 'input'
os.makedirs(input_dir, exist_ok=True)

def bulk_imaginators_reset(path='.'):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            os.makedirs(full_path.replace('./input', './output'), exist_ok=True)
            bulk_imaginators_reset(full_path)
        else:
            write_nfc_dump(full_path.replace('./input', './output'), TEST_imaginator_clear(read_nfc_dump(full_path)))

directory_path = './input'
bulk_imaginators_reset(directory_path)