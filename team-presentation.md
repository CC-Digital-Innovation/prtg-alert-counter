---
theme: gaia
class: invert
paginate: true
backgroundColor: #000
marp: true
---

# 

![bg 50%](https://user-images.githubusercontent.com/103965932/173462799-95b24a44-5926-426d-a1d2-92482b982c97.png)

---

# **Team Introductions**

![bg](https://user-images.githubusercontent.com/103965932/173463669-ca46743c-5b2a-48e2-83e3-78382bce2354.jpg )
![bg](https://user-images.githubusercontent.com/103965932/173463695-2bdd4dec-b4ab-4ae0-a6ab-4aaba77087fd.jpg)
![bg](https://user-images.githubusercontent.com/103965932/173463684-ea7c6dce-e8c5-417d-a7fb-a3c6d73f6c95.jpg)
![bg](https://user-images.githubusercontent.com/103965932/173463689-25b9b672-4118-4b31-a673-3906d5aeee7e.jpg)
![bg](https://user-images.githubusercontent.com/103965932/173463646-0134093e-9cfc-4dac-9c1c-6599bea7033e.jpg)
![bg](https://user-images.githubusercontent.com/103965932/173463651-7cc6143d-df45-4be4-b42d-08031d79e58d.jpg)
![justify-content bottom](https://user-images.githubusercontent.com/103965932/173463700-8cc56e77-270e-4c06-83e8-24b946b18c2a.png)
​
---

# **The Brainstorming Process**

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

Deploying PRTG 
-create an amazon account 
-build an ec2 instance  
-build/install/configure prtg on ec2 instance 
-deploy servers to create sensors on prtg server 
​
Deploying Log server 
-Deploy a server for collecting logs 
-Install greylog application 
-Configure greylog to collect logs from prtg 
​
---
​
Deploying Tensorflow 
-Deploy an ec2 ubuntu and run updates 
-Install tensorflow packages and run updates if needed 
-Pull logs from syslog 
-Train model 
-Test model 


--- 

# **Wait...This Does Not Work**

Deploying an AI solution that can work off prtg message data is harder to setup than originally thought. 

---

# **Time for Reflection**

---

# **Our Solution (Version 2.0)** 

---

# **Overview of Solution**
Descriptiong
---

# **Let's Look Under the Hood**
Work Flow diagram
---

# **Results**

---

# **Future Road Map**

[![](https://mermaid.ink/img/pako:eNq9kcFqwzAMhl9F6JxAnObk2yDtrZdul0EuIlZas9gujnwYpe8-m6QUxnYbEz5Y0qf_R-iGYzCMGs_kRQYPOcTKzHBgkhQZ9v5CfmTHXuAUyDi6rpgh4UOIjgTgPUd9PNZ9v_YWHsUGn0UkFRG1ll9AaPmAZ2hSFbSN6upG5VfBrjEb6oNcOD4HNE2Sc1IAZSRjP1u1a_mtzFlf2pvVw0a1RUG1mxF9NwINbfer_O7_Nun-ZhOs0HE-kzX5zLeCDpg5xwPq_DU8UZplwMHfM5qu5a57YyVE1BPNC1dIScLrpx9RS0z8gHpL50huo-5fllupdA)](https://mermaid.live/edit#pako:eNq9kcFqwzAMhl9F6JxAnObk2yDtrZdul0EuIlZas9gujnwYpe8-m6QUxnYbEz5Y0qf_R-iGYzCMGs_kRQYPOcTKzHBgkhQZ9v5CfmTHXuAUyDi6rpgh4UOIjgTgPUd9PNZ9v_YWHsUGn0UkFRG1ll9AaPmAZ2hSFbSN6upG5VfBrjEb6oNcOD4HNE2Sc1IAZSRjP1u1a_mtzFlf2pvVw0a1RUG1mxF9NwINbfer_O7_Nun-ZhOs0HE-kzX5zLeCDpg5xwPq_DU8UZplwMHfM5qu5a57YyVE1BPNC1dIScLrpx9RS0z8gHpL50huo-5fllupdA)

---
