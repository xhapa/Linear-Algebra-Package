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
## Matrix with 1 row or column (Vector)
For create a vector the package have a class that inherence from ```Matrix``` that is ```Vector``` is similar to Matrix object but with other atributes. For example you can create a ```lists``` with the values of the vector.
```python
v = Vector([2, 2, 0])# row vector
```
```python
v = Vector(2, 2, 0)#WRONG
v = Vector([[2, 2, 8]])#WRONG
```
Other way to create vector from a ```Matrix``` object, that takes the first row of the matrix.
```python
v = Vector.from_matrix([[2, 2, 0]])
```
For create columns vectors is create row vector and apply ```.transposed()``` method.
```python
v = Vector([2, 2, 0]).transposed()# col vector
```
## Operations
### Addition and Subtraction
For add or sustract matrices, they should have the same dimention mxn and for do this you can use the + and - operator in ```Matrix``` object.

![alt text](https://github.com/xhapa/Linear-Algebra-Package/blob/master/img/addition.gif "Addition")

```python
m = Matrix([[0, -3, 4], [3, 0, 0], [-4, 0, 0]])
print(m+m)
print(m-m)
```
### Scalar Product
This operation multiply a real number C with a matrix, each element in the matrix is multiply for C.

![alt text](https://github.com/xhapa/Linear-Algebra-Package/blob/master/img/scalar_mult.gif "Scalar mult")

For multiply you can use ```scalar_mul()``` that recive 1 possitional argument.
```python
m = Matrix([[0, -3, 4], [3, 0, 0], [-4, 0, 0]])
m.scalar_mul(2)
```
### Transposition
Is transform a *mxn* matrix in *nxm* matrix, turning the rows anf the columns

![alt text](https://github.com/xhapa/Linear-Algebra-Package/blob/master/img/transposed.gif "Transposed")

```python
m = Matrix([[0, -3, 4], [3, 0, 0], [-4, 0, 0]])
m.transposed()
```
### Matrix multiplication and power

For operate two matrices, left one should have the same number of columns that rows of the right one 
