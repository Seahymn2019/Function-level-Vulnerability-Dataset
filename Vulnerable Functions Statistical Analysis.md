## Vulnerable Functions Statistical Analysis

The "Data" folder contains the source code of vulnerable functions and non-vulnerable ones stored in a Zip file containing the 9 projects used in the experiments. After unzipping the files, one will find that the source code of each vulnerable function was named with its CVE ID. For the non-vulnerable functions, they were named with "{filename}_{functionname}.c" format. 

This folder also contains the Vulnerabilities_info.xlsx file which details information of the collected function-level vulnerabilities. These vulnerabilities are from 9 open-source projects. The vulnerability information was collected from [National Vulnerability Database(NVD)](https://nvd.nist.gov/) until the end of 2018.

The table shown below lists the 9 open-source projects involved in the evaluation.

    ------------------------------------------------------------------------
      Open-source projects  |         Web page
    ------------------------------------------------------------------------
          Asterisk          |    https://www.asterisk.org/
          FFmpeg            |    https://ffmpeg.org/
          HTTPD             |    https://httpd.apache.org
          LibPNG            |    https://www.libpng.org/pub/png/libpng.html
          LibTIFF           |    https://www.libtiff.org/
          OpenSSL           |    https://www.openssl.org/
          Pidgin            |    https://pidgin.im/
          VLC Media Player  |    https://www.videolan.org/vlc/index.html
          Xen               |    https://xenproject.org/
    ------------------------------------------------------------------------

The following graphs show the statistics of collected vulnerable functions from the 9 open-source projects.
Fig.1 shows the number of vulnerable functions labeled for each open-source project.
<div align=center><img width="600" height="500" src="https://github.com/Seahymn2019/Function-level-Vulnerability-Dataset/blob/master/Graph/The%20number%20of%20vulnerabilities.jpg" alt="Tree Graph of Category"/></div>

Fig.2 shows the annual distribution of vulnerable functions which we labeled.
<div align=center><img width="600" height="500" src="https://github.com/Seahymn2019/Function-level-Vulnerability-Dataset/blob/master/Graph/Vulnerability%20Annual%20Statistics.jpg" alt="Tree Graph of Category"/></div>

Fig.3 shows the trend of the labeled vulnerable functions from 9 open-source projects.
<div align=center><img width="600" height="500" src="https://github.com/Seahymn2019/Function-level-Vulnerability-Dataset/blob/master/Graph/Trend.jpg" alt="Tree Graph of Category"/></div>

Fig.4 shows the distribution of vulnerability category in our dataset.
<div align=center><img width="600" height="500" src="https://github.com/Seahymn2019/Function-level-Vulnerability-Dataset/blob/master/Graph/Vulnerability%20category%20treemap.jpg" alt="Tree Graph of Category"/></div>

Fig.5 shows the CVSS severity distribution in our dataset.
<div align=center> <img width="600" height="500" src="https://github.com/Seahymn2019/Function-level-Vulnerability-Dataset/blob/master/Graph/Severity%20Histogram.jpg" alt="Tree Graph of Category"/></div>

