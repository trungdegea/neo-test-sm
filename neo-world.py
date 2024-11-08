from boa3.builtin.compile_time import NeoMetadata, metadata, public
from boa3.builtin.interop import storage

# Define the metadata for the smart contract
@metadata
def manifest_metadata() -> NeoMetadata:
    meta = NeoMetadata()
    meta.author = "Hermes test contract NEO3"
    meta.email = "trungdegea30032000@gmail.com"
    meta.description = 'This is a contract example to store data on NEO3'
    return meta

@public
def main():
    storage.put(b'script_saved', b'Hello world, Welcome to NEO Smart Economy!')
    
@public
def get_saved_data() -> bytes:
    saved_data = storage.get(b'script_saved')
    if saved_data is not None:
        return saved_data
    else:
        return b"No data found."
# 0x0cf69f1cf6d39abe0709e50da822cabbdd5b82c5