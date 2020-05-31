import graphviz
import json


class Test:
    def __init__(self):
        self.graph = graphviz.Digraph(engine='neato', filename='unix4.gv',
                                      format='png',
                                      node_attr={'color': 'lightblue2',
                                                 'style': 'filled'},
                                      edge_attr={'weight': '10,2'}
                                      )
        self.graph.attr(size='100')
        self.graph.attr(overlap='false')
        self.graph.attr(fontsize='150')
        # self.graph.attr(center='true')

    def go_mad(self):
        with open('data2.json', 'r+') as f:
            file = f.read()
            json_data = json.loads(file)

            for i in json_data['data']:
                head = i['original']
                tail = i['found']
                self.graph.edge(head, tail)
            # self.graph.engine = 'unix'
            # self.graph.render()
            self.graph.view()


if __name__ == '__main__':
    t = Test()
    t.go_mad()
