import os
from typing import List
import unittest

from lib_pay_calculator.inbound_adapter import from_base64, from_txt


class TestInboudAdapters(unittest.TestCase):

    def test_adapter_from_base64(self):
        input = "UkVORT1NTzEwOjAwLTEyOjAwLFRVMTA6MDAtMTI6MDAsVEgwMTowMC0wMzowMCxTQTE0OjAwLTE4OjAwLFNVMjA6MDAtMjE6MDAKQVNUUklEPU1PMTA6MDAtMTI6MDAsVEgxMjowMC0xNDowMCxTVTIwOjAwLTIxOjAwCkpIT049TU8xMDowMC0xMjowMCxUVTEwOjAwLTEyOjAwLFRIMDE6MDAtMDM6MDAsU0ExNDowMC0xODowMCxTVTIwOjAwLTIxOjAwCk1BUlk9TU8xMDowMC0xMjowMCxUVTEwOjAwLTEyOjAwLFRIMDE6MDAtMDM6MDAsU0ExNDowMC0xODowMCxTVTIwOjAwLTIxOjAwCk5BTkNZPU1PMTA6MDAtMTI6MDAsVFUxMDowMC0xMjowMCxUSDAxOjAwLTAzOjAwLFNBMTQ6MDAtMTg6MDAsU1UyMDowMC0yMTowMA=="
        result = from_base64(file_content=input)

        self.assertTrue( isinstance( result, List ) )
        self.assertTrue( len( result ) == 5 )

        self.assertEqual( result[0], "The amount to pay RENE is: 215.0 USD" )
        self.assertEqual( result[1], "The amount to pay ASTRID is: 85.0 USD" )

    def test_adapter_from_txt(self):
        current_path = os.path.abspath(__file__)
        current_path = current_path.replace("/functional/test_inbound_adapter.py", "")
        input = current_path + "/static/five_employees.txt"
        
        file = open(input, 'r')
        result = from_txt(file=file)
        print(result)
        self.assertTrue( isinstance( result, List ) )
        self.assertTrue( len( result ) == 5 )

        self.assertEqual( result[0], "The amount to pay RENE is: 215.0 USD" )
        self.assertEqual( result[1], "The amount to pay ASTRID is: 85.0 USD" )