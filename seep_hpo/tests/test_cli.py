from click.testing import CliRunner
import unittest
import os
from seep_hpo.main import cli


class CliTest(unittest.TestCase):

    def test_version_cli(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['version'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Version not configured yet.", result.output)

    def test_resolver_cli(self):
        runner = CliRunner()
        test_annotaion_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'test_annotation_file.tsv')
        test_query_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                           'test_query.tsv')
        result = runner.invoke(cli, ['resolve', test_annotaion_file, test_query_file])
        self.assertIn("HP:0011042", result.output)
        self.assertIn("HP:0003362", result.output)
