from __future__ import division
import iotbx.pdb
import mmtbx.model
import math
from libtbx import group_args
import os
from libtbx.utils import null_out

def get_latest(files):
  indices = []
  for f in files:
    try:
      indices.append(int(f.replace("cycle_","").replace("_refined.pdb","")))
    except KeyboardInterrupt: raise
    except: return None
  last = max(indices)
  return "cycle_%d_refined.pdb"%last

def run():
  # Must run in cryo-EM folder!
  root = os.getcwd()
  folders = ["6i5a","3j63","5fn5_6iyc_A","3a5x","5ly6",   "3j06","5xsy","3los"]
  for folder in folders:
    folder_1 = "/".join([root, folder])
    print folder_1, "-"*(79-len(folder_1))
    if(not os.path.isdir(folder_1)):
      print "  ...does not exist, skip."
      continue
    for sub_ in os.listdir(folder_1):
      sub = "/".join([folder_1, sub_])
      if(not os.path.isdir(sub)): continue
      refined = "/".join([sub,"real_space_refined.pdb"])
      msg=""
      if(not os.path.isfile(refined)):
        msg="<<< WARNING: no final refined model."
      print "  ", sub_, msg
      sub1 = "/".join([sub, "pdb"])
      if(not os.path.isdir(sub1)):
        print "         not there:", sub1 
        continue
      files = []
      for fn in os.listdir(sub1):
        if(not fn.endswith(".pdb")): continue
        files.append(fn)
      refined = get_latest(files = files)
      if(refined is None):
        print "     No refined model."
        continue
      refined = "/".join([sub1, refined])
      assert os.path.isfile(refined)
      #
      pdb_inp = iotbx.pdb.input(file_name=refined)
      model = mmtbx.model.manager(model_input = pdb_inp, build_grm = True,
        log = null_out())
      print "      ", os.path.basename(refined), \
        model.geometry_statistics(use_hydrogens=False).show_short()

if(__name__ == "__main__"):
  run()
