---
theme: gaia
class: invert
paginate: true
backgroundColor: #000
marp: true
style: |
  img[alt~=bottom-center] {
    display: block;
    margin: 0 auto;
    padding-top: 350px;
  }

  .center {
    display: block;
    margin: 0;
    padding: 0;
    text-align: center;
  }

  .columns-2 {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .columns-2-33 {
    display: grid;
    grid-template-columns: 1.2fr 1fr;
  }
---

![bg fit](images/ai-logo.png)

---

<!--_class: lead invert-->

# **Team Introductions**
<!-- 
Presenter: SUMMER MARKLEY
Highlights: How we can we came about our name and logo 
Estimated Time:  2 mins
-->
![bg](https://user-images.githubusercontent.com/103965932/173463669-ca46743c-5b2a-48e2-83e3-78382bce2354.jpg )
![bg](https://user-images.githubusercontent.com/103965932/173463695-2bdd4dec-b4ab-4ae0-a6ab-4aaba77087fd.jpg)
![bg](https://user-images.githubusercontent.com/103965932/173463684-ea7c6dce-e8c5-417d-a7fb-a3c6d73f6c95.jpg)
![bg](https://user-images.githubusercontent.com/103965932/173463689-25b9b672-4118-4b31-a673-3906d5aeee7e.jpg)
![bg](https://user-images.githubusercontent.com/103965932/173463646-0134093e-9cfc-4dac-9c1c-6599bea7033e.jpg)
![bg](https://user-images.githubusercontent.com/103965932/173463651-7cc6143d-df45-4be4-b42d-08031d79e58d.jpg)

![bottom-center w:1150px](https://user-images.githubusercontent.com/103965932/173463700-8cc56e77-270e-4c06-83e8-24b946b18c2a.png)

---

# **The Brainstorming Process**
<!-- 
Presenter:        JONNY LE
Highlights:       Discuss how we as a team stepped through our initial ideas and formulated our final solution
Estimated Time:   2 mins
-->
Project ideas:
- AI analysis of PRTG Alerts
- AI analysis of Opsgenie
- AI analysis of time spent trends
- AI analysis of difficulty of customers

<!--
- buzzword/interest in AI
- find its application in all tools and workflows
-->

---
<!-- 
Presenter:        GABRIELLE WOODS
Highlights:       See Gab's index cards
Estimated Time:   5 mins
-->
# **The Problem**
Automated alerts are handled by a group of new, L1 engineers.
The sheer scale of alerting topics is daunting and too much to learn or research as applicable.

A series of seemingly disjointed alerts create a correlation in the mind of a Sr. engineer, but are easy to overlook for a newer engineer.

Example: An alert about a UPS on battery backup comes in. An hour later the site goes offline. A Sr. engineer will identify a likely power failure, but a new L1 engineer does not necessarily note the correlation.

![bg opacity:.3](https://img.huffingtonpost.com/asset/5b9d1023240000300094edab.jpeg?ops=scalefit_720_noupscale)

---
<!-- 
Presenter:        GABRIELLE WOODS
Highlights:       See Gab's index cards
Estimated Time:   5 mins
-->
# **Our Solution (Version 1.0)**

Add AI behind identifying and correlating alerts to crunch data and identify correlations.
- Reduce L1 burden
- Reduce manual training 
- Expedite escalation of important events
- Bridge the gap between teams

![bg left:33% fit](https://w7.pngwing.com/pngs/182/517/png-transparent-ted-eureka-university-college-of-engineering-osmania-university-student-education-organizing-miscellaneous-text-logo.png)

---

# **Step 1 - Engage the Project Manager!**
<!-- 
Presenter: SUMMER MARKLEY
Highlights: Discuss how we built our initial project plan and the use of our SmartSheet portal
Estimated Time:  5 mins
-->

<div class="center">

![w:1000px](images/project-manager-board.png)

</div>

---

# **The Journey to the Solution**
<!-- 
Presenter: RAK 
Highlights: What did we build and how did we build it
Estimated Time:  5 mins
-->
![w:350px](https://mermaid.ink/img/pako:eNo10MlqwzAQBuBXGebkQEKgRx8KtRVyLW1uVQ-DNHYEWoyWQBLy7pWX6iIx-mb4pSeqoBlbHCNNV7gI6aGujx_Bkw1340f4_Lqcf-FweIeu6SNTZiAP5OgR6qZUKD7v1rZuYX3TFWP1rFi9gfEpk1e8mX4xYjXH5dLaowp-MGOJDFPM40bFQk_NmgUSxxvHBDmAWnMk9inUSg0yt21ih3t0HB0ZXR_2nGdJzFd2LLGtR80DFZslSv-qtEy6zjppk0PEdiCbeI9Ucvi-e4VtjoX_kTBU_8lt6vUHgXBoJw) ![w: 350px](https://mermaid.ink/img/pako:eNo9kLFqw0AMhl9FaHIgeQEPhcTuUOiWbnUG4ZMvB-fTIcsFE_Luvdh1NQnp-z-QHtiLY6zRK-U7fLVdglLn75ZzlCUkD5_i4cr6w3qD0-kNLtW2A4JpHcMgCr3EyL29AlH8BIdNdFkjTfWRJqMYwSsvZQ-Ucww9WZC0o82KtlUjaQh-Vv6HTXb95h5URshqHg54xJF1pODKDY-XqEO788gd1qV1PNAcrcMuPQs6Z0fG7y6YKNYDxYmPSLPJdUk91qYz71AbqLxk_KOevydBYuY) ![w:350px](https://mermaid.ink/img/pako:eNpdkE1rwzAMhv-K0CmF9rJjDoO1yWC3wXKrd9BiJTW15eAPRij97_OSlMF0kngfPVi-Ye81Y41joOkCXaMESr2cG56sn42M0LFEHwbrv-ETDodnOFZrCCTA_RPkrywpl0lDyAJ50pQ4AuxW13FZOlVvEhNZC-nPN1F_pbGw_3fNAMKsWT8kp0XSVO-5GKwfIwzBO4hzLMPGNAvTVl0gI-DKXXZL2iV5rTqOaQtwj46DI6PL8bdfTGG6sGOFdWk1D5RtUqjkXtD1Xa02yQesB7KR90g5-Y9ZeqxTyPyAGkPlL91G3X8AU6xygA)

--- 

# **Wait...This Does Not Work**
<!-- 
Presenter: JONNY LE 
Highlights: How did this fail
Estimated Time:  5 mins
-->
<div class="columns-2">
<div>

Deploying an AI solution that can work off prtg message data is harder to setup than originally thought. 

* Noisy syslog messages
* Not enough **useful** data
* Noisy results

</div>
<div>

![w:420px](images/mess.jpg)

</div>
</div>

<!--
- unparsed syslog messages
- trouble filtering useful data
- not enough data
- garbage in, garbage out
-->

---

<div class="center">

![w:300px](images/bad-input.png)![w:750px](images/bad-input-2.png)
![h:230px](images/bad-data.png)![h:300px](images/noisy-data.png)

</div>

<!--
- top-left: unaggregatable data
- top-right: noisy syslog message, emphasize repeated words
- bottom-left: bad data
- bottom-right: noisy results
-->

---
<!-- 
Presenter: GROUP
Highlights: skit
Estimated Time:  5 mins
-->

# **Time for Reflection**

![](https://mermaid.ink/img/pako:eNptz7FOAzEMANBfsTyebkHAkgVRFaQuDKVSlyxW4uNMLwny-YRK1X8n7dF2wVPsPMv2AUOJjA4BPsukmfc-Qw0TGxhgTkYOJiXDRhJDVxTW3A1zbQan2PZkYD3Da9M0Tw7uHGyYEjyvbmZBYQdWzmxBo4TR1er9P3IrP6TxPNHBwxW0l4-1hB5u_I2_YSk67-Tg8dqALSbWRBLrjYdTg8c6PbFHV5-RdOfR52N101ck45coVhRdR8PILdJk5X2fAzrTiS9oKfShlP7U8RdCFGNz)

---
<!-- 
Presenter: JONNY LE 
Highlights: differences from version 1
Estimated Time:  2 mins
-->
# **Our Solution (Version 2.0)** 

"Instead of using AI, we became the AI"

Our new solution monitors the rate at which alerts are generated and programmatically protects our alert workflow process in the event a large spike in alerts is received.  By simplifying our approach to the overall problem of controlling massive spikes (anomolies) in our PRTG alert, we were able to quickly bring to market a working solution that not only addresses our immediate need, but allows us to build upon with future releases. 

<!--
- reiterate problem: alert spikes with no correlation
- many alerts escalated and EACH needing manual intervention
- our new solution programmatically monitors the rate of alerts and protects our alert workflow when that happens
- solves same problem, but a different, faster, more fundamental approach
-->

---

<!--
_backgroundColor: #1e1e1e
Presenter: JONNY LE 
Highlights: detailed logic flow
Estimated Time:  5 mins
-->

# **Let's Look Under the Hood**

![w:1150px](images/solution-flowchart.svg)
![w:900px](images/solution-flowchart-2.svg)

<!--
- picture two diagrams together
- As a result...
-->

---
<!-- 
Presenter: JONNY LE 
Highlights: it works!
Estimated Time: 2 mins
-->
# **Results**

<div class="columns-2-33">
<div>

![w:400px](images/prtg_test_down.png)
![w:400px](images/api-test-output.png)

</div>
<div>

 ![w:675px](images/opsgenie-test.png)

</div>
</div>

<!--
- unlike our first solution...
- reiterate working features
- mention for future demo
-->

---
<!-- 
Presenter: BOB
Highlights:
Estimated Time: 2 mins
-->
# **Future Road Map**

![w:1200px](https://mermaid.ink/img/pako:eNqFkcFqwzAMhl9F-NyMNGNs5FZIy3YolJYdBrlosZqYxlaxFcYoffcpS8MYDKaTjD79-i1dTMOWTGlaDCJ1AA1x0hNsCGWIBOvQYWjIUxDYM1qP5wmzKLTh6FEA3jSy7TarqqmWqBHHAfbUEyaC4i6fCjuM-vSUErYEPbcgDNQ774LKQWCn5SG50MLqRfkSlwso8qLI8scs13z5YCelZ04Ckd6ZJcE3eRSKgEuAG_W3lfvZyuvuAGf-GHt6ipMIlNOsJ5016szD9rsVdK7t1DHaX_y_yA9RkagXwABDwEE6jo6sflYdzKBZGE-6Umf1JJexrTbS6fJrU2pqMZ5qU4ercsN5PMDaOuFoyiP2iRZGZfnwGRpTShxohiqHbUR_o65fzZOapw)


### ROAD MAP
#### Parse message log to eliminate noise using AI
##### Host reboots
##### UPS power alerts
##### RPA high load alerts
##### Detect an unauthoried user