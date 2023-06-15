# Virtual-Currency-Practise
[中文](README_zh.md) | English
collect data from OKE, establish prediction model and make trade strategies
1. git clone
2. open this new folder
3. make change 
4. git add . (add untracked files)
5. git commit -a -m "your comment"
6. git push -u origin(remote repository's url) main(branch you want)
7. git status(working repository's status)
8. git remote -v(remote repository's url)
9. git rm 

## parameters
<table><thead>
<tr>
<th style="text-align: left">Parameter</th>
<th style="text-align: left">Type</th>
<th style="text-align: left">Required</th>
<th style="text-align: left">Description</th>
</tr>
</thead><tbody>
<tr>
<td style="text-align: left">instId</td>
<td style="text-align: left">String</td>
<td style="text-align: left">Yes</td>
<td style="text-align: left">Instrument ID, e.g. <code>BTC-USD-190927-5000-C</code></td>
</tr>
<tr>
<td style="text-align: left">bar</td>
<td style="text-align: left">String</td>
<td style="text-align: left">No</td>
<td style="text-align: left">Bar size, the default is <code>1m</code><br>e.g. [1m/3m/5m/15m/30m/1H/2H/4H] <br>Hong Kong time opening price k-line：[6H/12H/1D/2D/3D/1W/1M/3M]<br>UTC time opening price k-line：[/6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc]</td>
</tr>
<tr>
<td style="text-align: left">after</td>
<td style="text-align: left">String</td>
<td style="text-align: left">No</td>
<td style="text-align: left">Pagination of data to return records earlier than the requested <code>ts</code></td>
</tr>
<tr>
<td style="text-align: left">before</td>
<td style="text-align: left">String</td>
<td style="text-align: left">No</td>
<td style="text-align: left">Pagination of data to return records newer than the requested <code>ts</code></td>
</tr>
<tr>
<td style="text-align: left">limit</td>
<td style="text-align: left">String</td>
<td style="text-align: left">No</td>
<td style="text-align: left">Number of results per request. The maximum is <code>300</code>. The default is <code>100</code>.</td>
</tr>
</tbody></table>
