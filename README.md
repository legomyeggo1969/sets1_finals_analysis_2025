# SUMMARY
This analysis definitively shows there is a ticket discrepancy in the EnR -vs- OC match which negatively affected EnR.  We show this by parsing the logs and account for every ticket loss. We first show that the tool functions correctly to count tickets by showing that every other round for which we have data (five other rounds) there were **zero tickets unaccounted for**. Then we show that there are **between 101 - 107 tickets lost from EnR which are unaccounted-for** based on available data.

Low tickets situations cause teams to make very different decisions and play very differently. There is no explanation for why EnR tickets are lower than can be substantiated with any data. If EnR had the tickets which cannot be accounted for, then EnR would have made different in-game decisions.


### What caused these unexplained ticket losses?
We're not sure. But we know it happened... and here is a video from the match showing instances of it happening: [https://www.youtube.com/watch?v=OWYA8Cv1N7M](https://www.youtube.com/watch?v=OWYA8Cv1N7M)

[![Examples of unexplained ticket losses](https://img.youtube.com/vi/OWYA8Cv1N7M/0.jpg)](https://www.youtube.com/watch?v=OWYA8Cv1N7M)


### Independent Verification
We provide all data and all scripts used in this analysis and invite any independent party to inspect and verify our work. Because these server logs include player identifying information, we will keep the raw data private to be shared only with tournament-designated personnel, and are available on request. The full results are being publically published.


# Analysis
## Analysis: Proving correctness of the tool
We apply the tool to the logs from five other rounds:
- Two rounds from the 82-OWLS match on July 13
- Two rounds from the EnR-82 scrim on July 12
- One round from the 82-OC scrim on July 9

Please note that the tournament mod was updated the morning of July 12. Therefore we can prove the correctness of the tool across versions of the mod. We compare the output of the tool to the in-game screens. We also apply the tool to one round of an OC-82 scrim from July 9, which notably was on a prior version of the mod. Everything matches **exactly**. Therefore we have great confidence that the tool is counting tickets accurately.

### Tool Correctness 1 of 3: OC-82team Scrim played on July 9
Only round 2 logs were made available. Note that this scrim was played on a prior version of the mod from what was used in the OC-EnR match. The tool produced the **exact same** ticket outcomes that were shown in-game by parsing the logs and accounting for the known limitations in the tool (described in the section below "Accounting for Known Limitations"). Therefore we have great confidence that the tool is counting tickets accurately.

![Round 2](https://raw.githubusercontent.com/legomyeggo1969/sets1_finals_analysis_2025/refs/heads/main/output/OC_v_82_-_Round_2___oc%3D198___82team%3D0.png)
![Round 2 - Ingame Timeline](https://media.discordapp.net/attachments/1394089497305677875/1394332044166823987/20250710005106_1.jpg?ex=68766c68&is=68751ae8&hm=1d819990273a91bf844cc561a4bede906279c779cd1246dbf4d41e6a3d2e7e3b&=&format=webp&width=1654&height=930)
![Round 2 - Ingame - Details](https://media.discordapp.net/attachments/1394089497305677875/1394332044561223772/20250710005107_1.jpg?ex=68766c68&is=68751ae8&hm=3bfa9038b9c3af5d6464a4b41a3af1c5033ee2313f032dc663e328be085c69e1&=&format=webp&width=1654&height=930)
![Round 2 - Ingame - Scoreboard](https://media.discordapp.net/attachments/1394089497305677875/1394332042828845176/20250710005055_1.jpg?ex=68766c68&is=68751ae8&hm=bb1d2470aa1aa1ec0ff9cbe798e981b7461c51326c95474408923f4185c4ebfc&=&format=webp&width=1654&height=930)

### Tool Correctness 2 of 3: 82-OWLS Match Rounds 1 and 2
The tool produced the **exact same** ticket outcomes that were shown in-game by parsing the logs and accounting for the known limitations in the tool (described in the section below "Accounting for Known Limitations"). Therefore we have great confidence that the tool is counting tickets accurately.
![Round 1](https://raw.githubusercontent.com/legomyeggo1969/sets1_finals_analysis_2025/refs/heads/main/output/82_v_OWLS_-_Round_1___82team%3D198___owls%3D0.png)
![Round 1 - Ingame](https://media.discordapp.net/attachments/1393966496966770748/1393968143218774116/image.png?ex=68751980&is=6873c800&hm=457fc369fe5956a934b8803921cdc5343087f44b61620d68d8f4b70b1d20630b&=&format=webp&quality=lossless&width=1669&height=906)
![Round 1 - Ingame Timeline](https://media.discordapp.net/attachments/1393966496966770748/1393968145827500193/image.png?ex=68751980&is=6873c800&hm=b1506b6bd03cde2495e6b9d325bebdff68c00418049dc58a6bdf6043fe7a4ba0&=&format=webp&quality=lossless&width=1669&height=952)

![Round 2](https://raw.githubusercontent.com/legomyeggo1969/sets1_finals_analysis_2025/refs/heads/main/output/82_v_OWLS_-_Round_2___82team%3D169___owls%3D0.png)
![Round 2 - Ingame](https://media.discordapp.net/attachments/1393966496966770748/1393978306327609524/image.png?ex=687522f7&is=6873d177&hm=38d61fca9c0d28c0f558286a28f137c983723616bc19e04d22c35933b5d2cfa7&=&format=webp&quality=lossless&width=1669&height=934)
![Round 2 - Ingame Timeline](https://media.discordapp.net/attachments/1393966496966770748/1393978309133467669/image.png?ex=687522f7&is=6873d177&hm=3c11f57c49a380ded3da07c4a021cf66a67cc09085a843e2fc54f4679cc82048&=&format=webp&quality=lossless&width=1669&height=949)

### Tool Correctness 3 of 3: EnR-82team Scrim played on July 12 Rounds 1 and 2
The tool produced the **exact same** ticket outcomes that were shown in-game by parsing the logs and accounting for the known limitations in the tool (described in the section below "Accounting for Known Limitations"). Therefore we have great confidence that the tool is counting tickets accurately.

![Round 1](https://raw.githubusercontent.com/legomyeggo1969/sets1_finals_analysis_2025/refs/heads/main/output/EnR_v_82_-_Round_1___enr%3D-2___82team%3D94.png)
![Round 1 - Ingame Timeline](https://media.discordapp.net/attachments/1264242708239618180/1393684532171116574/Screenshot_1010.png?ex=68760b9d&is=6874ba1d&hm=51f35d51574f268ee60bc3ef9810b4b5cd9bb1ccdacde28d7ecfe013abf31d0d&=&format=webp&quality=lossless&width=1669&height=939)
![Round 1 - Ingame Details](https://media.discordapp.net/attachments/1264242708239618180/1393684531659280465/Screenshot_1011.png?ex=68760b9d&is=6874ba1d&hm=1d85e2235975f6ced65a672e77611d04e31cbbdd6fca904f727e31944e952658&=&format=webp&quality=lossless&width=1669&height=939)
![Round 1 - Ingame](https://media.discordapp.net/attachments/1264242708239618180/1393684534851145788/Screenshot_1004.png?ex=68760b9e&is=6874ba1e&hm=096d288e215fb6c4524cc87f04763a51339a08d3ad1333fbc55929df2279caed&=&format=webp&quality=lossless&width=1669&height=939)

![Round 2](https://raw.githubusercontent.com/legomyeggo1969/sets1_finals_analysis_2025/refs/heads/main/output/EnR_v_82_-_Round_2___enr%3D48___82team%3D0.png)
![Round 2 - Ingame Timeline](https://media.discordapp.net/attachments/1264242708239618180/1393684675553263829/Screenshot_1015.png?ex=68760bc0&is=6874ba40&hm=e87e7e10709fc99d56c96c2ca10e4a1ea977cbe314e501031cc846c22f46b297&=&format=webp&quality=lossless&width=1669&height=939)
![Round 2 - Ingame Details](https://media.discordapp.net/attachments/1264242708239618180/1393684675045888092/Screenshot_1016.png?ex=68760bbf&is=6874ba3f&hm=119983b2b1375b00316ad5834a2fa38b46d7052d00353fcfa528be5eebfb9bbf&=&format=webp&quality=lossless&width=1669&height=939)
![Round 2 - Ingame](https://media.discordapp.net/attachments/1264242708239618180/1393684677864329256/Screenshot_1005.png?ex=68760bc0&is=6874ba40&hm=fa43a2ba1e0cda3cd31ea16c33e1bcac2cd400049e1b9ed05504fa208d58e401&=&format=webp&quality=lossless&width=1669&height=939)


## Analysis: EnR-OC Match Round 1
In-game scoreboard showed the match resulted in 0(EnR) to 73(OC).

(1) Based on server logs, the match should have resulted in approximately 45-73. The shape of the graph produced by the tool matches the ingame "Tickets over Time" except for the missing tickets.

(2) The "Details" page shows 290 infantry tickets lost, however the "Scoreboard" page show 239 infantry deaths, when you account for commander deaths this leaves 49 unexplained tickets in the "Details - Infantry Losses" metric.

**Therefore, there is a loss of between 45 and 49 tickets which cannot be accounted for.**

![Round 1](https://github.com/legomyeggo1969/sets1_finals_analysis_2025/blob/main/output/EnR_v_OC_-_Round_1___enr=45___oc=73.png?raw=true)
![Round 1 - Ingame](https://media.discordapp.net/attachments/1264242708239618180/1394045908542292038/2025-07-13_20-02-51.mkv_snapshot_49.20.809.png?ex=687561ec&is=6874106c&hm=d480a27db1eabf06d4f1138fa9f8abadf258a6fa08c0867c2282a05a335fe05c&=&format=webp&quality=lossless&width=1669&height=939)
![Round 1 - Ingame Timeline](https://media.discordapp.net/attachments/1264242708239618180/1394045908143968417/2025-07-13_20-02-51.mkv_snapshot_49.22.479.png?ex=687561ec&is=6874106c&hm=551893b8ffec05e6f1aff3616f063ac69a5f2df13980f007640f7abf0b973fd3&=&format=webp&quality=lossless&width=1669&height=939)
![Round 1 - Ingame Scoreboard](https://media.discordapp.net/attachments/1264242708239618180/1394045906105401505/2025-07-13_20-02-51.mkv_snapshot_49.47.150.png?ex=687561ec&is=6874106c&hm=6ffb0a56227f973f95ac8bfcc299004a8c1c24ffb42dcb207932ccee26b9e231&=&format=webp&quality=lossless&width=1753&height=986)
![Round 1 - Ingame Details](https://media.discordapp.net/attachments/1264242708239618180/1394045907745505563/2025-07-13_20-02-51.mkv_snapshot_49.26.029.png?ex=687561ec&is=6874106c&hm=197ad0b731e8e69052e56d028631fe0d9cc0247ab9088b92295e14a8fc6fc0ea&=&format=webp&quality=lossless&width=1669&height=939)

Raw summary from the tool showing how logs break down ticket losses for both sides:
```
- enr Infantry=-245
- enr Cap=60
- enr Vehicle=-20
- oc Vehicle=-15
- oc Infantry=-157
- oc Cap=30
- oc Bleed=-35
```

## Analysis: EnR-OC Match Round 2
In-game scoreboard showed the match resulted in 0(EnR) to 77(OC)

(1) Based on server logs, the match should have resulted in approximately 56-73. The shape of the graph produced by the tool matches the ingame "Tickets over Time" except for the missing tickets.

(2) The "Details" page shows 280 infantry tickets lost, however the "Scoreboard" page show 192 infantry deaths, and the logs show 204. There were no commander deaths. This leaves 88 unexplained tickets in the "Details - Infantry Losses" metric.
It is possible that 30 tickets could be explained by the missing "flag flip ticket loss" (FFTL) which did not show up in the "Details" page. So if we conservatively assume the FFTL was accounted for under "Details - Infantry Losses" this still leaves 58 tickets unaccounted for.

**Therefore, there is a loss of between 56 and 58 tickets which cannot be accounted for.**

![Round 2](https://github.com/legomyeggo1969/sets1_finals_analysis_2025/blob/main/output/EnR_v_OC_-_Round_2___enr=56___oc=73.png?raw=true)
![Round 2 - Ingame](https://media.discordapp.net/attachments/1264242708239618180/1394046734732230677/2025-07-13_20-59-02.mkv_snapshot_48.41.286.png?ex=687562b1&is=68741131&hm=6ccc04a4cb5851d0c8b2e2fa4214eecd5f2a85976d6de3bfeecd42f000104b1c&=&format=webp&quality=lossless&width=1669&height=939)
![Round 2 - Ingame Timeline](https://media.discordapp.net/attachments/1264242708239618180/1394046732085755984/2025-07-13_20-59-02.mkv_snapshot_49.00.018.png?ex=687562b1&is=68741131&hm=acdb377feda7c67a8a1a16075682d1b8b0067c8a28827ea403737365df0c6e5d&=&format=webp&quality=lossless&width=1669&height=939)
![Round 2 - Ingame Scoreboard](https://media.discordapp.net/attachments/1264242708239618180/1394046732676890654/2025-07-13_20-59-02.mkv_snapshot_48.57.468.png?ex=687562b1&is=68741131&hm=2620b21fea8ea331f3463a2e8ca38f0b748b18df2ff71ba56fe41574bba12105&=&format=webp&quality=lossless&width=1753&height=986)
![Round 2 - Ingame Details](https://media.discordapp.net/attachments/1264242708239618180/1394046731519262851/2025-07-13_20-59-02.mkv_snapshot_49.03.352.png?ex=687562b0&is=68741130&hm=2736a908478692cfbf9d3fed934f70644d947b631c71c07effb3ea84b616be1e&=&format=webp&quality=lossless&width=1669&height=939)

Raw summary from the tool showing how logs break down ticket losses for both sides:
```
- enr Infantry=-196
- enr Cap=30
- enr Vehicle=-25
- enr Bleed=-3
- oc Vehicle=-25
- oc Infantry=-210
- oc Cap=90
- oc Bleed=-32
```

# Methodology and Content
## Content Description
### The contents of this public data package includes the follow files:

This file is the script which is used to process the log, summarize results, and visualize results
- main.py (written in python, requires 'matplotlib' as a dependency for visualization)

These files capture the output produced by running the main script:
- output/82_v_OWLS_-_Round_1___82team=198___owls=0.png
- output/82_v_OWLS_-_Round_2___82team=169___owls=0.png
- output/EnR_v_OC_-_Round_1___enr=45___oc=73.png
- output/EnR_v_OC_-_Round_2___enr=56___oc=73.png
- output/EnR_v_82_-_Round_1___enr=-2___82team=94.png
- output/EnR_v_82_-_Round_2___enr=48___82team=0.png
- output/OC_v_82_-_Round_2___oc=198___82team=0.png
- output/script_output.txt

### The contents of the private data package includes the following files.
These two files are the raw server logs from NA1 (82 vs OWLS) and EU2 (EnR vs OC)
- data/SquadGame_82OWLS.log
- data/SquadGame_ENROC.log

These two files are the raw server logs from the EnR EU Scrim Server (EnR vs 82 scrim)
- data/SquadGame-backup-2025.07.12-19.06.20.log
- data/SquadGame-backup-2025.07.13-15.00.10.log

This file are the raw server logs from the OC vs 82 scrim
- data/logs 2 OC vs 82 09.07 r2.txt

These data files are excerpts from the raw server logs downsampled to *only* the relevant rounds
- data/82owls_r1.log
- data/82owls_r2.log
- data/enroc_r1.log
- data/enroc_r2.log
- data/enr82_r1.log
- data/enr82_r2.log
- data/oc82_r2.log


## Accounting for Known Limitations
All manual adjustments are captured in the main script in the "main()" function unless otherwise noted.

(1) Sometimes vehicle losses are not automatically captured by this tool.

We mitigate this issue by comparing total ticket losses due to vehicles on the "Details" in-game screen to the summaries provided by this tool. When there is a difference, we inspected the Stream (https://www.twitch.tv/videos/2511367947) to find the times at which vehicles were lost. 

The result of this mitigation is that **all** vehicle losses exactly match what is shown in the "Details" in-game screen.


(2) Radio losses are not automatically captured by this tool.

We mitigate this issue by manually recording the times of radio losses. The result of this mitigation is that **all** radio losses exactly match what is shown in the "Details" in-game screen.

(3) Flag Points are not automatically captured by this tool.

We mitigate this issue by manually recording times of initial-flag-captures, bleed start, bleed end (upon mid-cap neutral), and flag flip gains & losses. The result of this mitigation is that **all** tickets changes due to flags are correctly accounted for.

In the course of implementing this mitigation, we recognized that the "Details" screen does not account for ticket losses due to flag flips. As a result, EnR-OC Round 2 does not exactly match what is shown in the "Details" screen, and we believe this is correct and the Details screen is wrong for EnR (+30, +30, -30).

(4) Commander infantry losses must be accounted as 2 tickets (not 1). The tool does not automatically identify the commander.

We mitigate this issue by manually recording who the commander was, and when that player dies they count as 2 tickets. We believe this mitigates the issue.

(5) Teamkills are not automatically captured by this tool.

When a teamkill occurs, a ticket is not lost when a player gives up. The tool does not detect team kills and therefore infantry losses may be slightly high relative to truth. We believe the extra work to account for the very few teamkills which occured is not necessary to highlight the primary issue found in this report.

(6) The tool does not automatically detect which team a player is on.

To mitigate this, we parse player names and assign them to a team based on their name. This logic is implemented in the the function "infer_side_from_player_name"
