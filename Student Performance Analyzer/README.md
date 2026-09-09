# NumPy Student Performance Analyzer

A data analysis project built with **Python and NumPy** to practice numerical computing, multidimensional arrays, data filtering, statistical analysis, random data generation, and linear algebra.

This project is being developed step-by-step while learning NumPy and building a foundation for data analysis and machine learning.

## Current Progress

### Phase 1: NumPy Fundamentals

- Creating NumPy arrays
- Understanding array shape
- Working with rows and columns
- Calculating totals and averages
- Using `axis` for array operations

### Phase 2: Indexing and Slicing

- Accessing individual rows and columns
- Selecting specific subjects
- Slicing multiple students
- Slicing multiple subjects

### Phase 3: Boolean Masking

- Creating boolean conditions
- Filtering NumPy arrays
- Selecting students based on marks
- Filtering data using multiple conditions

### Phase 4: Statistical Operations

- Mean
- Median
- Minimum and maximum values
- Standard deviation
- Percentiles
- Statistical operations across rows and columns

### Phase 5: Random Data Generation

- Generating datasets using NumPy
- Using `np.random`
- Generating random student marks
- Creating larger datasets
- Working with dynamically generated data

### Phase 6: ML-Style Data Analysis

- Finding top and lowest-performing students
- Calculating overall performance
- Identifying best and worst-performing subjects
- Finding students who failed
- Filtering students based on average performance
- Calculating subject-wise standard deviation
- Exploring relationships between subjects
- Using correlation with NumPy

### Phase 7: Linear Algebra

- Working with vectors
- Vector arithmetic
- Dot product
- Vector magnitude and norms
- Creating and manipulating matrices
- Matrix addition and subtraction
- Element-wise multiplication
- Matrix multiplication
- Matrix transpose
- Determinants
- Matrix inverse
- Eigenvalues and eigenvectors

## Dataset

The project initially uses student marks across five subjects:

- Python
- Mathematics
- Machine Learning
- DBMS
- Statistics

The dataset can also be generated dynamically using NumPy for larger experiments.

Example:

```python
import numpy as np

marks = np.random.randint(0, 101, size=(1000, 5))
```

This generates marks for **1,000 students across 5 subjects**.

## Technologies

- Python
- NumPy

## Learning Objectives

The main goal of this project is to develop a strong understanding of NumPy and learn how numerical data can be efficiently processed and analyzed using arrays.

The project currently covers:

- Array creation and manipulation
- Indexing and slicing
- Boolean masking
- Statistical analysis
- Random data generation
- Ranking and filtering
- Correlation analysis
- Vector operations
- Matrix operations
- Basic linear algebra

## Future Phases

The next stages will focus on applying NumPy concepts to machine learning:

- Vectorization and broadcasting
- Data normalization
- Distance and similarity calculations
- ML mathematical operations
- Linear Regression from scratch
- Gradient descent
- Machine learning algorithms using NumPy

## Project Status

**Completed:** Phase 1, Phase 2, Phase 3, Phase 4, Phase 5, Phase 6, Phase 7

**Next:** Phase 8 - Linear Algebra Project
