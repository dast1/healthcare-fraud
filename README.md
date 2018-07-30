<div class="cell text_cell rendered unselected" tabindex="2">
<div class="inner_cell">
<div class="text_cell_render rendered_html" tabindex="-1">
<h1>Healthcare Fraud/Abuse Detection</h1>
</div>
</div>
</div>
<div class="cell text_cell unselected rendered" tabindex="2">
<div class="prompt input_prompt"><strong>1. Project Objective:</strong></div>
<div class="prompt input_prompt">
There over 800,000 healthcare providers in the US and since the beginning of 2013, the OIG (the Office of Inspector General of the US Department of Health and Human Services) excluded over 18,000 for various healthcare violations (see table 1: Summary of the List of Excluded Individuals and Entities). 
<br />
The primary objective of this project is to develop a Machine Learning model that will aid the OIG to target investigations into potential healthcare fraud or abuse more accurately.&nbsp;</div>
<br />
<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>Code</th>      <th>Description</th>      <th>Count</th>    </tr>  </thead>  <tbody>    <tr>      <td>1128b4</td>      <td>License revocation, suspension, or surrender. Minimum Period: Period imposed by the state licensing authority.</td>      <td>7439.0</td>    </tr>    <tr>      <td>1128a1</td>      <td>Conviction of program-related crimes. Minimum Period: 5 years</td>      <td>6540.0</td>    </tr>    <tr>      <td>1128a3</td>      <td>Felony conviction relating to health care fraud. Minimum Period: 5 years</td>      <td>1573.0</td>    </tr>    <tr>      <td>1128a2</td>      <td>Conviction relating to patient abuse or neglect. Minimum Period: 5 years</td>      <td>1313.0</td>    </tr>    <tr>      <td>1128a4</td>      <td>Felony conviction relating to controlled substance. Minimum Period: 5 years</td>      <td>907.0</td>    </tr>    <tr>      <td>1128b5</td>      <td>Exclusion or suspension under federal or state health care program. Minimum Period: No less than the period imposed by federal or state health care program.</td>      <td>249.0</td>    </tr>    <tr>      <td>1128b1</td>      <td>Misdemeanor conviction relating to health care fraud. Baseline Period: 3 years</td>      <td>246.0</td>    </tr>    <tr>      <td>1128b14</td>      <td>Default on health education loan or scholarship obligations. Minimum Period: Until default or obligation has been resolved.</td>      <td>182.0</td>    </tr>    <tr>      <td>1128b7</td>      <td>Fraud, kickbacks, and other prohibited activities. Minimum Period: None</td>      <td>110.0</td>    </tr>    <tr>      <td>1128b3</td>      <td>Misdemeanor conviction relating to controlled substance. Baseline Period: 3 years</td>      <td>32.0</td>    </tr>    <tr>      <td>1128b8</td>      <td>Entities controlled by a sanctioned individual. Minimum Period: Same as length of individual\'s exclusion.</td>      <td>24.0</td>    </tr>    <tr>      <td>1128b2</td>      <td>Conviction relating to obstruction of an investigation or audit. Baseline Period: 3 years</td>      <td>15.0</td>    </tr>    <tr>      <td>Misc.</td>      <td>Other</td>      <td>20.0</td>    </tr>    <tr>      <td></td>      <td>Total</td>      <td>18650.0</td>    </tr>  </tbody></table>
<br />
<div class="prompt input_prompt"><strong>2. How has this problem been solved before? If you feel like you are addressing a novel issue, what similar problems have been solved, and how are you borrowing from those?:</strong></div>
<div class="prompt input_prompt">
"The Office of Inspector General investigates complaints or allegations of wrongdoing or misconduct by employees or contractors that involve or give rise to fraud, waste or abuse within the programs or operations of the FCC.<br />
Allegations are received primarily from FCC employees and licensees. However, members of Congress, other agencies, citizens, contractors and public interest groups also refer matters to the OIG for investigation. Allegations of suspected wrongdoing are also received from FCC managers and the OIG audit program ." (source: <a href="https://www.fcc.gov/inspector-general/general/investigations#block-menu-block-4">www.fcc.gov</a>)<br />
<br />
"James Cosgrove, who directs health care reviews for the Government Accountability Office, told the House Ways and Means oversight subcommittee that the Medicare Advantage improper payment rate was 10 percent in 2016, which comes to $16.2 billion." (source: <a href="https://www.publicintegrity.org/2017/07/19/21011/fraud-and-billing-mistakes-cost-medicare-and-taxpayers-tens-billions-last-year">www.publicintegrity.org</a>)<br />
<br />
Healthcare fraud prevention is a big business and there isn't a shortage of experts and consultants in this space. One of them is <a href="https://www.accenture.com/us-en/company-michael-petersen">Dr. Mike Peterson</a> from Accenture. I've reached out to him through a mutual friend and was told that Accenture has a team of data scientists working on problems such as these. Dr. Peterson, seems very interested in my project and I plan on inviting him or someone from his team to the DSI71 cap-stone presentation day.<br /> 
&nbsp;</div>
<br />
<div class="prompt input_prompt"><strong>3. What is new about your approach, why do you think it will be successful?:</strong></div>
<div class="prompt input_prompt">
Heathcare fraud is a big, multi faceted, complex problem and there are lot of smart people who are involved in solving various aspects of this huge problem. With that said, I beleive there is still plenty of room to make a meaningful contribution. I beleive I will be successful because, my project is pretty specific and set-up ideally for levearging AI and ML.<br />
<br />
<div class="prompt input_prompt"><strong>4. Who cares? If you're successful, what will the impact be?:</strong></div>
<div class="prompt input_prompt">
"MFCUs coordinated over 18,000 investigations for Medicaid fraud and neglect, where fraud made up 15,509 of that total. The results of the investigations led to a total recovery of $1.8 billion,..." 
"Texas ($53,618,692), California ($27,240,288), and Ohio ($23,031,251) respectively ranked 3rd, 4th, and 5th in the greatest number of criminal recoveries. These states also ranked in the top five for investigations in Medicaid fraud. A significant outlier for recovery amounts was Florida, where the MFCUs recovered $101,059,813 in Medicaid fraud, the highest by far of any state in the country." (Source: <a href="https://healthpayerintelligence.com/news/medicaid-fraud-control-units-recovered-1.8-billion-in-2016">www.healthpayerintelligence.com</a>)<br />
<br />
<div class="prompt input_prompt"><strong>5. Presentation Format:</strong></div>
<div class="prompt input_prompt">
<ul>
<li>Data visualization will be done in Tableau</li>
<li>Presentation of the research will be done using PowerPoint and a video recording. (I will also explore other alternatives such as Canva, Prezi, &amp; SlideDog)</li>
<li>All materials for this capstone project, including code, will also be publicaly available on my personal <a href="https://dast1.github.io/" rel="nofollow">github page</a>.</li>
</ul>
<br />
<div class="prompt input_prompt"><strong>6. What are your data sources? What is the size of your dataset, and what is your storage format?:</strong></div>
<div class="prompt input_prompt">
<ul>
<li>
<p><strong>List of offenders:</strong> The OIG maintains a List of Excluded Individuals/Entities (LEIE) from Federally funded health care programs pursuant to section 1128 of the Social Security Act (Act) and from Medicare and State health care programs under section 1156 of the Act). In addition to an online search tool, they have a flat file database avaialable for dowload. The records go back to 1977 and the most recent file is about 12.6MB.</p>
</li>
<li>
<p><strong>Prescription data:</strong> The Center for Medicare and Medicaid Services has a set of various health related data sets, including the Medicare Part D Prescriber Data &amp; Opioid Drug list. The Prescriber data sets for 2013-2016 years are available as flat files and range anywhere from 500-600MB for each year. Information contained in these record can be easily joined with the data from OIG as they both share multiple common fields such as first, last, or business name of the health practioner, their address and a National Provider Identifier or NPI - a unique 10-digit identification number issued to health care providers in the United States by the Centers for Medicare and Medicaid Services (CMS).</p>
</li>
<li><strong>DEA Controlled Substance List:</strong> "Drugs, substances, and certain chemicals used to make drugs are classified into five (5) distinct categories or schedules depending upon the drug&rsquo;s acceptable medical use and the drug&rsquo;s abuse or dependency potential. The abuse rate is a determinate factor in the scheduling of the drug; for example, Schedule I drugs have a high potential for abuse and the potential to create severe psychological and/or physical dependence. As the drug schedule changes-- Schedule II, Schedule III, etc., so does the abuse potential-- Schedule V drugs represents the least potential for abuse. A <a href="https://www.dea.gov/druginfo/ds.shtml" rel="nofollow">Listing of drugs</a> and their schedule are located at Controlled Substance Act (CSA) Scheduling or CSA Scheduling by Alphabetical Order."</li>
<li>
<p><strong>Crime data:</strong> Socrata claims that they are a market leader in making existing government data discoverable, usable, and actionable for government workers and the people they serve. All data is available in a json format and I have already registered and obtained an app token. A quick look through their data revealed that most of their data-sets are from police departments nationwide. This is exactly what I was looking for to incorporate into my model so I can norrow down the geographical regions where offending health practitioners operate.</p>
</li>
<li>
<p><strong>Demographic data:</strong> The United States Census Bureau has a large set of demographic data. I plan on incorporating income and education into my model and explore how they impact the predictive peroformance.</p>
</li>
</ul>
<br />
<div class="prompt input_prompt"><strong>7. What are potential problems with your capstone, and what have you done to mitigate these problems?:</strong></div>
<div class="prompt input_prompt">
The primary concern for me with regards to this project is my lack of domain expertise. That's why I've established contacts with <a href="https://www.accenture.com/us-en/company-michael-petersen">Dr. Mike Peterson</a> from Accenture and Dr. Ted Spears, Chief Medical Officer for the Inspector General of the Texas Health and Human Services Commission.<br />
<br />
<div clas s="prompt input_prompt"><strong>8. What is the next thing you need to work on? Getting the data, not just some, likely all? Understanding the data? Building a minimum viable product? Gauging how much signal might be in the data?:</strong></div>
<div class="prompt input_prompt">
<ol>
<li>Getting data:<br />
<ol>
<li>Crime data,</li>
<li>Demographic data</li>
</ol>
</li>
<li>Perform EDA of:<br />
<ol>
<li>List of Excluded Individuals/Entities (LEIE),</li>
<li>Medicare Part D Prescriber Data,</li>
<li>Controlled Substance List (in 16 pages in PDF)</li>
</ol>
</li>
<li>The sprase feature matrix can easily be over 10,000 features for 800,000 unique NPIs for each year. This feature matrix can easily exceed 200 Gigs. Therefore, I will have to build a model using Spark on AWS EMR.</li>
</ol>
