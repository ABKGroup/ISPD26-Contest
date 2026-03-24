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
- Final Submission Deadline: Mar, 7, 2026 (Anywhere on earth, and it is a hard deadline)**
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
<!--### Overall leaderboard
| Rank | Team | Total Score | Notes     | 
|----------|-------------|-------------|-------------|
|1 | Team33  | 1438.06      |     | 
|2 | Team27   | 1347.03      |      | 
|3 | Team31   | 1315.00      |      | 
| |OpenROAD RSZ   | 1107.55  | [script](./scripts/evaluation_baseline.tcl)      | 
| |pre_opt   | 0      | `contest.def` without any optimization  | 
-->
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