import graphviz
import random
import json


class LinkextractorPipeline:

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
        self.set = []

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        spider.link_set = {v['found']: v for v in spider.link_set}.values()
        d = {'data': []}
        for i in spider.link_set:
            d['data'].append(i)

        with open('data.json', 'a+') as f:
            f.write(json.dumps(d))
            f.close()
        for i in d['data']:
            head = i['original']
            tail = i['found']
            self.graph.edge(head, tail)

        self.graph.view()
