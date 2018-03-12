import  urllib3    # the lib that handles the url stuff
import pandas as pd
urllib3.disable_warnings()
http = urllib3.PoolManager()
target_url = input("URL of the FastTimerService log file: ")
output_html_file = input("output file: ")


r = http.request('GET', target_url)
text = r.data.decode()
lines = text.split("\n")

report = {}

for line in lines:
    if line.startswith("FastReport") and len(line.split()) == 18:
        _, CPUavgtime, _ , CPUwhenRunOnlytime, _ , RealavgTime, _, RealwhenRunOnlyTime, _, memoryAlloc, _ , _,  _,  _,  _,  _,  _, moduleName = line.split()

        modInfo = (CPUavgtime, CPUwhenRunOnlytime,  RealavgTime, RealwhenRunOnlyTime, memoryAlloc)
        report[moduleName] =  modInfo
df = pd.DataFrame(report).transpose()

df.columns = ['Average CPU Time (ms)',
              'Average CPU Time when executed (ms)',
              'Average Real Time (ms)',
              'Average Real Time when executed (ms)',
              'Allocated Memory (kB)']


file = open(output_html_file,'w')
file.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n<title>Time Report</title>\n<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/v/dt/jq-3.2.1/dt-1.10.16/af-2.2.2/b-1.5.1/b-colvis-1.5.1/b-html5-1.5.1/b-print-1.5.1/cr-1.4.1/fc-3.2.4/kt-2.3.2/r-2.2.1/rg-1.0.2/sc-1.4.4/sl-1.2.5/datatables.min.css"/>\n<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.32/pdfmake.min.js"></script>\n<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.32/vfs_fonts.js"></script>\n<script type="text/javascript" src="https://cdn.datatables.net/v/dt/jq-3.2.1/dt-1.10.16/af-2.2.2/b-1.5.1/b-colvis-1.5.1/b-html5-1.5.1/b-print-1.5.1/cr-1.4.1/fc-3.2.4/kt-2.3.2/r-2.2.1/rg-1.0.2/sc-1.4.4/sl-1.2.5/datatables.min.js"></script>\n<script type="text/javascript" language="javascript" class="init" src="dataTableCustomization.js"></script>\n</head>\n')



file.close()
file = open(output_html_file,'a')
file.write('''<button id="button">Row count</button>
<div id="avgCPUTimeSelTmp"></div>
<div id="avgCPUTimeOnlySelTmp"></div>
<div id="avgRealTimeSelTmp"></div>
<div id="avgRealTimeOnlySelTmp"></div>
<div id="avgMemSelTmp"></div>
''')
file.write(df.to_html(classes = 'display" id = "timereport" cellspacing="0" width="100%').replace('</thead>',
'''</thead>
        <tfoot>
            <tr>
                <th>Selected Rows Total</th>
                <th id ="avgCPUTimeSel"></th>
                <th id ="avgCPUTimeOnlySel"></th>
                <th id ="avgRealTimeSel"></th>
                <th id ="avgRealTimeOnlySel"></th>
                <th id ="avgMemSel"></th>
            </tr>
            <tr>
                <th>Overall Total</th>
                <th id ="avgCPUTimeTot"></th>
                <th id ="avgCPUTimeOnlyTot"></th>
                <th id ="avgRealTimeTot"></th>
                <th id ="avgRealTimeOnlyTot"></th>
                <th id ="avgMemTot"></th>
            </tr>
            <tr>
                <th>Page Total</th>
                <th id ="avgCPUTimePageTot"></th>
                <th id ="avgCPUTimeOnlyPageTot"></th>
                <th id ="avgRealTimePageTot"></th>
                <th id ="avgRealTimeOnlyPageTot"></th>
                <th id ="avgMemPageTot"></th>
            </tr>
        </tfoot>
'''))


file.write("\n")
file.close()
