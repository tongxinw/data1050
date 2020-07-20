import pandas as pds
from cmd import Cmd
from SearchEngine import SearchEngine


class SearchEngineCLI(Cmd):
    prompt = 'DATA1050> '
    intro = """Welcome to your search engine! Type help for more information.
    load FILE_PATH
    switch TF-IDF | PageRank | smart
    search keywords...
    exit
    """

    def __init__(self):
        """ Initialize Search Engine CLI """
        super().__init__()
        self.engine = None
        self.mode = 'TF-IDF'

    def do_load(self, inp):
        """ load {FILE_PATH} """
        try:
            print(f"loading {inp}...")
            self.engine = SearchEngine(inp)
            print(f"loading succeed\n")
        except Exception as e:
            print("Loading failed with ", e)

    def do_switch(self, inp):
        """ switch {TF-IDF | PageRank | smart} """
        if inp not in {'TF-IDF', 'PageRank', 'smart'}:
            print('mode must be one of {TF-IDF, PageRank, smart}\n')
        else:
            self.mode = inp
            print(f'change mode to {inp}\n')

    def do_search(self, inp):
        """ search {keywords...} """
        if self.engine is None:
            print("load a data file first\n")
        else:
            results = self.engine.search(inp, self.mode)
            if len(results) == 0:
                print("No results returned\n")
            else:
                response = pds.DataFrame(columns=['documents', 'score'], data=results).to_string()
                print(response)
                print("")

    def do_exit(self, inp):
        """ exit the program """
        print("Bye!\n")
        return True


if __name__ == '__main__':
    SearchEngineCLI().cmdloop()
