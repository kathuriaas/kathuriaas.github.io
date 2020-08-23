---
layout: default
title: Home
nav_order: 1
permalink: /
---
# Platform for Learning with examples

This website has multiple topics. Click on the topic of your interest in the navigation menu on left (If you are using a mobile device, click on menu bar on top of this page).

## Setup a Unix/Linux machine

Before moving further, we should have a unix/linux machine with root access. Examples on this website can be replicated on a unix machine, which has docker installed for some cases. You can setup the machine using Virtual Box on a windows machine.

If you can't setup unix/linux machine locally, you can get one on any cloud vendor's platform, which is generally free for 1 year (Now, 3 months for GCP).

### Google Cloud Platform VM Instance

Google Cloud Platform (GCP) offers a VM (few OS options), with 1 GB RAM free for 1 year (now 3 months) under `Google Cloud Free Tier` for new accounts. GCP also gives $300 free, which can be used for 3 months. This amount can be used to add more RAM to the VM. See this [link](https://cloud.google.com/free/docs/gcp-free-tier) for details. Go through this link carefully, to avoid any unexpected charges. Terms and conditions may be changed by GCP anytime.

Follow below steps to create a new VM on GCP:-

- Create a GCP account [here](https://accounts.google.com/signin).
- Now, login to Google Cloud Console link [here](https://console.cloud.google.com/).
- On left top corner of page, look for menu and search for VM Instances.
- Click `Create Instance`.
- Provide details and choose options, as per need.
- Click `create`.
- You are now ready with your machine.
- Now, connect to your VM instance using instructions [here](https://cloud.google.com/compute/docs/instances/connecting-to-instance).

### AWS EC2

AWS offers free EC2 (VM instance) for 1 year, for new accounts.

Follow below steps to create EC2:-

- Create account on AWS [here](https://aws.amazon.com/console/).
- Now, login to AWS console and search for EC2.
- Click on `Launch Instance`.
- Select Operating System.
- Now choose other options and click `Review and Launch`.
- Now, connect to your VM instance using instructions [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html).
