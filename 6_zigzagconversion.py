'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows,
giving: "PAHNAPLSIIGYIR"

string convert(string text, int nRows)

'''

string= "PAYPALISHIRING"
numrows= 3

class Sol(object):
    def zig(self, string, numrows):
        '''

        :param string: str
        :param numrows:int
        :return: str
        '''
        # add each character to the array in a zigzag pattern

        if numrows < 2:
            return string

        else:
            rows= ["" for i in range(numrows)] # makes a list with numrows number of "", will be joining to these
            i, right= -1, True
            for char in string:
                if right:
                    i = i+1
                else:
                    i= i-1
                rows[i] += char
                right = False if i==numrows - 1 else True if i==0 else right
        return "".join(rows)


sol= Sol()
print sol.zig(string, numrows)