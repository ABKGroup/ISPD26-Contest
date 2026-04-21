# ISPD26 Contest: Post-Placement Buffering and Sizing

<div align="center">

**Organizing Team:** UCSD, Fudan University, POSTECH  

**Co-Chairs**  
Dr. Yiting Liu, UCSD ABKGroup [yil375@ucsd.edu]  
Prof. Zhiang Wang, Fudan University [zhiangwang@fudan.edu.cn]  

</div>

## Table of Contents
- Contest description: [ISPD26_contest_description.pdf](./ISPD26_contest_description.pdf)
- [Benchmarks](https://vlsicad.ucsd.edu/ISPD26-Contest/ispd26.html): Public and hidden benchmarks.
- [Platform/ASAP7](./Platform/ASAP7): Technology platform files and libraries for the ASAP7 PDK.
- [Evaluation scripts](./scripts): Evaluation scripts for [aes_cipher_top](./scripts/aes_cipher_top/eval.sh), [jpeg_encoder](./scripts/jpeg_encoder/eval.sh), [ariane](./scripts/ariane/eval.sh) and [bsg_chip](./scripts/bsg_chip/eval.sh). 
- [Equivalence check](./equiv_check): Scripts for validating equivalence between pre-optimization and post-optimization netlists for ASAP7 designs.
- [Docker containers and submission formatting](./docker): Dockerfile and commands required to maintain a consistent evaluation and submission environment can be found at the [`README`](./docker/README.md).

## Timeline
- Registration Open: Oct 1, 2025
- Release the first set of benchmarks, evaluation scripts and Docker image: Oct. 1, 2025
- Release the second set of benchmarks (with placement blockages): Nov. 9, 2025
- Registration Close: Nov 30, 2025
- Release one large-scale testcase: Dec. 1, 2025
- Release one large-scale testcase with placement blockages; all public benchmarks are available: Dec. 3, 2025
- Alpha Submission Deadline: Jan 12, 2026
- Beta Submission Deadline: Feb, 2, 2026
- Final Submission Deadline: Mar, 7, 2026 (Anywhere on earth, and it is a hard deadline)
- Results Announcement: March 18, 2026


## Contact
Email: ispd26contest@gmail.com

## Registration
<!-- - Please fill in this [online registration form](https://forms.gle/w2bDxrAENhFzw862A)-->
- Registration has closed.
- Registration window: Oct.1, 2025 - Nov 30, 2025
- We confirm that we’ve received the registration forms from the following teams. If we overlooked your registration or any related information, please feel free to email us.

| ID | Team Name | Affiliation |
|----------|-------------|---------|
| 1   | Horiguchi Takahiro        | Unknown |
| 2   | XidianU         | Xidian University|
| 3   | Marvin         | Indian Institute of Technology Madras|
| 4   | IITM Placement Cell         |Indian Institute of Technology, Madras |
| 5   | GT         | georgia tech|
| 6   | PKU         | Peking University|
| 7   | m0654         | Yuan Ze University|
| 8   | nvBuffplace         | NVIDIA|
| 9   | HKUST-GZ         |The Hong Kong University of Science and Technology (Guangzhou) |
| 10   | arg_duck         | Independent|
| 11   | Placed and Confused         | Chair of Design Automation, Technical University of Munich (TUM)|
| 12   | ChipFat         |Vellore Institute of Technology |
| 13   | UCLA_Placer         |UCLA |
| 14   | IRISLab         | Graduate Institute of Electronics Engineering, National Taiwan University|
| 15   | timing-booster         | Texas A&M University|
| 16   | lololol         |Department of Electrical Engineering,National Taiwan University of Science and Technology |s
| 17   | ECOS-OPT           | Institute of Computing Technology, Chinese Academy of Sciences|
| 18   | have a try         | Sun Yat-Sen University|
| 19   | poSTer         | southeast university|
| 20   | Anti_Chaos       |Southeast University |
| 21   | Wild at heart          | National Yang Ming Chiao Tung University|
| 22   | BFS        | Yuan Ze University|
| 23   | Encoding         | National Yang Ming Chiao Tung University |
| 24   | ECOS-OPT         | Institute of Computing Technology, Chinese Academy of Sciences |
| 25   | NYCUVDALAB        | Institute of Electronics, National Yang Ming Chiao Tung Unniversity |
| 26   | The Phoenix Gate Guardians      | The Chinese University of Hong Kong |
| 27   | \\(^(oo)^)/      | National Tsing Hua University, The Chinese University of Hong Kong |
| 28   | Masters of Chatgpt      | Yuan Ze University |
| 29   | HLFC      | National Tsing Hua University |
| 30   | ECO      | Independent |
| 31   | PTSD      | National Tsing Hua University |
| 32   | TCLAB      | National Tsing Hua University  |
| 33   | IRISLab      | Graduate Institute of Electronics Engineering National Taiwan University |
| 34   | warp_speed      | Indian Institute of Technology Madras |
| 35   | XORcists      | Faculty of Engineering, University of Peradeniya |
| 36   | EDAnh      | National Taiwan University of Science and Technology |

<!-- ## Alpha Submission
| Rank | Total Score | Notes     | 
|----------|-------------|-------------|
| Rank1  | 1279.97      |     | 
| OpenROAD RSZ   | 1107.55  | [script](./scripts/evaluation_baseline.tcl)      | 
| Rank2   | 1106.29      |      | 
| Rank3   | 588.85      |      | 
| pre_opt   | 0      | `contest.def` without any optimization  | 

## Beta Submission
| Rank | Total Score | Notes     | 
|----------|-------------|-------------|
| Rank1  | 1309.12      |     | 
| Rank2   | 1185.65      |      | 
| Rank3   | 1109.22      |      | 
| OpenROAD RSZ   | 1107.55  | [script](./scripts/evaluation_baseline.tcl)      | 
| pre_opt   | 0      | `contest.def` without any optimization  |  -->

## Leaderboard - Final Submission

**Next year, we will use more rigorous evaluations (e.g., only on hidden testcases) and explicit policies to reinforce the spirit of the competition**

### Overall leaderboard
| Rank | Team | Total Score | Notes     | 
|----------|-------------|-------------|-------------|
|1 | Team33  | 1438.06      |     | 
|2 | Team31   | 1314.93      |      | 
|3 | Team29   | 1301.32      |      | 
| |OpenROAD RSZ   | 1107.55  | [script](./scripts/evaluation_baseline.tcl)      | 
| |pre_opt   | 0      | `contest.def` without any optimization  | 

#### 1st Place (Team 33)

| Design Name | TNS (ps) | Dynamic Power (mW) | Leakage Power (mW) | Cap Over Sum | Slew Over Sum | Fanout Over Sum | Max GR Overflow | Total GR Overflow | Tool Runtime | Flow Runtime | Avg Disp (dbu) | Design Score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| aes_cipher_top    | -44.42      | 51.69      | 0.0078 | 0      | 0          | 0 | 0 | 0 | 340.64   | 8.5     | 0.37 | **123.17** |
| aes_cipher_top_v2 | -43.69      | 131.99     | 0.0061 | 0      | 0          | 0 | 0 | 0 | 378.90   | 6.0     | 0.42 | **120.48** |
| ariane            | -6,377.76   | 137.21     | 4.79   | 15.13  | 2,187.73   | 0 | 0 | 0 | 1,581.67 | 80.5    | 0.51 | **94.33**  |
| ariane_v2         | -4,277.14   | 137.19     | 4.81   | 11.39  | 328.72     | 3 | 0 | 0 | 1,240.62 | 50.5    | 0.49 | **88.39**  |
| bsg_chip          | -44,875.21  | 747.20     | 28.80  | 98.01  | 40,659.66  | 0 | 0 | 0 | 4,580.50 | 1,035.0 | 0.62 | **88.55**  |
| bsg_chip_v2       | -18,877.64  | 1,491.40   | 28.60  | 179.51 | 47,134.73  | 0 | 0 | 0 | 6,346.50 | 557.0   | 0.59 | **93.06**  |
| jpeg_encoder      | -488.89     | 93.60      | 0.0047 | 0      | 0          | 0 | 0 | 0 | 774.46   | 9.5     | 0.28 | **145.62** |
| jpeg_encoder_v2   | -474.07     | 117.00     | 0.0040 | 0.04   | 14.43      | 0 | 0 | 0 | 746.44   | 10.0    | 0.42 | **138.14** |
| ariane_h1         | -4,368.32   | 148.18     | 4.82   | 8.66   | 1,340.43   | 0 | 0 | 0 | 1,598.64 | 69.0    | 0.50 | **75.08**  |
| ariane_h2         | -3,271.86   | 157.14     | 4.86   | 6.61   | 993.40     | 0 | 0 | 0 | 1,722.51 | 76.5    | 0.66 | **73.45**  |
| bsg_chip_h1       | -21,542.37  | 727.40     | 28.60  | 106.67 | 39,769.80  | 0 | 0 | 0 | 4,405.50 | 511.5   | 0.65 | **77.62**  |
| bsg_chip_h2       | -21,505.02  | 789.40     | 28.60  | 76.44  | 33,502.37  | 0 | 0 | 0 | 4,466.00 | 1,075.5 | 0.58 | **82.86**  |


#### 2nd Place (Team 31)
| Design Name | TNS | Dynamic Power (mW) | Leakage Power (mW) | Cap Over Sum | Slew Over Sum | Fanout Over Sum | Max GR Overflow | Total GR Overflow | Tool Runtime | Flow Runtime | Avg Disp (dbu) | Design Score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| aes_cipher_top    | -62.90      | 62.39      | 0.0128 | 0     | 0       | 0 | 0 | 0 | 19.38    | 8.0     | 0.01 | **113.71** |
| aes_cipher_top_v2 | -52.11      | 242.99     | 0.0137 | 0     | 0.29    | 0 | 0 | 0 | 57.12    | 6.0     | 0.16 | **99.02**  |
| ariane            | -18,493.99  | 140.19     | 4.81   | 0     | 46.74   | 0 | 0 | 0 | 1,279.69 | 78.0    | 0.02 | **95.94**  |
| ariane_v2         | -22,177.20  | 140.15     | 4.85   | 0.02  | 0.08    | 4 | 0 | 0 | 1,523.53 | 61.0    | 0.03 | **81.09**  |
| bsg_chip          | -116,298.92 | 760.80     | 29.20  | 0     | 408.07  | 0 | 0 | 0 | 2,259.31 | 1,082.5 | 0.02 | **80.12**  |
| bsg_chip_v2       | -85,359.99  | 1,720.10   | 29.90  | 0.02  | 477.97  | 0 | 0 | 0 | 1,744.01 | 555.5   | 0.03 | **83.27**  |
| jpeg_encoder      | -862.06     | 100.99     | 0.0129 | 0     | 0       | 0 | 0 | 0 | 153.05   | 10.5    | 0.04 | **142.89** |
| jpeg_encoder_v2   | -1,154.62   | 148.99     | 0.0050 | 0     | 0       | 0 | 0 | 0 | 32.98    | 10.0    | 0.04 | **132.03** |
| ariane_h1         | -10,840.31  | 152.11     | 4.89   | 0     | 107.15  | 0 | 0 | 0 | 470.74   | 62.0    | 0.02 | **68.98**  |
| ariane_h2         | -12,004.41  | 158.13     | 4.87   | 0     | 83.93   | 0 | 0 | 0 | 837.54   | 78.5    | 0.02 | **49.98**  |
| bsg_chip_h1       | -67,533.41  | 742.90     | 29.10  | 0.09  | 849.62  | 0 | 0 | 0 | 2,150.27 | 485.5   | 0.02 | **73.14**  |
| bsg_chip_h2       | -75,461.08  | 799.80     | 29.20  | 0     | 590.33  | 0 | 0 | 0 | 2,152.70 | 849.0   | 0.02 | **78.20**  |

#### 3rd Place (Team 29)
| Design Name | TNS | Dynamic Power (mW) | Leakage Power (mW) | Cap Over Sum | Slew Over Sum | Fanout Over Sum | Max GR Overflow | Total GR Overflow | Tool Runtime | Flow Runtime | Avg Disp (dbu) | Design Score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| aes_cipher_top    | -66.69      | 60.89      | 0.0125 | 0     | 2.86    | 0 | 0 | 0 | 24.56    | 8.5     | 0.00 | **113.58** |
| aes_cipher_top_v2 | -41.27      | 239.98     | 0.0162 | 0.02  | 0       | 0 | 0 | 0 | 132.10   | 6.0     | 0.14 | **105.49** |
| ariane            | -18,254.21  | 140.20     | 4.80   | 0     | 46.91   | 0 | 0 | 0 | 1,313.73 | 75.5    | 0.02 | **96.04**  |
| ariane_v2         | -15,890.82  | 140.07     | 4.93   | 0     | 0       | 4 | 0 | 0 | 2,579.78 | 50.5    | 0.03 | **82.92**  |
| bsg_chip          | -120,350.04 | 759.70     | 29.30  | 0.01  | 671.09  | 0 | 0 | 0 | 4,384.53 | 1,714.0 | 0.02 | **78.41**  |
| bsg_chip_v2       | -48,214.92  | 1,730.00   | 30.00  | 0.08  | 484.40  | 0 | 0 | 0 | 3,983.74 | 669.5   | 0.03 | **86.36**  |
| jpeg_encoder      | -1,207.15   | 99.99      | 0.0050 | 0     | 0       | 0 | 0 | 0 | 102.94   | 9.5     | 0.03 | **143.08** |
| jpeg_encoder_v2   | -1,730.19   | 147.00     | 0.0050 | 0     | 0.82    | 0 | 0 | 0 | 66.95    | 10.0    | 0.03 | **129.77** |
| ariane_h1         | -13,434.62  | 151.19     | 4.81   | 0     | 68.01   | 0 | 0 | 0 | 1,098.28 | 61.0    | 0.02 | **65.01**  |
| ariane_h2         | -16,344.31  | 157.18     | 4.82   | 0     | 113.05  | 0 | 0 | 0 | 968.35   | 70.5    | 0.03 | **35.93**  |
| bsg_chip_h1       | -67,533.41  | 742.90     | 29.10  | 0.09  | 849.62  | 0 | 0 | 0 | 2,384.47 | 488.5   | 0.02 | **73.06**  |
| bsg_chip_h2       | -75,461.08  | 799.80     | 29.20  | 0     | 590.33  | 0 | 0 | 0 | 2,198.18 | 1,220.0 | 0.02 | **77.85**  |


### Leaderboard per design
| Design | Top Team | Note|
|----------|-------------|-------------|
|aes|Team33| |
|aes_v2|Team33||
|ariane|Team27||
|ariane_v2|Team33||
|bsg_chip|Team33||
|bsg_chip_v2|Team33||
|jpeg|Team33||
|jpeg_v2|Team33||
|ariane_h1|Team6| hidden testcase|
|ariane_h2|Team33| hidden testcase|
|bsg_chip_h1|Team6| hidden testcase|
|bsg_chip_h2|Team6| hidden testcase|




## Contest Prizes
- First, second and third place winning teams will receive prizes consisting of cash and/or NVIDIA GPUs, with a total value of prizes at least USD $5000. Thanks to NVIDIA for their sponsorship of the ISPD26 contest prizes!

## Organizers
- Andrew B. Kahng, Sayak Kundu, Yiting Liu, and Davit Markarian from UCSD
- Zhiang Wang from Fudan University
- Seokhyeong Kang and Seonghyeon Park from POSTECH

## Sponsors
- Purdue University and the NSF [Chipshub](https://nanohub.org/groups/chipshub/): compute resources for teams and submission evaluation
- NVIDIA: prizes for winning teams

## Support
Feel free to **open a GitHub issue** if you have any questions.