import unittest
from unittest.mock import patch, mock_open
import src.extended_functions as ef

class TestSystemInfo(unittest.TestCase):

    @patch('socket.socket')
    def test_local_ip(self, mock_socket):
        mock_socket.return_value.getsockname.return_value = ('192.168.1.100', 0)
        self.assertEqual(ef.local_ip(), '192.168.1.100')

    @patch('requests.get')
    @patch('bs4.BeautifulSoup')
    def test_global_ip(self, mock_bs, mock_requests):
        mock_response = mock_requests.return_value
        mock_response.status_code = 200
        mock_response.text = '<div id="ip">1.2.3.4</div>'
        mock_bs.return_value.find.return_value = mock_response

        self.assertEqual(ef.global_ip(), '1.2.3.4')

    """
    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_get_cpu_temperature_valid_data(self, mock_open, mock_exists, mock_listdir):
        # Simular la lista de zonas térmicas
        mock_listdir.return_value = ['thermal_zone0', 'thermal_zone1']
        mock_exists.side_effect = [True, True, True, True]  # Ambos archivos existen

        # Configurar el mock_open y asegurar que devuelva valores apropiados
        mock_open.side_effect = [
            mock_open(read_data='thermal_zone0\n').return_value,  # Tipo de térmica
            mock_open(read_data='50000\n').return_value,  # Temperatura en mK
            mock_open(read_data='thermal_zone1\n').return_value,  # Tipo de térmica
            mock_open(read_data='50000\n').return_value  # Temperatura en mK
        ]

        expected_output = "thermal_zone0\t50.0°C\nthermal_zone1\t50.0°C"
        print(f"expected_output={expected_output}")
        output = ef.get_cpu_temperature()
        print(f"output={output}")
        self.assertEqual(output, expected_output)
    """

    @patch('os.listdir')
    @patch('os.path.exists')
    def test_get_cpu_temperature_no_data(self, mock_exists, mock_listdir):
        # Simular que no hay zonas térmicas
        mock_listdir.return_value = []
        output = ef.get_cpu_temperature()
        expected_output = "No temperature data available"
        self.assertEqual(output, expected_output)

    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_get_cpu_temperature_file_not_found(self, mock_open, mock_exists, mock_listdir):
        # Simular la lista de zonas térmicas
        mock_listdir.return_value = ['thermal_zone0']
        mock_exists.side_effect = [True, False]  # El archivo de temperatura no existe

        # Probar que no se produzca un error y que se devuelva el resultado adecuado
        expected_output = "No temperature data available"
        output = ef.get_cpu_temperature()
        self.assertEqual(output, expected_output)

    @patch('os.popen')
    def test_get_cpu_use(self, mock_popen):
        mock_popen.return_value.readline.return_value = 'CPU MHz: 2800.000'
        self.assertEqual(ef.get_cpu_use(), '2800.000')

    @patch('os.popen')
    def test_get_ram_info(self, mock_popen):
        mock_popen.return_value.readline.side_effect = [
            b'Inter:     8000000  2500000  5500000  0%   0%   0%\n',  # Unused line
            b'Mem:       8000000  2500000  5500000  0%   0%   0%\n'   # Used line
        ]
        self.assertEqual(ef.get_ram_info(), ['8000000', '2500000', '5500000'])

    @patch('os.popen')
    def test_get_disk_space(self, mock_popen):
        mock_popen.return_value.readline.side_effect = [
            b'Filesystem      Size  Used Avail Use% Mounted on\n',
            b'/dev/sda1       100G   30G   70G  30% /'  # Sample disk info
        ]
        self.assertEqual(ef.get_disk_space(), ['100G', '30G', '70G', '30%'])

    @patch('os.getenv')
    @patch('os.uname')
    def test_get_hostname(self, mock_uname, mock_getenv):
        mock_getenv.return_value = None
        mock_uname.return_value.nodename = 'test-host'

        self.assertEqual(ef.get_hostname(), 'test-host')

    @patch('src.extended_functions.get_hostname', return_value="test-host")
    @patch('src.extended_functions.get_ram_info', return_value=['8000000', '2500000', '5500000'])
    @patch('src.extended_functions.get_disk_space', return_value=['100G', '30G', '70G', '30%'])
    @patch('src.extended_functions.local_ip', return_value='192.168.1.1')
    @patch('src.extended_functions.global_ip', return_value='1.2.3.4')
    @patch('src.extended_functions.get_cpu_temperature', return_value='thermal_zone\t50.0°C')
    @patch('src.extended_functions.get_cpu_use', return_value='2800.000')
    def test_get_full_info(self, mock_hostname, mock_ram_info, mock_disk_space, mock_local_ip, mock_global_ip,
        mock__cpu_temperature, mock_cpu_use):
        expected_output = {
            "hostname": "test-host",
            "local_ip": '192.168.1.1',
            "global_ip": '1.2.3.4',
            "cpu_temp": 'thermal_zone\t50.0°C',
            "cpu_usage": '2800.000',
            "ram_total": '8000.0',
            "ram_used": '2500.0',
            "ram_free": '5500.0',
            "disk_total": '100G',
            "disk_used": '30G',
            "disk_perc": '30%',
        }
        self.assertEqual(ef.get_full_info(), expected_output)

if __name__ == '__main__':
    unittest.main()
