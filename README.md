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
The Office of Inspector General investigates complaints or allegations of wrongdoing or misconduct by employees or contractors that involve or give rise to fraud, waste or abuse within the programs or operations of the FCC.<br />
<br />
Allegations are received primarily from FCC employees and licensees. However, members of Congress, other agencies, citizens, contractors and public interest groups also refer matters to the OIG for investigation. Allegations of suspected wrongdoing are also received from FCC managers and the OIG audit program. (<a href="https://www.fcc.gov/inspector-general/general/investigations#block-menu-block-4"></a>source<br />)
The primary objective of this project is to develop a Machine Learning model that will aid the OIG to target investigations into potential healthcare fraud or abuse more accurately.&nbsp;</div>
<br />
