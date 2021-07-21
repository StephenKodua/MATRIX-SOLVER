class Matrix(object):
    def __init__(self,num_rows = 2,num_cols = 2):
        '''
            initilaizes rows, columns, and array
        ''' 
        self.num_rows = num_rows
        self.num_cols = num_cols
        
        try:
            if type(num_rows) == int and type(num_cols) == int:#check if rows and column are integers
                if num_rows >= 1 and num_cols >= 1: #checks for positivity
                    self.array = [ [ 0 for i in range(num_cols) ] for j in range(num_rows) ] #initaize zero for each row,column
                    
                    return None 
        except ValueError:
            raise ValueError("Matrix: Error, the dimensions must be positive integers!")
                
     
        
    def __str__(self):
        '''
            Returns a string representation of the matrix
        '''
        result = "" #empty string to keep reult as a string
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                
                if i== 0 and j == 0:
                    result += "[[{}".format(self.array[i][j])
            
                elif j == 0:
                    result += " [{}".format(self.array[i][j])
                    
                elif j == self.num_cols - 1 :
                    if i == self.num_rows - 1:
                        result += " {}]]".format(self.array[i][j]) 
                       
                    else:
                        result += " {}]\n".format(self.array[i][j]) 
                        
                else:
                    result += " {}".format(self.array[i][j]) 
                
        return result
                     



    def __repr__(self):
        '''
            Returns the same matrix string as __str__
        '''
        return(self.__str__())
    
      
    def __getitem__(self, iijj):
        ''' 
            Gets the values from the matrix, given indexes
        '''
       
        if type(iijj) == tuple: #checks if indexes is tuple
            for i in iijj: #iterates through indexes and checks for each index is integer
                if not type(i) == int: 
                    raise ValueError("Matrix: Error, the indices must be a positive integer or a tuple of integers!") 
                
            if 0 < iijj[0] < self.num_rows and 0 < iijj[1] < self.num_cols: #checks if indexing is positive
                return self.array[iijj[0] -1][iijj[1] - 1] 
            else:
                if 0 >= iijj[0] or 0 >= iijj[1]: #raise error if negative
                    raise IndexError("Matrix: Error, bad indexing!") 
                else:
                    raise IndexError("Matrix: Error, index out of range!") 
            
        elif type(iijj) == int: #checks if indexes is integer
            if 0 < iijj < self.num_rows : #checks if indexing is positive
                return self.array [iijj - 1] 
            else:
                if 0 > iijj:
                    raise IndexError("Matrix: Error, index out of range!") 
                else:
                    raise  IndexError("Matrix: Error, index out of range!") 
                    
        
        else:
            raise ValueError("Matrix: Error, the indices must be a positive integer or a tuple of integers!") 
                    
                                         
    
    def __setitem__(self, iijj, value):
        '''
            Set the values from the matrix, given indexes and value
        ''' 
        if type(value) != int: #checks if value is integer
            if type(value) != float: #checks if value is integer
                raise ValueError("Matrix: Error, You can only assign a float or int to a matrix!") 
                
        if type(iijj) == tuple:#checks indexes is tuple
            for i in iijj: #loops through tuple and check if all values are int
                if type(i) != int:
                    raise ValueError("Matrix: Error, the indices must be a tuple of integers!") 
            if 0 < iijj[0] <= self.num_rows and 0 < iijj[1] <= self.num_cols: #checks if indexing is positive
                self.array[iijj[0] - 1][iijj[1] - 1 ] = value #sets value 
                
            else:
                if 0 >= iijj[0] or 0 >= iijj[1]:
                    raise IndexError("Matrix: Error, bad indexing!") 
                else:
                    raise IndexError("Matrix: Error, index out of range!")
        else:
            raise ValueError("Matrix: Error, the indices must be a tuple of integers!") 
            
                
                    
             
    
    def __add__(self, B):
        '''
            performs a matrix addition 
        ''' 
        
        if B:
            if type(B) != Matrix: #checks if matrix
                raise ValueError("Matrix: Error, you can only add a matrix to another matrix!") 
            
            if not (self.num_cols == B.num_cols and self.num_rows == B.num_rows ) :#checks same dimension
                raise ValueError("Matrix: Error, matrices dimensions must agree in addition!") 
               
            else: 
                D = Matrix(self.num_rows,self.num_cols) #creates a new matrix
                for i in range(self.num_rows): #loops through rows
                    for j in range(B.num_cols): #oops through columns
                        D.array[i][j] = self.array[i][j] + B.array[i][j] #adds values and equate to new matrix
                        
            return D
        else:
             raise ValueError("Matrix: Error, you can only add a matrix to another matrix!")
            


    def dot_product(self,L1,L2):
        '''
            Returns the dot product of two given lists of numbers
        ''' 
        dot_product = 0 #to add multiplacation value
        if not len(L1) == len(L2): #checks for same length
            raise ValueError("Dot Product: must be same length") 
        else:
            for iijj in range(len(L1)): 
                dot_product += ( L1[iijj] * L2[iijj] ) #multiply values of lists
            return dot_product

        
    def __mul__(self,B):
        '''
            Performs multiplication of two matrices, using dot product function
        ''' 
        if not type(B) == Matrix:  #checks if matrix
            raise ValueError("Matrix: Error, you can only multiply a matrix to another matrix!")  
        if not self.num_cols == B.num_rows : #checks dimension
            raise ValueError("Matrix: Error, matrices dimensions must agree in multiplication!")
        else:
            C = Matrix(self.num_rows , B.num_cols) #creates a new matrix
            for i in range(C.num_rows):
                for j in range(C.num_cols):
                    j_list = [] #to append values from j
                    for i_s in B.array: #loops through B_rows 
                        j_list.append(i_s[j]) #appends values from j 
                    C.array[i][j] = Matrix.dot_product(self, self.array[i], j_list) #set value in matrix to dot_product of i and j
                    
        return C
                    
    def transpose(self):
        '''
             Returns the transpose of the matrix
        ''' 
        T = Matrix(self.num_cols, self.num_rows)  #creates a new matrix

        for i in range(T.num_rows): #loops through rows
            for j in range(T.num_cols):#loops through colums
                T[i + 1, j+ 1] = self.array[j][i] #switches rows and colums to transpose, equate to new matrix
        
        return T
        
        
    def __eq__(self,B):
        '''
            Checks if corresponding values of matrices are equal , returns boolean 
        '''
        if B:
            if type(B) != Matrix: #checks if matrix B is a matrix
                return False
            
            if not (self.num_cols == B.num_cols and self.num_rows == B.num_rows ) : #checks equal dimension
                return False
               
            else:  
                for i in range(self.num_rows): #loops through rows
                    for j in range(B.num_cols): #loops through rows
                        if i == j : #check if values are equal
                            continue 
                return True
    
        else:
             return False
            


    
    def __rmul__(self,num):
        '''
            Performs a scalar multiplication , given integer
        '''
        R = Matrix(self.num_rows, self.num_cols) #creates a new matrix
        
        if type(num) != int: #checks for num validity
            raise ValueError("Matrix Error: scaler must be an int." ) 
        else:
            for i in range(0, self.num_rows ): 
                for j in range(0 , self.num_cols):
                
                    R.array[i][j] = self.array[i][j] * num #gets value and makes multiplication

            

        return R
    

        
