from libtbx import easy_run
for i in range(67):
  command="wc -l ./ase/%d/%d_capping.xyz"%(i,i)
  print command
  easy_run.call(command)
