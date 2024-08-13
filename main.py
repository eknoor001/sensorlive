from sensor.exception import SensorException
import sys
import os

def test_exception():
    try:
       a=1/1
    except Exception as e:
        raise SensorException(e, sys)
    


#prevent execution or import
if __name__ == "__main__":
    try:
       test_exception()
    except Exception as e:
       print(e)