# from main import cmdcd, cmdexit, cmdrev, cmdclear
import unittest
from zipfile import ZipFile, Path as zipPath

class TestMethods(unittest.TestCase):
    f = ZipFile("home.zip", 'r')
    zipRoot = zipPath(f).joinpath("home")
    unittest.main()

    def test_ls(self):
        files = []
        for file_name in self.zipRoot.iterdir():
            files.append(file_name.name)
        self.assertEqual(files, ["programs", "test", "test1"])

    def test_clear(self):
        var = cmdclear([])
        self.assertTrue(var)

    def test_cd(self):
        cmdcd("test")
        self.assertTrue(self.zipRoot.exists())
        cmdcd("..")
        self.assertTrue(self.zipRoot.name == "home")

    def test_rev(self):
        self.assertEqual(cmdrev(["-t", "1234"]), "4321")

    def test_exit(self):
        cmdexit([])
        self.assertRaises(SystemExit)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)