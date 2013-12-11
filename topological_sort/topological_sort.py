
class Node(object):
    def __init__(self, row_num, col_num, value):
        self.row_num = row_num
        self.col_num = col_num
        self.value = value
        self.topo_sequence_object = None


class TopologicalSort(object):
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.adjancent_matrix = self.__generate_matirx(n, edges)
        self.topo_sequence = None


    def topo_sort(self):
        topo_sequence_object = self.__topological_sort(self.adjancent_matrix)
        self.topo_sequence = [(node[1].col_num for node in seq) for seq in topo_sequence_object]
        return None

    def __topological_sort(self, adjancent_matrix):
        dim = len(adjancent_matrix[0])
        if dim == 1:
            return [[(0, adjancent_matrix[0][0])]]

        no_prevous_node = []
        for j in range(dim):
            found1 = False
            for i in range(dim):
                if adjancent_matrix[i][j].value == 1:
                    found1 = True
                    break
            if not found1:
                no_prevous_node.append((j, adjancent_matrix[j][j]))

        topo_sequence_object = []
        for j, node in no_prevous_node:
            for totoseq in self.__topological_sort(self.__minus_one_dim(adjancent_matrix, j)):
                topo_sequence_object.append([(j, node)] + totoseq)
        return topo_sequence_object

    def __generate_matirx(self, n, edges):
        adjancent_matrix = [[Node(i, j, 0) for i in range(n)] for j in range(n)]
        for e in edges:
            adjancent_matrix[e[0]][e[1]].value = 1
        return adjancent_matrix

    def __minus_one_dim(self, matrix, i):
        return [e[:i] + e[i+1:] for e in matrix[:i] + matrix[i+1:]]


    def topo_sequence(self):
        return [seq[1].col_num for seq in self.topo_sequence_object]

    @staticmethod
    def __print_matirx(matrix, callback=lambda x: x):
        for row in matrix:
            print [callback(node) for node in row]
        return None

    def print_raw_matrix(self):
        self.__print_matirx(self.adjancent_matrix, callback=lambda x: x.value)
        print '\n'
        return None

    def print_topo_seq(self):
        for seq in self.topo_sequence:
            print [node for node in seq]
        print '\n'
        return None

def main():
    edges = ((0, 1), (1, 3), (3, 6), (3, 2), (2, 4), (5, 4), (6, 5), (7, 5), (8, 6), (8, 7))
    topo = TopologicalSort(9, edges)
    topo.print_raw_matrix()
    topo.topo_sort()
    topo.print_topo_seq()
    return None

if __name__ == '__main__':
    main()