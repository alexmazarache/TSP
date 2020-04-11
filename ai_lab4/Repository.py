class Repository(object):
    def __init__(self):

        self._lenght=0
        self._graph=[]
        self._s= -1
        self._d= -1
        self.load_from_file()
      
        
    def load_from_file(self):
        #citeste datele din fisier
        f = open("easy_01_tsp.txt","r")
        lines = f.readlines()

        self._lenght= int(lines[0])

        for i in range(1, self.get_length() + 1):
            self._graph.append([int(j.rstrip()) for j in lines[i].split(',')])

        self._s=int(lines[self._lenght+1])
        self._d=int(lines[self._lenght+2])
        f.close()

    


    def get_graph(self):
        return self._graph

    def get_length(self):
        return self._lenght

    def get_source(self):
        return self._s

    def get_destination(self):
        return self._d