#388: finding the longest (number of characters) absolute path to a file within our file system.
# Time complexity required: O(n) where n is the size of the input string

directory1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
directory2= "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

def LongestPath(directory):
    max_len= 0
    path_len={0:0}

    for line in directory.splitlines(): # split along new line
        name= line.strip("\t") # get rid of tab
        depth= len(line) - len(name) # tab takes into account the number of tabs
        if "." in name:
            max_len= max(max_len, path_len[depth] + len(name))
        else:
            path_len[depth + 1] = path_len[depth] + len(name) + 1

    return max_len



class Sol2(object):
    def longest(self, directory):
        maxlen= 0
        path= []

        for line in directory.split('\n'): # split along newline
            path[line.count('\t'):]= [line.strip('\t')] # at the Tth position, add the line stripped of tab
                                                     # Note: this means the elements of path list will change as depth changes
                                                    # need to add square brackets around [line.strip()] otherwise the string will be converted to a list as an extend()
            if '.' in line: # update maxlen if line is a filename
                maxlen=  max(maxlen, sum(map(len, path))+len(path)-1 ) # the "len(path) - 1" considers the number of brackets that should be in the directory string but were removed
                                                                        # i.e. one bracket per level of depth
        return maxlen


sol= Sol2()
print sol.longest(directory1)
print sol.longest(directory2)
