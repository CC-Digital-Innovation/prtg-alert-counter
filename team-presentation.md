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

![bg fit](https://user-images.githubusercontent.com/103965932/173462799-95b24a44-5926-426d-a1d2-92482b982c97.png)

---

<!--_class: lead invert-->

# **Team Introductions**

![bg](https://user-images.githubusercontent.com/103965932/173463669-ca46743c-5b2a-48e2-83e3-78382bce2354.jpg )
![bg](https://user-images.githubusercontent.com/103965932/173463695-2bdd4dec-b4ab-4ae0-a6ab-4aaba77087fd.jpg)
![bg](https://user-images.githubusercontent.com/103965932/173463684-ea7c6dce-e8c5-417d-a7fb-a3c6d73f6c95.jpg)
![bg](https://user-images.githubusercontent.com/103965932/173463689-25b9b672-4118-4b31-a673-3906d5aeee7e.jpg)
![bg](https://user-images.githubusercontent.com/103965932/173463646-0134093e-9cfc-4dac-9c1c-6599bea7033e.jpg)
![bg](https://user-images.githubusercontent.com/103965932/173463651-7cc6143d-df45-4be4-b42d-08031d79e58d.jpg)

![bottom-center w:1150px](https://user-images.githubusercontent.com/103965932/173463700-8cc56e77-270e-4c06-83e8-24b946b18c2a.png)

---

# **The Brainstorming Process**

Project ideas:
- AI analysis of difficulty of customers
- AI analysis of PRTG Alerts
- AI analysis of time spent trends


---

# **The Problem**
Automated alerts are handled by a group of new, L1 engineers.
The sheer scale of alerting topics is daunting and too much to learn or research as applicable.

A series of seemingly disjointed alerts create a correlation in the mind of a Sr. engineer, but are easy to overlook for a newer engineer.

Example: An alert about a UPS on battery backup comes in. An hour later the site goes offline. A Sr. engineer will identify a likely power failure, but a new L1 engineer does not necessarily note the correlation.

![bg opacity:.3](https://img.huffingtonpost.com/asset/5b9d1023240000300094edab.jpeg?ops=scalefit_720_noupscale)

---

# **Our Solution (Version 1.0)**

Add AI behind identifying and correlating alerts to crunch data and identify correlations.
- Reduce L1 burden
- Reduce manual training 
- Expedite escalation of important events
- Bridge the gap between teams

![bg left fit](https://w7.pngwing.com/pngs/182/517/png-transparent-ted-eureka-university-college-of-engineering-osmania-university-student-education-organizing-miscellaneous-text-logo.png)

---

# **The Journey to the Solution**

[![](https://mermaid.ink/img/pako:eNo10MlqwzAQBuBXGebkQEKgRx8KtRVyLW1uVQ-DNHYEWoyWQBLy7pWX6iIx-mb4pSeqoBlbHCNNV7gI6aGujx_Bkw1340f4_Lqcf-FweIeu6SNTZiAP5OgR6qZUKD7v1rZuYX3TFWP1rFi9gfEpk1e8mX4xYjXH5dLaowp-MGOJDFPM40bFQk_NmgUSxxvHBDmAWnMk9inUSg0yt21ih3t0HB0ZXR_2nGdJzFd2LLGtR80DFZslSv-qtEy6zjppk0PEdiCbeI9Ucvi-e4VtjoX_kTBU_8lt6vUHgXBoJw)](https://mermaid.live/edit#pako:eNo10MlqwzAQBuBXGebkQEKgRx8KtRVyLW1uVQ-DNHYEWoyWQBLy7pWX6iIx-mb4pSeqoBlbHCNNV7gI6aGujx_Bkw1340f4_Lqcf-FweIeu6SNTZiAP5OgR6qZUKD7v1rZuYX3TFWP1rFi9gfEpk1e8mX4xYjXH5dLaowp-MGOJDFPM40bFQk_NmgUSxxvHBDmAWnMk9inUSg0yt21ih3t0HB0ZXR_2nGdJzFd2LLGtR80DFZslSv-qtEy6zjppk0PEdiCbeI9Ucvi-e4VtjoX_kTBU_8lt6vUHgXBoJw)

[![](https://mermaid.ink/img/pako:eNo9kLFqw0AMhl9FaHIgeQEPhcTuUOiWbnUG4ZMvB-fTIcsFE_Luvdh1NQnp-z-QHtiLY6zRK-U7fLVdglLn75ZzlCUkD5_i4cr6w3qD0-kNLtW2A4JpHcMgCr3EyL29AlH8BIdNdFkjTfWRJqMYwSsvZQ-Ucww9WZC0o82KtlUjaQh-Vv6HTXb95h5URshqHg54xJF1pODKDY-XqEO788gd1qV1PNAcrcMuPQs6Z0fG7y6YKNYDxYmPSLPJdUk91qYz71AbqLxk_KOevydBYuY)](https://mermaid.live/edit#pako:eNo9kLFqw0AMhl9FaHIgeQEPhcTuUOiWbnUG4ZMvB-fTIcsFE_Luvdh1NQnp-z-QHtiLY6zRK-U7fLVdglLn75ZzlCUkD5_i4cr6w3qD0-kNLtW2A4JpHcMgCr3EyL29AlH8BIdNdFkjTfWRJqMYwSsvZQ-Ucww9WZC0o82KtlUjaQh-Vv6HTXb95h5URshqHg54xJF1pODKDY-XqEO788gd1qV1PNAcrcMuPQs6Z0fG7y6YKNYDxYmPSLPJdUk91qYz71AbqLxk_KOevydBYuY)

[![](https://mermaid.ink/img/pako:eNpdkE1rwzAMhv-K0CmF9rJjDoO1yWC3wXKrd9BiJTW15eAPRij97_OSlMF0kngfPVi-Ye81Y41joOkCXaMESr2cG56sn42M0LFEHwbrv-ETDodnOFZrCCTA_RPkrywpl0lDyAJ50pQ4AuxW13FZOlVvEhNZC-nPN1F_pbGw_3fNAMKsWT8kp0XSVO-5GKwfIwzBO4hzLMPGNAvTVl0gI-DKXXZL2iV5rTqOaQtwj46DI6PL8bdfTGG6sGOFdWk1D5RtUqjkXtD1Xa02yQesB7KR90g5-Y9ZeqxTyPyAGkPlL91G3X8AU6xygA)](https://mermaid.live/edit#pako:eNpdkE1rwzAMhv-K0CmF9rJjDoO1yWC3wXKrd9BiJTW15eAPRij97_OSlMF0kngfPVi-Ye81Y41joOkCXaMESr2cG56sn42M0LFEHwbrv-ETDodnOFZrCCTA_RPkrywpl0lDyAJ50pQ4AuxW13FZOlVvEhNZC-nPN1F_pbGw_3fNAMKsWT8kp0XSVO-5GKwfIwzBO4hzLMPGNAvTVl0gI-DKXXZL2iV5rTqOaQtwj46DI6PL8bdfTGG6sGOFdWk1D5RtUqjkXtD1Xa02yQesB7KR90g5-Y9ZeqxTyPyAGkPlL91G3X8AU6xygA)

--- 

# **Wait...This Does Not Work**

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

# **Time for Reflection**

---

# **Our Solution (Version 2.0)** 

---

# **Overview of Solution**

Description

---

<!--
_backgroundColor: #1e1e1e
-->

# **Let's Look Under the Hood**

![w:1150px](images/solution-flowchart.svg)
![w:900px](images/solution-flowchart-2.svg)

<!--
- 
- As a result...
-->

---

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
- prevents mass, unnecessary alerts and ticket creation
- proactive, automatic approach
- custom, disgestable alert to escalate
- top-left: example error sending mass alerts
- bottom-left: api counter alerts
- right: custom opsgenie alert, as oppose to mass alerts
-->

---

# **Future Road Map**

[![](https://mermaid.ink/img/pako:eNq9kcFqwzAMhl9F6JxAnObk2yDtrZdul0EuIlZas9gujnwYpe8-m6QUxnYbEz5Y0qf_R-iGYzCMGs_kRQYPOcTKzHBgkhQZ9v5CfmTHXuAUyDi6rpgh4UOIjgTgPUd9PNZ9v_YWHsUGn0UkFRG1ll9AaPmAZ2hSFbSN6upG5VfBrjEb6oNcOD4HNE2Sc1IAZSRjP1u1a_mtzFlf2pvVw0a1RUG1mxF9NwINbfer_O7_Nun-ZhOs0HE-kzX5zLeCDpg5xwPq_DU8UZplwMHfM5qu5a57YyVE1BPNC1dIScLrpx9RS0z8gHpL50huo-5fllupdA)](https://mermaid.live/edit#pako:eNq9kcFqwzAMhl9F6JxAnObk2yDtrZdul0EuIlZas9gujnwYpe8-m6QUxnYbEz5Y0qf_R-iGYzCMGs_kRQYPOcTKzHBgkhQZ9v5CfmTHXuAUyDi6rpgh4UOIjgTgPUd9PNZ9v_YWHsUGn0UkFRG1ll9AaPmAZ2hSFbSN6upG5VfBrjEb6oNcOD4HNE2Sc1IAZSRjP1u1a_mtzFlf2pvVw0a1RUG1mxF9NwINbfer_O7_Nun-ZhOs0HE-kzX5zLeCDpg5xwPq_DU8UZplwMHfM5qu5a57YyVE1BPNC1dIScLrpx9RS0z8gHpL50huo-5fllupdA)
