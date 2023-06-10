## 数据参数


<table><thead>
<tr>
<th style="text-align: left"><strong>参数名</strong></th>
<th style="text-align: left"><strong>类型</strong></th>
<th style="text-align: left"><strong>描述</strong></th>
</tr>
</thead><tbody>
<tr>
<td style="text-align: left">ts</td>
<td style="text-align: left">String</td>
<td style="text-align: left">开始时间，Unix时间戳的毫秒数格式，如 <code>1597026383085</code></td>
</tr>
<tr>
<td style="text-align: left">o</td>
<td style="text-align: left">String</td>
<td style="text-align: left">开盘价格</td>
</tr>
<tr>
<td style="text-align: left">h</td>
<td style="text-align: left">String</td>
<td style="text-align: left">最高价格</td>
</tr>
<tr>
<td style="text-align: left">l</td>
<td style="text-align: left">String</td>
<td style="text-align: left">最低价格</td>
</tr>
<tr>
<td style="text-align: left">c</td>
<td style="text-align: left">String</td>
<td style="text-align: left">收盘价格</td>
</tr>
<tr>
<td style="text-align: left">vol</td>
<td style="text-align: left">String</td>
<td style="text-align: left">交易量，以<code>张</code>为单位<br>如果是<code>衍生品</code>合约，数值为合约的张数。<br>如果是<code>币币/币币杠杆</code>，数值为交易货币的数量。</td>
</tr>
<tr>
<td style="text-align: left">volCcy</td>
<td style="text-align: left">String</td>
<td style="text-align: left">交易量，以<code>币</code>为单位<br>如果是<code>衍生品</code>合约，数值为交易货币的数量。<br>如果是<code>币币/币币杠杆</code>，数值为计价货币的数量。</td>
</tr>
<tr>
<td style="text-align: left">volCcyQuote</td>
<td style="text-align: left">String</td>
<td style="text-align: left">交易量，以计价货币为单位<br>如：BTC-USDT 和 BTC-USDT-SWAP, 单位均是 USDT；<br>BTC-USD-SWAP 单位是 USD</td>
</tr>
<tr>
<td style="text-align: left">confirm</td>
<td style="text-align: left">String</td>
<td style="text-align: left">K线状态 <br> <code>0</code> 代表 K 线未完结，<code>1</code> 代表 K 线已完结。</td>
</tr>
</tbody></table>