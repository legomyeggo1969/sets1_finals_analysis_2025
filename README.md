## SUMMARY
This analysis definitely shows there is a ticket discrepancy in the EnR -vs- OC match which negatively affected EnR. Meanwhile the 82 -vs- OWLS match was unaffected. We show this by parsing the logs and account for every ticket loss. We show that the logs **exactly** account for all ticket losses in the 82-vs-OWLS match, and there are between 85 - 107 tickets lost from EnR which are **unaccounted-for** based on available data.

Low tickets situations cause teams to make very different decisions and play very differently. There is no explanation for why EnR tickets are lower than can be substantiated with any data. If EnR had the tickets which cannot be accounted for, then EnR would have made different in-game decisions.

We provide all data and all scripts used in this analysis and invite any independent party to inspect and verify our work. Because these server logs include player identifying information, we will keep the raw data private to be shared only with tournament-designated personnel, and are available on request. The full results are being publically published.


## Analysis: 82-OWLS Rounds 1 and 2
The tool produced the *exact same* ticket outcomes that were shown in-game by parsing the logs and accounting for the known limitations in the tool (described in the section below "Accounting for Known Limitations"). Therefore we have great confidence that the tool is counting tickets accurately.
![Round 1](https://raw.githubusercontent.com/legomyeggo1969/sets1_finals_analysis_2025/refs/heads/main/output/82_v_OWLS_-_Round_1___82team%3D198___owls%3D0.png)
![Round 1 - Ingame](https://media.discordapp.net/attachments/1393966496966770748/1393968143218774116/image.png?ex=68751980&is=6873c800&hm=457fc369fe5956a934b8803921cdc5343087f44b61620d68d8f4b70b1d20630b&=&format=webp&quality=lossless&width=1669&height=906)
![Round 1 - Ingame Timeline](https://media.discordapp.net/attachments/1393966496966770748/1393968145827500193/image.png?ex=68751980&is=6873c800&hm=b1506b6bd03cde2495e6b9d325bebdff68c00418049dc58a6bdf6043fe7a4ba0&=&format=webp&quality=lossless&width=1669&height=952)

![Round 2](https://raw.githubusercontent.com/legomyeggo1969/sets1_finals_analysis_2025/refs/heads/main/output/82_v_OWLS_-_Round_2___82team%3D169___owls%3D0.png)
![Round 2 - Ingame](https://media.discordapp.net/attachments/1393966496966770748/1393978306327609524/image.png?ex=687522f7&is=6873d177&hm=38d61fca9c0d28c0f558286a28f137c983723616bc19e04d22c35933b5d2cfa7&=&format=webp&quality=lossless&width=1669&height=934)
![Round 2 - Ingame Timeline](https://media.discordapp.net/attachments/1393966496966770748/1393978309133467669/image.png?ex=687522f7&is=6873d177&hm=3c11f57c49a380ded3da07c4a021cf66a67cc09085a843e2fc54f4679cc82048&=&format=webp&quality=lossless&width=1669&height=949)

## Analysis: EnR-OC Round 1
In-game scoreboard showed the match resulted in 0(EnR) to 73(OC).

(1) Based on server logs, the match should have resulted in approximately 37-81. The shape of the graph produced by the tool matches the ingame "Tickets over Time" except for the missing tickets.

(2) The "Details" page shows 290 infantry tickets lost, however the "Scoreboard" page show 239 infantry deaths, when you account for commander deaths this leaves 49 unexplained tickets in the "Details - Infantry Losses" metric.

Therefore, there is a loss of between 37 and 49 tickets which cannot be accounted for.

![Round 1](https://raw.githubusercontent.com/legomyeggo1969/sets1_finals_analysis_2025/refs/heads/main/output/EnR_v_OC_-_Round_1___enr%3D37___oc%3D81.png)
![Round 1 - Ingame](https://media.discordapp.net/attachments/1264242708239618180/1394045908542292038/2025-07-13_20-02-51.mkv_snapshot_49.20.809.png?ex=687561ec&is=6874106c&hm=d480a27db1eabf06d4f1138fa9f8abadf258a6fa08c0867c2282a05a335fe05c&=&format=webp&quality=lossless&width=1669&height=939)
![Round 1 - Ingame Timeline](https://media.discordapp.net/attachments/1264242708239618180/1394045908143968417/2025-07-13_20-02-51.mkv_snapshot_49.22.479.png?ex=687561ec&is=6874106c&hm=551893b8ffec05e6f1aff3616f063ac69a5f2df13980f007640f7abf0b973fd3&=&format=webp&quality=lossless&width=1669&height=939)
[!Round 1 - Ingame Details](https://media.discordapp.net/attachments/1264242708239618180/1394045907745505563/2025-07-13_20-02-51.mkv_snapshot_49.26.029.png?ex=687561ec&is=6874106c&hm=197ad0b731e8e69052e56d028631fe0d9cc0247ab9088b92295e14a8fc6fc0ea&=&format=webp&quality=lossless&width=1669&height=939)

Raw summary from the tool showing how logs break down ticket losses for both sides:
```
- enr Infantry=-253
- enr Cap=60
- enr Vehicle=-20
- oc Vehicle=-15
- oc Infantry=-149
- oc Cap=30
- oc Bleed=-35
```

## Analysis: EnR-OC Round 2
In-game scoreboard showed the match resulted in 0(EnR) to 77(OC)

(1) Based on server logs, the match should have resulted in approximately 48-81. The shape of the graph produced by the tool matches the ingame "Tickets over Time" except for the missing tickets.

(2) The "Details" page shows 280 infantry tickets lost, however the "Scoreboard" page show 192 infantry deaths. There were no commander deaths. This leaves 88 unexplained tickets in the "Details - Infantry Losses" metric.
It is possible that 30 tickets could be explained by the missing "flag flip ticket loss" (FFTL) which did not show up in the "Details" page. So if we conservatively assume the FFTL was accounted for under "Details - Infantry Losses" this still leaves 58 tickets unaccounted for.

Therefore, there is a loss of between 48 and 58 tickets which cannot be accounted for.
![Round 1](https://raw.githubusercontent.com/legomyeggo1969/sets1_finals_analysis_2025/refs/heads/main/output/EnR_v_OC_-_Round_2___enr%3D48___oc%3D81.png)
![Round 1 - Ingame](https://media.discordapp.net/attachments/1264242708239618180/1394046734732230677/2025-07-13_20-59-02.mkv_snapshot_48.41.286.png?ex=687562b1&is=68741131&hm=6ccc04a4cb5851d0c8b2e2fa4214eecd5f2a85976d6de3bfeecd42f000104b1c&=&format=webp&quality=lossless&width=1669&height=939)
![Round 1 - Ingame Timeline](https://media.discordapp.net/attachments/1264242708239618180/1394046732085755984/2025-07-13_20-59-02.mkv_snapshot_49.00.018.png?ex=687562b1&is=68741131&hm=acdb377feda7c67a8a1a16075682d1b8b0067c8a28827ea403737365df0c6e5d&=&format=webp&quality=lossless&width=1669&height=939)
[!Round 1 - Ingame Details](https://media.discordapp.net/attachments/1264242708239618180/1394046731519262851/2025-07-13_20-59-02.mkv_snapshot_49.03.352.png?ex=687562b0&is=68741130&hm=2736a908478692cfbf9d3fed934f70644d947b631c71c07effb3ea84b616be1e&=&format=webp&quality=lossless&width=1669&height=939)

Raw summary from the tool showing how logs break down ticket losses for both sides:
```
- enr Infantry=-204
- enr Cap=30
- enr Vehicle=-25
- enr Bleed=-3
- oc Vehicle=-25
- oc Infantry=-202
- oc Cap=90
- oc Bleed=-32
```

## Content Description
# The contents of this public data package includes the follow files:

This file is the script which is used to process the log, summarize results, and visualize results
- main.py (written in python, requires 'matplotlib' as a dependency for visualization)

These files capture the output produced by running the main script:
- output/82_v_OWLS_-_Round_1___82team=198___owls=0.png
- output/82_v_OWLS_-_Round_2___82team=169___owls=0.png
- output/EnR_v_OC_-_Round_1___enr=37___oc=81.png
- output/EnR_v_OC_-_Round_2___enr=48___oc=81.png
- output/script_output.txt

# The contents of the private data package includes the following files.
These two files are the raw server logs from NA1 (82 vs OWLS) and EU2 (EnR vs OC)
- data/SquadGame_82OWLS.log
- data/SquadGame_ENROC.log

These data files are excerpts from the raw server logs downsampled to *only* the relevant rounds
- data/82owls_r1.log
- data/82owls_r2.log
- data/enroc_r1.log
- data/enroc_r2.log


## Accounting for Known Limitations
All manual adjustments are captured in the main script in the "main()" function above line ~100-ish.

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

To mitigate this, we parse player names and assign them to a team based on their name. This logic is implmented in the the function "infer_side_from_player_name"
