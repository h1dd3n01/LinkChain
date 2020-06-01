import json
import graphviz


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

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        d = {'data': {v['found']: v for v in spider.link_set}.values()}
        with open('data3.json', 'a+') as f:
            f.write(json.dumps(list(d['data'])))
            f.close()
        for i in d['data']:
            head = i['original']
            tail = i['found']
            self.graph.edge(head, tail)
        self.graph.view()
