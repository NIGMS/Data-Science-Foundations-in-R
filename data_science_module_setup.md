

# Setting Up a Jupyter Notebook in Google Cloud Console

## Initial Access
1. Navigate to Google Cloud Console using this URL:  [https://console.cloud.google.com/welcome](https://console.cloud.google.com/welcome)
2. In the search bar at the top of the console, type "Vertex AI" and select it from the search results

<img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXd8h7ybiiNfu3Lm38OdIpG_DKpHNwEszKxsgqSIsrJE_C8tELIL5Mzz5FZ_w7oa1Zi1SEVjPrXjoR8Olt0-P_tZ6tAGhin5jQvX7tRxrTv49oaEMA7TsEypoWaOdFABKVw7VNXD?key=dKp5FwnnbucCvNhB4NAX4_8B" alt="img" style="zoom:67%;" />

## Setting Up Vertex AI Workbench
1. Within Vertex AI, locate and select "Workbench" from the available options

<img src="assets/img/image-20250127200440871.png" alt="image-20250127200440871" style="zoom:50%;" />

2. Click "Create New Instance" to begin setting up your Jupyter environment

## Configuring Your Instance
1. Basic Setup:
   - Provide a meaningful name for your instance
   - Click "Advanced Options" to access additional configuration settings

<img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXf7EE2lAyE-P4YLaeN71KlypSza91MsdbRWFclwNLNrzLSGEHI8z9UH22ikBX9_0Ljhbi9I4lEte7xmh1anKtS0r3p6lC9097XHoyOkTqYDDPBsugTPDbY32Utid4jE7bnxfpu88w?key=dKp5FwnnbucCvNhB4NAX4_8B" alt="img" style="zoom:50%;" />

2. Environment Configuration:
   - Navigate to the "Environment" tab
   - Select "JupyterLab 4" as your development environment

<img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfPzdjxJT9agX1oxjWsbAvOzAkdffAfeUeGuJLvQptovu5xaMAfLdBgfjXv0VtKPrsdIhJBwf9K6MsH2EG9DTX4gp3QxH7R09_E_2QVuVLpR4Mx42wmvm5o3VuO8PjuvdKZ1GQZeQ?key=dKp5FwnnbucCvNhB4NAX4_8B" alt="img" style="zoom:50%;" />

   - Look for the "Startup Script" option

     <img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfIlm0CIJMZbF-9-nBZobmKLHs4W0YuqTC6UlQihIi7l7h7YDUvCHTmHtJTHZzLwACn6Ki1J-QzO97G-SRxlJA3eMWu3gSnwQqxYaRkx7uspjCVWW1ds6efzFrLl9hMCUdYxTTg4w?key=dKp5FwnnbucCvNhB4NAX4_8B" alt="img" style="zoom:50%;" />

   - Click "Browse" to locate the script

   - Paste to "gs://nigms-sandbox/nosi-duke/post_start_clean_032225.sh"


<img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXekFnjgdo8elVtvYBgHh57ca6uKLJjBhtBgDVKTX7kUdWzIYnEAu-2xwxB4i1X2_70rMIUREwaZ310QlAUCL12F3hrahpF1atsQfU3SkMQaTKh-q3N6SsxeBrEIQtoGBdPS9inC?key=dKp5FwnnbucCvNhB4NAX4_8B" alt="img" style="zoom:50%;" />

3. Machine Configuration:
   - For machine type, the default settings are typically sufficient
   
     <img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfQR8LimU3pf1ykmJTdxs88ZaBS12NULvHVIaIG9AI_hVFH8Uflv78_YHRqigdw1trznlhunuyFFwaouYG84t5EaXImtWQcnqzVOR1OeeehlGfVUX0MrSid4qVLtM0c7WN0Ef9nTg?key=dKp5FwnnbucCvNhB4NAX4_8B" alt="img" style="zoom:50%;" />
   
   - Important: Ensure "Enable idle shutdown" is checked to avoid unnecessary resource usage

<img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXc6QHwKUC29_-SlPNlQMWlwap55_76ONhtzgK5eOaqHQPjSjsjWc0TTEV7qbsl4KI9tGOAxk8z8H7njCSzvV85GqDlBw9Tjli9zPzDVnvKlIgbeWcgrGKrscCf5rwhjaeEzzZHGow?key=dKp5FwnnbucCvNhB4NAX4_8B" alt="img" style="zoom:50%;" />

   - Click "Create" at the bottom of the page

## Launching JupyterLab
1. Wait approximately 3-5 minutes for the instance to be fully provisioned
2. Once provisioning is complete, click "Start JupyterLab" to launch the environment

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc0KGfbuCvCc7KPxCQi0ntjaJuxbM_cicEULyDa558BC0sc-MWxZKYCMPtmSCXVG1AyolJru2xlUeC2M70w7TNkpAXTwx6i4aLvYnsrkG1ZXiMakbK13hm4XPZugGinXTNQYmUF3A?key=dKp5FwnnbucCvNhB4NAX4_8B)

## Setting Up Your Project Repository
1. In JupyterLab, locate and click the Git button in the sidebar

<img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdYtpdTOv73EkhW3LiNHbbQBRXR-RyagJsgFyfQA1dTecoxfzy5SgXYw2TpS3-4_bjJCXzTdIPt7ikeKBzkhpwDVqsSzCqQ6SjIW5KVTidmagdcz02a5yIUBvayMHqSntvbQou_?key=dKp5FwnnbucCvNhB4NAX4_8B" alt="img" style="zoom: 67%;" />

2. Select "Clone a Repository"

3. Enter the following repository URL: https://github.com/mitomac/duke_nigms_sandbox.git
4. Click "Clone" to download the repository

<img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfov5a8LLigr_PTJEI7QJlnrDMHDgp7g_eTVIGU5qmeFIRwb38AscqciovyfchJu_BgE13xHfFLpA7Y0_hUnQKQKKBPH-b0g9VeqBWDHcKOU-DTxfxhTBVp2gllBf5uuEUh_ieTsg?key=dKp5FwnnbucCvNhB4NAX4_8B" alt="img" style="zoom: 50%;" />

5. Navigate into the project by double-clicking the "duke_nigms_sandbox" folder to access the modules

<img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcRDYVmR-rbbFV7rxDAA0neq5SXREzJla2rncbR-KTlGKY9Yu_3f4IRStUtQo7HtKHt819L8JVqmAtl80gi64FTaJxcTQ1AD8OzZBZFS4xvwooi7gFLRPQ432LKAIqtXeYyKoCNcQ?key=dKp5FwnnbucCvNhB4NAX4_8B" alt="img" style="zoom:67%;" />

## Working with notebooks
1. If you're working with R notebooks, you'll be prompted to select a kernel

2. Choose the R kernel when prompted to ensure proper execution of R code

   ![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXckYuAXDg4-sk3xkNLD51xurb4xd0ycpAiyFMYGTXJE0LgAvIftTDd_MpADgqLypLmbTOghBRAz4XLX0yF4KhvXAiy8ujFGy34uHBnQf_6pnwPDtLJxklsYIZl6FHC_HaqfBA4?key=dKp5FwnnbucCvNhB4NAX4_8B)

## AI Assistant

1. Start the AI  assistant

   

   <img src="assets/img/image-20250127202922005.png" alt="image-20250127202922005" style="zoom:50%;" />

2. Generate and copy API key by running through [Module 0](./module0.ipynb) notebook.

3. Select a google gemini model and input the API key you just generated.

   <img src="assets/img/image-20250127202818547.png" alt="image-20250127202818547" style="zoom: 50%;" />


Additional Tips:
- Keep track of your instance's running time to manage resources effectively

- Save your work regularly

- Consider bookmarking the Google Cloud Console URL for easier access in the future

   
