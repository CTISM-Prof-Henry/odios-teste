import pandas as pd
import sys


def tarefa_01(path):
    try:
        df = pd.read_csv(path)
        print('Consegui ler a tabela (mas isso não quer dizer que ela está completa...)')
        return df
    except:
        print('Não consegui ler a tabela! =(', file=sys.stderr)
        return None


if __name__ == '__main__':
    tarefa_01('odio.csv')
