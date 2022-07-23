class inputs(object):
  def __init__(self):
    self.nmoves = 108 # initial N for muVT
    self.nsample = 1
    self.nmovesequil = 10
    self.fname = 'mc'
    self.boxlength = [1., 1.]
    self.ndim = len(self.boxlength)
    self.R = 0.5
    self.make_movie = True

  def readcommandline(self,parser):
    if parser.parse_args().N != 'read':
      self.nmoves = int(parser.parse_args().N)
    if parser.parse_args().outfile != 'read':
      self.fname = parser.parse_args().outfile

