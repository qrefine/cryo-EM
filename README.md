# cryo-EM
## command used
0. if ligand included, phenix.pdbtool keep="protein" *.pdb
1. phenix.map_box mask_atoms=true soft_mask=true keep_origin=false keep_input_unit_cell_and_grid=false *.pdb *.map
2. qr.finalise *.pdb
