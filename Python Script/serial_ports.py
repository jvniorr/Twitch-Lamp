import serial
import questionary


def get_serial_ports():
    ports = ['COM%s' % (i + 1) for i in range(256)]
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)

        except (OSError, serial.SerialException):
            pass
    result.append('Refresh')
    return result


def select_serial_port():
    selected_port = questionary.select('Select the arduino serial port',
                                       choices=get_serial_ports()).ask()
    return selected_port
