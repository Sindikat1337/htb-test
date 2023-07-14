from pymodbus.client.sync import ModbusTcpClient

# Connect to the MODBUS TCP device
client = ModbusTcpClient('94.237.63.218', port=37242)

# Connect to the device
client.connect()

# Read a holding register
slave_id = 0x34
address = 0x0006
num_registers = 0x01

# Read the register value
response = client.read_holding_registers(address, num_registers, unit=slave_id)

if response.isError():
    print("Error:", response)
else:
    register_value = response.registers[0]
    print("Register Value:", register_value)

# Close the connection
client.close()
