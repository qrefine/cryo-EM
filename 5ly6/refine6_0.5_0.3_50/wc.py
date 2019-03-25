from libtbx import easy_run
for i in range(67):
  command="wc -l ./ase/%d/%d_capping/xtb_tmp.xyz"%(i,i)
  print command
  easy_run.call(command)
