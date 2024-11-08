
# NEO3 Smart Contract Example

This repository contains an example smart contract for the NEO blockchain. The contract is written in Python using `neo3-boa`, designed to store and retrieve a simple message on the NEO blockchain.

## Project Structure

```
.
├── neo-world.py            # Main smart contract code
└── README.md               # Project documentation
```

## Prerequisites

- Python 3.8.10
- [neo3-boa](https://github.com/neo-project/neo3-boa) v1.0.1
- [neo-express](https://github.com/neo-project/neo-express) for local NEO blockchain testing

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**:
   Ensure that `neo3-boa` is installed. You can install it via pip:
   ```bash
   pip install neo3-boa==1.0.1
   ```

## Contract Overview

### Metadata

The contract metadata includes the author's information and a brief description:
- **Author**: Hermes test contract NEO3
- **Email**: trungdegea30032000@gmail.com
- **Description**: "This is a contract example to store data on NEO3"

### Functions

1. **main()**: 
   - This function saves a predefined message to the NEO blockchain storage.
   - Key: `b'script_saved'`
   - Value: `b'Hello world, Welcome to NEO Smart Economy!'`

2. **get_saved_data()**:
   - Retrieves and returns the stored message associated with the key `b'script_saved'`.
   - Returns the message as bytes if it exists, or a "No data found." message in bytes if it does not.

## Usage

1. **Compile the Smart Contract**:
   Run the following command to compile the contract:
   ```bash
   neo3-boa neo-world.py
   ```

2. **Deploy and Test**:
   Use `neo-express` to deploy the contract on a local NEO blockchain instance for testing. Ensure you have `neo-express` running and configured in your environment.

   - **Store data**: 
     Invoke the `main()` function to save data to the blockchain.

   - **Retrieve data**: 
     Invoke the `get_saved_data()` function to read the stored data.

## Example

### Save Data

```python
from boa3.builtin.interop.contract import call_contract

call_contract(<contract_hash>, 'main')
```

### Retrieve Data

```python
data = call_contract(<contract_hash>, 'get_saved_data')
print(data)
```

Replace `<contract_hash>` with the actual deployed contract hash.

## Troubleshooting

If you encounter issues with unsupported functions or types in `neo3-boa`, consider using simpler operations or raw bytes instead of attempting string decoding directly in the contract.

## License

This project is licensed under the MIT License.
