# cryo-EM
## 3a5x (7194 atoms)
method         | bond   | angle |clashscore |rama_outlier| rama_favor|rotamer | CC_mask
:--:           | :--:   | :--:  |   :--:    |   :--:     |   :--:    |:--:    |:--:
initial        | 0.013  | 1.530 | 117.79    |   2.85     |   86.59   | 8.72   | 0.292
cctbx_refine   | 0.001  | 0.4   |  2.36     |   0.61     |   93.50   |  2.05  | 0.3025
xtb_refine     | 0.010  | 1.70  |  2.5      |   0.81     |   93.90   |  4.36  | 0.3050
terachem_refine| 0.014  | 1.4   |  1.53     |   0        |   96.75   |  4.62  | 0.3051
## 3j63_chain_A (1436 atoms)
method         | bond   | angle |clashscore |rama_outlier| rama_favor|rotamer | CC_mask
:--:           | :--:   | :--:  |   :--:    |   :--:     |   :--:    |:--:    |:--:
initial        | 0.004  | 1.007 |   50.84   |   4.49     |   85.39   | 5.48   | 0.6747
cctbx_refine   | 0.002  | 0.749 |   3.48    |   0        |   98.88   | 4.11   | 0.6553
xtb_refine     | 0.011  | 1.67  |   3.5     |   0        |   91.01   | 4.11   | 0.6530
terachem_refine| 0.013  | 1.535 |   0.70    |   0        |   100.00  | 1.37   | 0.6386
## 5fn5_chain_c(3787 atoms)
method         | bond   | angle |clashscore |rama_outlier| rama_favor|rotamer | CC_mask
:--:           | :--:   | :--:  |   :--:    |   :--:     |   :--:    |:--:    |:--:
initial        | 0.012  | 2.001 |  14.27    |    2.07    |   90.87   | 18.13  | 0.6430
cctbx_refine   | 0.002  | 0.51  |   5.0     |    0.83    |   91.70   | 7.25   | 0.6540
xtb_refine     | 0.009  | 1.5   |    2.9    |    0.41    |   90.04   |  8.29  | 0.6555
terachem_refine| 0.013  | 1.58  |    1.8    |    0       |   96.28   | 11.92  | 0.6441
# 5ly6(7399 atoms)
method         | bond   | angle |clashscore |rama_outlier| rama_favor|rotamer | CC_mask
:--:           | :--:   | :--:  |   :--:    |   :--:     |   :--:    |:--:    |:--:
initial        | 0.005  | 0.942 |   92.04   |    4.9     |   74.2    | 36.08  | 0.6239
cctbx_refine   | 0.002  | 0.48  |    4.6    |    4.26    |  77.61    |  10.41 |  0.6564
xtb_refine     | 0.011  | 1.86  |    1.8    |    2.13    |   87.21   |  7.75  |   0.6623
terachem_refine| 0.012  | 1.61  |    1.08   |    2.13    |   89.98   |  11.14 | 0.6394
### 6i5a(2396 atoms)
method         | bond   | angle |clashscore |rama_outlier| rama_favor|rotamer | CC_mask
:--:           | :--:   | :--:  |   :--:    |   :--:     |   :--:    |:--:    |:--:
initial        | 0.012  | 1.840 |  6.69     |   1.32     |  97.35    |  0.74  | 0.8156
xtb_refine     | 0.011  | 1.590 |   2.09    |   1.32     |  94.70    |  0.74  | 0.8066
terachem_refine| 0.010  | 1.407 |   0.84    |   1.32     |  98.68    |  0.00  | 0.8106
## command used
0. if ligand included, phenix.pdbtool keep="protein" *.pdb
1. phenix.map_box mask_atoms=true soft_mask=true keep_origin=false keep_input_unit_cell_and_grid=false *.pdb *.map
2. qr.finalise *.pdb
