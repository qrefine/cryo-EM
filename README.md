# cryo-EM
## 3a5x (7194 atoms)
method         | bond   | angle |clash   |rama_out| rama_favor|rotamer | EMRinger |CC_mask
:--:           | :--:   | :--:  |   :--: |   :--: |   :--:    |:--:    |:--:      |:--:
initial        | 0.013  | 1.530 | 117.79 |   2.85 |   86.59   | 8.72   |   0.80   |0.292
cctbx_refine   | 0.002  | 1.14  |  3.9   |   0.41 |   92.28   |  2.56  |  -0.08 |0.3091
xtb_refine     | 0.010  | 1.73  |  3.3   |   0.61 |   94.31   |  3.33  |   0.40   |0.3311
terachem_refine| 0.010  | 1.47  |  0.14  |   0    |   96.75   |  5.13  | 0.89     |0.3001
## 3j63_chain_A (1436 atoms)
method         | bond   | angle | clash |rama_out| rama_favor|rotamer | EMRinger |CC_mask
:--:           | :--:   | :--:  | :--:  |  :--:  |   :--:    |:--:    |:--:      |:--:
initial        | 0.004  | 1.007 | 50.84 |  4.49  |   85.39   | 5.48   | 2.36     |0.6747
cctbx_refine   | 0.002  | 0.749 | 3.48  |  0     |   98.88   | 4.11   | 1.17     |0.6553
xtb_refine     | 0.012  | 1.705 | 3.48  |  0     |   94.38   | 4.11   | 1.83     |0.6546
terachem_refine| 0.013  | 1.535 |0.70   |  0     |   100.00  | 1.37   | 1.17     |0.6386
## 5fn5_chain_c(3787 atoms)
method         | bond   | angle |clash  |rama_out| rama_favor|rotamer | EMRinger |CC_mask
:--:           | :--:   | :--:  |  :--: | :--:   |   :--:    |:--:    |:--:      |:--:
initial        | 0.012  | 2.001 | 14.27 | 2.07   |   90.87   | 18.13  |   0.79 |0.6430
cctbx_refine   | 0.003  | 1.19  | 5.81  | 0.83   |   92.53   | 8.29   |   -0.10|0.6645
xtb_refine     | 0.01   | 1.55  | 2.64  | 0.83   |   90.87   |  9.33  |   0.79 |0.6573
terachem_refine| 0.012  | 1.741 | 0     |  0     |   95.85   | 7.77   |   0.79 |0.6648
# 5ly6(7399 atoms)
method         | bond   | angle | clash |rama_out| rama_favor|rotamer | EMRinger  |CC_mask
:--:           | :--:   | :--:  |  :--: |  :--:  |   :--:    |:--:    |:--:     |:--:
initial        | 0.005  | 0.942 | 92.04 |   4.9  |   74.2    | 36.08  |  0.49 |0.6239
cctbx_refine   | 0.002  | 0.66  |  4.87 |   3.62 |   79.10   |  3.39  |  1.05 |0.6441
xtb_refine     | 0.011  | 1.86  |  1.8  |   2.13 |   87.21   |  7.75  |  0.93 |0.6623
terachem_refine| 0.012  | 1.61  |  1.08 |   2.1  |   89.98   |  11.14 |  0.93 |0.6394
### 6i5a(2396 atoms)
method         | bond   | angle |clash |rama_out | rama_favor|rotamer | EMRinger|CC_mask
:--:           | :--:   | :--:  | :--: |   :--:  |   :--:    |:--:    |:--:      |:--:
initial        | 0.012  | 1.840 | 6.69 |   1.32  |  97.35    |  0.74  |    3.94  |0.8156 
cctbx_refine   | 0.002  | 0.570 | 1.67 |   1.32  |  95.36    |  0.00  |    3.73  |0.8118
xtb_refine     | 0.011  | 1.590 | 2.09 |   1.32  |  94.70    |  0.74  |    3.57  |0.8066
terachem_refine| 0.010  | 1.407 | 0.84 |   1.32  |  98.68    |  0.00  |    3.99  |0.8106
## command used
0. if ligand included, phenix.pdbtool keep="protein" *.pdb
1. phenix.map_box mask_atoms=true soft_mask=true keep_origin=false keep_input_unit_cell_and_grid=false *.pdb *.map
2. qr.finalise *.pdb
