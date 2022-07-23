import numpy as np
import random as rand
class moves(object):
  def __init__(self,box,R):
    self.box = box
    self.R2 = R*R
    self.ndim = box.ndim
    self.area = box.area
    self.nmovetypes = 1
    self.nattempt = np.zeros((self.nmovetypes))
    self.naccept = np.zeros((self.nmovetypes))
    print(self.box.half_boxlength)

  def incircle(self, ipos):
    """Check if a point is in a circle

    Parameters
    ----------
    ipos : numpy array with dimensions (ndim)
        position of test particle

    Returns
    -------
    bool
        True if successful, False otherwise.
    """
    return True

  def move(self, i, pos, ex):
    """MC driver. 

    Parameters
    ----------
    pos : numpy array with dimensions (nmoves,ndim)
        position of test particle
    ex : numpy array with dimensions (nmoves)
        interger assignment with:
        0: not inserted yet
        1: inside circle
        2: outside circle

    """
    tfrac = rand.random()
    movetype = 0
    if movetype == 0:
      ipos = self.insert()
    is_incircle = self.incircle(ipos)

    # update the self.naccept, self.nattempt, pos and ex

  def insert(self):
    """Generate a point in the box

    Parameters
    ----------
    self.box.box : dimensions (2,ndim)
      bondaries on the box.
      index 1: 0 is the lower bound, 1 is the upper bound
      index 2: x or y

    Returns
    -------
    ipos : numpy array with dimensions (ndim)
        position of test particle
    """
    ipos = np.zeros((self.box.ndim))
    return ipos

  def outputefficiency(self, fname='mc'):
    movefile = open(fname + '.moves', 'w')
    movefile.write('# fa_incirlce\n')
    for imovetype in range(self.nmovetypes):    
      if self.nattempt[imovetype] > 0:
        ratio = self.naccept[imovetype]/float(self.nattempt[imovetype])
      else:
        ratio = 0
      movefile.write('%f ' % ratio)
    movefile.write('\n')
