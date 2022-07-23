import numpy as np
import matplotlib.pyplot as plt
class tally(object):
  def __init__(self,filename='mc'):
    self.file = open(filename + '.data', 'w')
    self.file.write("# step ratio\n")
    self.step = []
    self.ratio = []
    self.nsamp = 0

  def average(self):
    self.ratio = np.array(self.ratio)
    self.ratioave = np.mean(self.ratio)
    self.ratiostd = np.std(self.ratio)

  def update(self, istep, iratio):
    self.nsamp += 1
    self.step.append(istep)
    self.ratio.append(iratio)
    self.file.write('%d %f\n' % (istep, iratio))
    
  def pltseries(self):
    """
    Plot function[s]
    """
    plt.plot(self.step, self.ratio)
    plt.xlabel('step')
    plt.ylabel('ratio')
    plt.show()

  def outputave(self, fname='mc'):
    ofile = open(fname + '.ave', 'w')
    ofile.write("# ratio, stds\n")
    ofile.write('%f %f\n' % (self.ratioave, self.ratiostd))
