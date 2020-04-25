class Algorithms(object):

    def equivalenceClasses(input, output):
        line = input.readline()
        p = PartitionAsForest(int(line))
        for line in input.readlines():
            words = line.split()
            i = int(words[0])
            j = int(words[1])
            s = p.find(i)
            t = p.find(j)
            if s is not t:
                p.join(s,t)
            else:
                output.write("redundant pair: %d, %d\n" %(i,j))
        output.write(str(p)+ "\n")
    equivalenceClasses = staticmethod(equivalenceClasses)
