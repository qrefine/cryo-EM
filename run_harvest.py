from __future__ import division
import iotbx.pdb
import mmtbx.model
import math
from libtbx import group_args
import os
from libtbx.utils import null_out
from scitbx.array_family import flex
from libtbx import easy_run
from mmtbx.command_line import emringer

def get_latest(files):
  indices = []
  for f in files:
    try:
      indices.append(int(f.replace("cycle_","").replace("_refined.pdb","")))
    except KeyboardInterrupt: raise
    except: return None
  last = max(indices)
  return "cycle_%d_refined.pdb"%last
  
def show_geo(fn, prefix):
  pdb_inp = iotbx.pdb.input(file_name=fn)
  model = mmtbx.model.manager(model_input = pdb_inp, build_grm = True,
    log = null_out())
  mes = "%s %s"%(prefix,
    model.geometry_statistics(use_hydrogens=False).show_short())
  return model, mes
  
def get_z(fn):
  cmd = " ".join(["phenix.development.rama_z_score", fn])
  r = easy_run.fully_buffered(cmd).raise_if_errors()
  return round(float(r.stdout_lines[-5].split()[2].replace(",","")), 2)
  
def get_emringer(pdb_file, map_file):
  result = emringer.run(
    args=[pdb_file, map_file], out=null_out(), verbose=False)[1].score
  return result

def run():
  # Must run in cryo-EM folder!
  root = os.getcwd()
  folders = ["6i5a","3j63","5fn5_6iyc_A/c","3a5x","5ly6"]
  for folder in folders:
    folder_1 = "/".join([root, folder])
    print folder_1, "-"*(79-len(folder_1))
    if(not os.path.isdir(folder_1)):
      print "  ...does not exist, skip."
      continue
    #
    map_file = None
    for fi in os.listdir(folder_1):
      if(fi.endswith(".map") or fi.endswith(".ccp4")):
        map_file = "/".join([folder_1, fi])
    assert os.path.isfile(map_file)
    #
    start = "/".join([folder_1, "initial.pdb"])
    assert os.path.isfile(start)
    z1 = get_z(start)
    emr1 = get_emringer(start, map_file)
    model_1, mes1 = show_geo(start, prefix="     start:")
    print mes1, "z_score:", z1, "EMRinger: %4.2f"%emr1
    #
    for sub_ in os.listdir(folder_1):
      sub = "/".join([folder_1, sub_])
      if(not os.path.isdir(sub)): continue
      if "opt" in sub: continue
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
      model_2, mes2 = show_geo(refined, prefix="     final:")
      z2 = get_z(refined)
      emr2 = get_emringer(refined, map_file)
      s1 = model_1.get_sites_cart()
      s2 = model_2.get_sites_cart()
      dist = flex.sqrt((s1 - s2).dot())
      print mes2, "min/max/mean(start, final): %5.3f %5.3f %5.3f"%\
        dist.min_max_mean().as_tuple(), "z_score:", z2, "EMRinger: %4.2f"%emr2
      

if(__name__ == "__main__"):
  run()
