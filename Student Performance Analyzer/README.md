# NumPy Student Performance Analyzer

A beginner-level data analysis project built with **Python and NumPy** to practice numerical computing, multidimensional arrays, data filtering, statistical analysis, random data generation, and basic data relationships.

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

- Finding top-performing students
- Finding lowest-performing students
- Calculating overall performance
- Identifying the best and worst-performing subjects
- Finding students who failed
- Filtering students based on average performance
- Calculating subject-wise standard deviation
- Exploring relationships between subjects
- Using correlation with NumPy

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
- Aggregation
- Statistical analysis
- Random data generation
- Sorting and ranking
- Correlation analysis
- Basic ML-style data analysis

## Future Phases

The next stages will focus on more advanced NumPy concepts:

- Matrix operations
- Linear algebra
- Vectorized computations
- Distance and similarity calculations
- Linear Regression from scratch
- Machine Learning algorithms using NumPy

## Project Status

**Completed:** Phase 1, Phase 2, Phase 3, Phase 4, Phase 5, Phase 6

**Next:** Phase 7 - Advanced NumPy and Machine Learning
