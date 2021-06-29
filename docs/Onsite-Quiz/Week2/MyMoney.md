# Week 2 - My Money
## Description
ให้น้องทำโปรแกรมสมุดบัญชีธนาคารตัวเอง โดยสามารถถอนเงินหรือฝากเงินก็ได้เรื่อยๆ หรือจะสั่งปิดบัญชีก็ได้ โดยจะหยุดการทำงานก็ต่อเมื่อรับคำว่า Stop
โดย withdraw คือ การถอนเงิน
deposit คือ ฝากเงิน
delete คือ การปิดบัญชี (เงินคงเหลือเป็น 0)

## Specification
|Input|Output|
|-|-|
|บรรทัดแรก ชื่อบัญชี <br> อีก n บรรทัด เป็นการทำรายการในบัญชี จนกว่าจะรับคำว่า Stop <br> โดยบรรทัดแรก เป็นสถานะ deposit, withdraw หรือ delete <br> บรรทัดต่อมา จำนวนเงินเป็นจำนวนเต็ม|ชื่อบัญชี : จำนวนเงินที่คงเหลือในธนาคาร เป็นจำนวนเต็ม|

## Sample Input / Output
|Sample Input|Sample Output|
|-|-|
|joe <br> deposit <br> 120 <br> deposit <br> 3000 <br> withdraw <br> 2500 <br> Stop|joe : 620|
|Stick of Truth <br> deposit <br> 3000000000 <br> deposit <br> 720 <br> deposit <br> 3200 <br> withdraw <br> 72000000 <br> delete <br> deposit <br> 300 <br> withdraw <br> 110 <br> Stop|Stick of Truth : 190|
