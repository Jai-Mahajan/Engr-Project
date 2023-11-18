import CoreBluetooth
class BluetoothManager: NSObject, CBCentralManagerDelegate, CBPeripheralManagerDelegate {
  var centralManager: CBCentralManager?
  var peripheralManager: CBPeripheralManager?
  var peripheral: CBPeripheral?}
let bluetoothManager = BluetoothManager()
bluetoothManager.centralManager = CBCentralManager(delegate: bluetoothManager, queue: nil)

func centralManagerDidUpdateState(_ central: CBCentralManager) {
if central.state == .poweredOn {
  central.scanForPeripherals(withServices: nil, options: nil)}
}

func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral,
advertisementData: [String : Any], rssi RSSI: NSNumber) {
  if peripheral.name == "MyPeripheral" {

central.stopScan()
self.peripheral = peripheral
central.connect(peripheral, options: nil)
}
}
func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
peripheral.delegate = self
peripheral.discoverServices(nil)
}
func peripheralManagerDidUpdateState(_ peripheral: CBPeripheralManager) {
if peripheral.state == .poweredOn {
let serviceUUID = CBUUID(string: "MyServiceUUID")
let service = CBMutableService(type: serviceUUID, primary: true)
let characteristicUUID = CBUUID(string: "MyCharacteristicUUID")
let characteristic = CBMutableCharacteristic(type: characteristicUUID, properties: [.read, .write],
value: nil, permissions: [.readable, .writeable])
service.characteristics = [characteristic]
peripheral.add(service)
peripheral.startAdvertising([CBAdvertisementDataLocalNameKey: "MyPeripheral",
CBAdvertisementDataServiceUUIDsKey: [serviceUUID]])
}
}
func peripheralManager(_ peripheral: CBPeripheralManager, didReceiveWrite requests: [CBATTRequest]) {
for request in requests {
if request.characteristic.uuid == CBUUID(string: "MyCharacteristicUUID") {
// Handle incoming data here
}
}
}

if motionManager.isAccelerometerAvailable {
// Accelerometer is available
} else {
// Accelerometer is not available
}
motionManager.accelerometerUpdateInterval = 0.1 // Update interval in seconds

motionManager.startAccelerometerUpdates(to: .main) { (data, error) in
if let accelerometerData = data {
let speed = sqrt(pow(accelerometerData.acceleration.x, 2) + pow(accelerometerData.acceleration.y, 2)
+ pow(accelerometerData.acceleration.z, 2))
// Use the speed value here}
}