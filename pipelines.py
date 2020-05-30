import graphviz
import random


class LinkextractorPipeline:

    def __init__(self):
        self.graph = graphviz.Digraph()
        self.counter = 0
        self.set = []
        for _ in self.graph:
            self.counter += 1

    def process_item(self, item, spider):
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        if len(self.set) == 0:
            self.set.append(item)
        else:
            for i in self.set:
                if next(iter(i.values())) != next(iter(item.values())):
                    self.set.append(item)
                else:
                    last_item = list(item.values())[-1]
                    if list(i.values())[-1] != last_item:
                        rand_int = random.randrange(0, 100)
                        i['additional{}'.format(rand_int)] = last_item
        return item

    def close_spider(self, spider):
        elems = [i.replace('digraph {', ' ').replace('}', ' ').replace('\t', '') for i in self.graph]
        elems = [i.split('->')[-1] for i in elems]
        print('1')
        for i in self.set:
            print(i)
            el1 = next(iter(i.values()))
            print(el1)
            if self.counter <= 2:
                print('2.2')
                self.graph.node(el1)
                for j in list(i.values())[1:]:
                    print(j)
                    print('2.3')
                    self.graph.edge(el1, str(j).split('//')[1])
            print('3')
            for j in elems:
                print('4')
                if el1 == j:
                    print('4.1')
                    for k in list(i.values())[1:]:
                        print('4.2')
                        self.graph.edge(el1, k)
                    break
        print('5')
        self.graph.engine ='circo'
        self.graph.render('test-output', view=True)
