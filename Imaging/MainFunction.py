import angled_corners
import line
import serial


def CornerInput():
    return line.finalcorners()


def AngleOut(CornerArray):
    analyzed_angles = angled_corners.ArrayAnalyzer(CornerArray)
    return angled_corners.CompiledAnglePure(analyzed_angles)


def Main():
    ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=0)
    while True:
        if raw_input():
            break
        given_corners = CornerInput()
        angle = AngleOut(given_corners)
        ser.write(str(angle).encode())
        print angle
    ser.close()


if __name__ == '__main__':
    Main()
