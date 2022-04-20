import unittest

import pandas as pd

from project import *
from inspect import signature
import os


class TestaTudo(unittest.TestCase):
    def test_imports(self):
        libs = ['flask', 'sqlite3', 'numpy', 'pandas', 'argparse']

        for lib in libs:
            try:
                exec('import %s' % lib)
            except ModuleNotFoundError or ImportError:
                raise ImportError(
                    'Não foi possível importar a biblioteca ' + lib + '; verifique se você está executando o Python ' +
                    'Anaconda, digite na linha de comando:\n' +
                    'conda\n' +
                    'Se uma mensagem de \"conda não é reconhecido como comando interno ou externo...\" aparecer, ' +
                    'provavelmente você precisará reinstalar o Python Anaconda,\n' +
                    'com privilégios de administrador, e marcar a opção \"Incluir Anaconda no PATH do sistema\", ' +
                    'para que este teste funcione.'
                )

    def test_tarefa_01(self):
        from project.tarefa_01 import tarefa_01

        path = os.path.join('project', 'odio.csv')

        if not os.path.exists(path):
            raise FileNotFoundError('Você deve executar o testador a partir da pasta do repositório. Do contrário, ele '
                                    'não achará o arquivo .csv! Tente pela linha de comando.')

        df = tarefa_01(path)

        self.assertIsInstance(df, pd.DataFrame, "tarefa_01 deveria retornar um pandas.DataFrame!")
        self.assertGreaterEqual(len(df), 5, "A tabela precisa ter ao menos 5 linhas!")
        self.assertGreaterEqual(
            len(pd.unique(df['integrante'])) * 5,
            len(df),
            'A tabela precisa ter pelo menos 5 contribuições por integrante!'
        )


if __name__ == '__main__':
    unittest.main()
