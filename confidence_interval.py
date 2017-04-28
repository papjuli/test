import numpy as np
import math

def confidence_interval (l, conf_level):
  arr = np.array(l)
  n = arr.size
  mean = arr.sum() / n
  deviations = np.array([(x - mean)**2 for x in l])
  st_dev_estim = math.sqrt(deviations.sum() / (n - 1))
  if (conf_level == 90):
    z = 1.645
  elif (conf_level == 95):
    z = 1.96
  elif (conf_level == 99):
    z = 2.576 
  sqrt_n = math.sqrt(n)
  return (mean - z * st_dev_estim / sqrt_n, mean + z * st_dev_estim / sqrt_n)
  


if __name__ == "__main__":
  import random
  random.seed(123)
  l = []
  for i in range(0,8999):
    l.append(random.random())
  print confidence_interval(l, 95)
  print confidence_interval(l, 90)

