import re 
import numpy as np 
import matplotlib.pyplot as plt
def function_plotter(val,max_,min_):
    the_allowed_words={'sin','cos','exp','sqrt','^','x'}
    # we will try to find string x 
    for x in re.findall('[a-zA-Z_]+', val):
        if x not in the_allowed_words:
            raise ValueError ('you can\'t use this {} Try another one'.format(x))         
    if min_ >= max_ or max_ <min_ :
        raise ValueError('Use proper max and min values')    
    func_range = np.linspace(min_,max_,101)
    s=list(func_range)    
    replacements= {
    'sin' : 'np.sin',
    'cos' : 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
}
    for old, new in replacements.items():
        val = val.replace(old, new)
    val1=val
    y=[]
    for i in range(len(s)):
        if 'exp' in val1:
            for i1 in re.findall('exp+', val1):
                val1 = val1.replace(i1, "_")
                for x in re.findall('[x]+', val1):
                    val1 = val1.replace(x, '({})'.format(str(s[i])))
                val1 = val1.replace("_", "exp")
        else:     
            for x in re.findall('[x]+', val):
                val1 = val.replace(x, '({})'.format(str(s[i])))   
        try:
            y.append(eval(val1))
        except ZeroDivisionError :
            y.append(np.nan)
            val1=val  
    return(y)        