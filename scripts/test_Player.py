import unittest 
from Player import Player

class TestPlayer(unittest.TestCase):
    def test_can_perform_list_inventory_action(self):
        p = Player("foo")
        actual_commands = p.getCommands()
        expected_command = "list inventory"
        expected_inventory = []
        self.assertTrue(expected_command in actual_commands)
        self.assertEqual(p.doCommand(expected_command), expected_inventory)

if __name__ == '__main__':
    unittest.main()
