import numpy as np
class box(object):
  def __init__(self):
    return
  def setedges(self,edges):
    self.ndim = len(edges)
    bottomedge = [0] * self.ndim
    self.box = np.array([bottomedge,edges])
    self.boxlength = np.array(edges)
    self.half_boxlength = self.boxlength/2.0
    self.area = 1.0
    for idim in range(self.ndim):
      self.area *= (self.box[1,idim]-self.box[0,idim])
