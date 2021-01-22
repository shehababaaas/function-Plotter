import pytest
import numpy as np 
from function_plotter import function_plotter
func_range = np.linspace(-10,10,101)
def test():
    assert function_plotter('x',10,-10)== list(func_range)
def test_2():
    assert function_plotter('x^2',10,-10)==list((func_range)**2)
def test_3():
    with pytest.raises(ValueError):
        function_plotter('x',10,12)        
