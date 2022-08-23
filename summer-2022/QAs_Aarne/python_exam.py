# exam https://docs.google.com/presentation/d/1ATCJtMdHpcV1rHu9o7vZ_GmrlonB5M6JPh0HLLZ_-a4/edit#slide=id.g927cd5c6ec_0_72

# Jag bekräftar härmed att jag inte kommunicerar med andra personer än kursens lärare under tentans gång.
# Jag är medveten om att fusk i tentan kan leda till disciplinåtgärder.

# 1

prices = {
    'kaffe': 30,
    'öl': 50,
    'kola': 25
    }

    
def price(s):
    parts = s.split()
    unitprice = prices[parts[1]]
    return int(parts[0]) * unitprice


def get_order():
    order = input('Vad vill du dricka? ')
    total = price(order)
    while order != 'Det är bra så':
        order = input('Något mer? ')
        if order.split()[1] in prices:
            total = total + price(order)
        elif order != 'Det är bra så':
            print('Finns tyvärr inte')
    print('Det blir', total, 'kronor')


# 2

def edges2adjacency(edges):
    dict = {}
    for a, b in edges:
        if a in dict:
            dict[a].append(b)
        else:
            dict[a] = [b]
        if b in dict:
            dict[b].append(a)
        else:
            dict[b] = [a]
    return dict


def adjacency2edges(adj):
    edges = []
    for a in adj:
        for b in adj[a]:
            if (b, a) not in edges:
                edges.append((a, b))
    return edges


# 3

class Graph():
    def __init__(self):
        self.adj = {}  # starting with empty adjacency list 

    def neighbors(self, n):
        return self.adj[n]

    def add_node(self, a):
        self.adj[a] = []

    def add_edge(self, a, b):
        if a not in self.adj:
            self.add_node(a)
        if b not in self.adj:
            self.add_node(b)
        self.adj[a].append(b)
        self.adj[b].append(a)

    def nodes(self):
        return list(self.adj.keys())

    def edges(self):
        eds = []
        for a in self.adj:
            for b in self.adj[a]:
                if (b, a) not in eds:
                    eds.append((a, b))
        return eds



if __name__ == '__main__':
#    print(price('4 kaffe'))
#    get_order()
#    edges = [(0,1), (1,2), (2,0), (2,3)]
#    adj = edges2adjacency(edges)
#    print(adj)
#    print(adjacency2edges(adj))

    G = Graph()
    G.add_edge(0,1)
    G.add_edge(1,2)
    G.add_edge(0,2)
    G.add_edge(2,3)
    G.add_node(4)
    print(G.neighbors(2))
    print(G.neighbors(4))
    print(G.nodes())
    print(G.edges())



    



    
