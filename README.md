# Linear-Algebra-Package
## Multidimensional array (Matrix)
A matrix is table of numbers, expressions and other data, arranged with index or coordinates, the size corresponds to the dimension and it's *m* rows and *n* columns, matrices have defined differents operations between them.

![alt text](https://github.com/xhapa/Linear-Algebra-Package/blob/master/img/matrix.gif "Matrix definition")

* A matrix with same number of columns that rows is a square matrix.
* A matriz with 1 row and n columns is a row vector for n dimension.
* A matrix with 1 column and m rows is a column vector for m dimension.

For create a matrix this package have a class called ```Matrix``` that use the list objects to define them, and have two ways to create matrices.
For example you can create nested ```lists``` objects, that represent de number of rows and append the elements for each row and that number of elements is the number of columns.
```python
m = Matrix([[1, 2, 3], [4, 5, 6], [6, 7, 8]])
```
It class take 1 positional argument that is the nested list.
```python
m = Matrix([1, 2, 3], [4, 5, 6], [6, 7, 8])#WRONG
m = Matrix(1,2,3,4,5,6,7,8)#WRONG
```
Other way to create a matrix is from her values, it method use n arguments for matrix elements and 2 positional arguments that should be the number of rows and the number of columns.
```python
m = Matrix.from_values(1, 2, 3, 4, 5, 6, dim_m=2, dim_n=3)
```

![alt text](https://github.com/xhapa/Linear-Algebra-Package/blob/master/img/addition.gif "Addition")

![alt text](https://github.com/xhapa/Linear-Algebra-Package/blob/master/img/scalar_mult.gif "Scalar mult")
