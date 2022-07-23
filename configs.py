import numpy as np
import random as rand
import matplotlib.pyplot as plt

class movie(object):
  def __init__(self,box,R):
    yfactor = (box.box[1,1]-box.box[0,1])/(box.box[1,0]-box.box[0,0])
    self.box = box.box
    self.R = R

    self.figsize = (5,5*yfactor)
    npoints = 360
    self.xcir = np.zeros(npoints)
    self.ycir = np.zeros(npoints)
    for theta in range(360):
      rad = np.radians(theta)
      self.xcir[theta] = self.R * np.cos(rad) + box.half_boxlength[0]
      self.ycir[theta] = self.R * np.sin(rad) + box.half_boxlength[1]
    

  def update(self,pos,color):
    # ims is a list of lists, each row is a list of artists to draw in the
    # current frame; here we are just animating one artist, the image, in
    # each frame
    plt.subplots(figsize=self.figsize)
    im = plt.scatter(pos[:,0], pos[:,1], c=color)
    plt.plot(self.xcir, self.ycir)
    plt.xlim(self.box[:,0])
    plt.ylim(self.box[:,1])
    plt.show()

class configfile(object):
  def __init__(self,ndim, fname='config'):
    self.file = open(fname + '.xyz', 'w')
    self.ndim = ndim

  def writeframe(self,imove,pos,type, nmol):
    self.file.write('%d\nframe %d\n' % (nmol, imove))
    i = 0
    name = {0:'n', 1:'I', 2:'O'}
    while type[i] > 1:
      if self.ndim == 2:
        self.file.write('%s %f %f 0.0\n' % (name[type[i]],pos[i,0],pos[i,1]))
      elif self.ndim == 3:
        self.file.write('%s %f %f %f\n' % (name[type[i]],pos[i,0],pos[i,1],pos[i,2]))
      elif self.ndim == 1:
        self.file.write('%s %f 0.0 0.0\n' % (name[type[i]],pos[i,0]))
      i += 1
