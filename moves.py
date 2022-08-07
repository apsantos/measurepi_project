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
	
	Variables you may use
    --------------------
	self.R2 : the radius squared (float)
	self.box.half_boxlength : half the box length
	 x_center = self.box.half_boxlength[0]
	 y_center = self.box.half_boxlength[1]
	x = ipos[0]
	y = ipos[1]

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
    movetype = 0
    if movetype == 0:
      ipos = self.insert()
    is_incircle = self.incircle(ipos)

    # update the self.naccept, self.nattempt, pos and ex
    if is_incircle:
      self.naccept[movetype] += 1
      ex[i] = 1
    else:
      ex[i] = 2
    self.nattempt[movetype] += 1

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
    rand.uniform(min,max) : gives a number from min to max
    rand.uniform(self.box.box[0,0],self.box.box[1,0]) : random number from 0 to 1 for x
	ipos[0] : x position
	ipos[1] : y position
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
