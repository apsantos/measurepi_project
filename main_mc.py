# python code for monte carlo simulations
import sys, argparse
import numpy as np
sys.path.append('/content/drive/MyDrive/MC')
from box import box
from configs import configfile
from configs import movie
from input import inputs
from moves import moves
from tally import tally

def run(parser):
#def run(parser=argparse.ArgumentParser()):
  inp = inputs()
  inp.readcommandline(parser)
  
  bx = box()
  bx.setedges(inp.boxlength)

  # Set up move
  mv = moves(bx,inp.R)
  
  if inp.make_movie:
    mov = movie(bx,inp.R)
  
  config = configfile(inp.ndim, inp.fname)
  io = tally(inp.fname)
  pos = np.zeros((inp.nmoves,bx.ndim))
  inout = np.zeros((inp.nmoves))
  
  for imove in range(inp.nmoves):
    mv.move(imove, pos, inout)
    if (imove % inp.nsample) == 0 and (imove > inp.nmovesequil):
      config.writeframe(imove, pos, inout,mv.nattempt[0])
      io.update(imove, mv.naccept[0]/float(mv.nattempt[0]))
  
  if inp.make_movie:
    mov.update(pos, inout)
  io.average()
  io.pltseries()
  io.outputave(inp.fname)
  mv.outputefficiency(inp.fname)

def main(argv=None):
  parser = argparse.ArgumentParser(description='Simple MC code')
  parser.add_argument("-N", type=str, default='read',
                 help='Number of insertions')
  parser.add_argument("--outfile", type=str, default='read',
                 help='output file name root')

  run(parser)

if __name__ == '__main__':
    sys.exit(main())
