import detectorlib
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import pandas as pd



"""window=16 # Window represents the sensors
det=detectorlib.detector()
det.xlsx_path="Anomalies_hierarchy_exp_distribution"
randexp=[]
for i in range (144):
    randexp.append(det.random_exp_generator(1800))
for i in range(15):
    randexp.append(det.random_big_anomalies_generation(1800)) 
randexp.append(det.random_complete_anomalies_generation(1800)) 
randexp=np.array(randexp)
det.df=randexp



possible_shapes=[
([10, 16], [1800]), 
([16], [1800, 10]),	
([10], [1800, 16]),	
]

possible_shapes_pruned=[
([9, 16], [1800]), 
([16], [1800, 9]),	
([9], [1800, 16]),	
]

possible_shapes_antipruned=[([16], [1800])]


det.create_statistical_model('PCA')
det.stamp_all_shape_anomalies(possible_shapes)

det.df=randexp
print(det.pruning(window).shape, det.df)
det.stamp_all_shape_anomalies(possible_shapes_pruned)


det.df=randexp
print(det.antipruning(window).shape)

det.stamp_all_shape_anomalies(possible_shapes_antipruned)"""


X, Y, Z = 100, 200, 300  # Dimensioni del tensore
det=detectorlib.detector()
# Aggiungi piccole anomalie
#data2 = det.introduce_anomalies(data, num_anomalies=40, scale_range=[3, 10])

# Aggiungi anomalie di scala più grande
data_infected=[]
for i in tqdm(range(3), desc='Generating tensors...'):
    decision=np.random.choice([1, 2])
    data=np.random.normal(loc=0.0, scale=1.0, size=(X, Y, Z))
    data=det.introduce_anomalies(data, num_anomalies=6, scale_range=[7, 15], index=i)
    if decision==1:
        print(f'Big anomaly at index:{i}')
        data=det.introduce_anomalies(data, num_anomalies=1, scale_range=[59, 60], index=i)
    data_infected.append(data)
    det.hitmaps(X, Y, Z, data, i)

possible_shapes=[
    ([3], [100, 200, 300]),
    ([3, 100], [200, 300]),
    ([3, 200], [100, 300]),
    ([3, 300], [200, 100])
]
det.df=np.array(data_infected)
det.create_statistical_model('PCA')
det.xlsx_path='anomalies_cubes.xlsx'
det.stamp_all_shape_anomalies(possible_shapes)