import pandas

data={
    'id':[1,2,3,4,5,6],
    'name':['bharti','karina','vandana','krupa','princy','shivansh'],
    'city':['rajkot','surat','sardhar','haripar','s.nagar','haripar']
}

dt=pandas.DataFrame(data)
print(dt)