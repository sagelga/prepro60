(window.webpackJsonp=window.webpackJsonp||[]).push([[132],{396:function(r,e,v){"use strict";v.r(e);var _=v(13),t=Object(_.a)({},(function(){var r=this,e=r._self._c;return e("ContentSlotsDistributor",{attrs:{"slot-key":r.$parent.slotKey}},[e("h1",{attrs:{id:"week-2-plagarism"}},[e("a",{staticClass:"header-anchor",attrs:{href:"#week-2-plagarism"}},[r._v("#")]),r._v(" Week 2 - Plagarism")]),r._v(" "),e("h2",{attrs:{id:"description"}},[e("a",{staticClass:"header-anchor",attrs:{href:"#description"}},[r._v("#")]),r._v(" Description")]),r._v(" "),e("p",[e("img",{attrs:{src:"https://vignette2.wikia.nocookie.net/fallout/images/e/ec/Fo4_Hacker.png/revision/latest?cb=20170320162306",alt:""}})]),r._v(" "),e("p",[r._v("วันหนี่ง พี่ๆต้องการจะเล่นเกมหนึ่ง ชื่อเกมว่า Fallout 4"),e("br"),r._v("\nในเกมนั้น พี่ๆจะต้องแฮกคอมพิวเตอร์ โดยที่คอมพิวเตอร์จะแจกรหัสที่จะเข้าคอมพิวเตอร์หลายๆอัน"),e("br"),r._v("\nและให้ผู้เล่นเดารหัส โดยจะมีการใบ้คำตอบให้ ว่าถูกต้องกี่ตำแหน่ง"),e("br"),r._v("\nแต่ทว่า พี่ๆก็อยากจะฝึกให้เก่งๆอ่ะเนอะ มาช่วยพี่ๆที")]),r._v(" "),e("p",[r._v("วันนี้ น้องจึงเป็นคอมพิวเตอร์ ให้เช็คว่าพี่ๆใส่รหัสถูกต้องหรือไม่ โดยให้แสดงจำนวนตัวอักษรที่ถูกต้องเท่านั้น")]),r._v(" "),e("p",[r._v("เช่น"),e("br"),r._v("\nคำตอบที่แท้จริงเพื่อเข้าคอมพิวเตอร์ = 8234"),e("br"),r._v("\nและพี่ๆเดารหัสคอมพิวเตอร์มาว่า = 8542"),e("br"),r._v("\nซึ่งพี่ๆเดาถูกต้อง 1 ตำแหน่ง (ตัวเลข 8 ในหลักแรก)")]),r._v(" "),e("p",[r._v("ดังนั้น น้องจึงต้องเขียนบอกพี่ๆว่า ถูกต้องไปทั้งหมดกี่ตำแหน่ง"),e("br"),r._v("\nเอาเป็นว่าให้ปรี้นท์อะไร ให้ไปดูใน Output Specification ดีกว่าเนอะ")]),r._v(" "),e("h2",{attrs:{id:"specification"}},[e("a",{staticClass:"header-anchor",attrs:{href:"#specification"}},[r._v("#")]),r._v(" Specification")]),r._v(" "),e("table",[e("thead",[e("tr",[e("th",[r._v("Input")]),r._v(" "),e("th",[r._v("Output")])])]),r._v(" "),e("tbody",[e("tr",[e("td",[r._v("Input x+1 บรรทัด [สูงสุด 21 บรรทัด] (Integer หรือ String) "),e("br"),r._v(" บรรทัดแรก เป็นคำตอบที่ถูกต้อง "),e("br"),r._v(" บรรทัดที่สองเป็นต้นไป เป็นคำตอบที่พี่ๆเดาออกมา "),e("br"),r._v(" และรับมาเรื่อยๆ จนกว่าพี่ๆจะเดาได้ถูกต้อง หรือครบ 20 ครั้ง "),e("br"),r._v(" "),e("br"),r._v(" โดยค่าที่รับมา หากเป็นตัวอักษร "),e("br"),r._v(" ตัวอักษรตัวใหญ่และเล็กจะถือว่าเป็นตัวเดียวกัน เช่น kuma = KUMA")]),r._v(" "),e("td",[r._v("Output ทุกบรรทัดที่พี่ๆเดา [สูงสุด 20 บรรทัด] (String) "),e("br"),r._v(" หาก เดาได้ถูกหรือไม่ถูกเลย จะให้ตอบว่า Likeness = x (โดย x คือตอบได้ตรงคำตอบกี่ตำแหน่ง) "),e("br"),r._v(" "),e("br"),r._v(" หาก รหัสที่พี่ๆเดา ความยาวไม่เท่ากับคำตอบ จะให้ตอบว่า Entry Denied "),e("br"),r._v(" "),e("br"),r._v(" หาก เดาได้ตรงกับคำตอบ จะให้ตอบว่า System Unlocked "),e("br"),r._v(" แทนการปรี้นท์ Likeness หรือ Entry Denied และหยุดการทำงานของโปรแกรมทันที "),e("br"),r._v(" "),e("br"),r._v(" หาก เป็นการเดาครั้งที่ 20 แล้วยังคงเดาได้ไม่ตรงกับคำตอบ (ยังคงตอบผิด หรือ Entry Denied) "),e("br"),r._v(" จะให้ตอบว่า System Locked Down แทนการปรี้นท์ Likeness หรือ Entry Denied "),e("br"),r._v(" และหยุดการทำงานของโปรแกรมทันที")])])])]),r._v(" "),e("h2",{attrs:{id:"sample-input-output"}},[e("a",{staticClass:"header-anchor",attrs:{href:"#sample-input-output"}},[r._v("#")]),r._v(" Sample Input / Output")]),r._v(" "),e("table",[e("thead",[e("tr",[e("th",[r._v("Input")]),r._v(" "),e("th",[r._v("Output")])])]),r._v(" "),e("tbody",[e("tr",[e("td",[r._v("1234 "),e("br"),r._v(" 1000 "),e("br"),r._v(" 0200 "),e("br"),r._v(" 0030 "),e("br"),r._v(" 0004 "),e("br"),r._v(" 1234")]),r._v(" "),e("td",[r._v("Likeness = 1 "),e("br"),r._v(" Likeness = 1 "),e("br"),r._v(" Likeness = 1 "),e("br"),r._v(" Likeness = 1 "),e("br"),r._v(" System Unlocked")])]),r._v(" "),e("tr",[e("td",[r._v("kumamon "),e("br"),r._v(" kynonan "),e("br"),r._v(" KYNONAN "),e("br"),r._v(" kYnOnAn "),e("br"),r._v(" KUMAMON")]),r._v(" "),e("td",[r._v("Likeness = 2 "),e("br"),r._v(" Likeness = 2 "),e("br"),r._v(" Likeness = 2 "),e("br"),r._v(" System Unlocked")])]),r._v(" "),e("tr",[e("td",[r._v("1234 "),e("br"),r._v(" 1234567 "),e("br"),r._v(" 123 "),e("br"),r._v(" 12340 "),e("br"),r._v(" ABCD "),e("br"),r._v(" A234 "),e("br"),r._v(" 1234")]),r._v(" "),e("td",[r._v("Entry Denied "),e("br"),r._v(" Entry Denied "),e("br"),r._v(" Entry Denied "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 3 "),e("br"),r._v(" System Unlocked")])]),r._v(" "),e("tr",[e("td",[r._v("12345 "),e("br"),r._v(" 10000 "),e("br"),r._v(" 12000 "),e("br"),r._v(" 12300 "),e("br"),r._v(" 12340 "),e("br"),r._v(" 12345")]),r._v(" "),e("td",[r._v("Likeness = 1 "),e("br"),r._v(" Likeness = 2 "),e("br"),r._v(" Likeness = 3 "),e("br"),r._v(" Likeness = 4 "),e("br"),r._v(" System Unlocked")])]),r._v(" "),e("tr",[e("td",[r._v("1234 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000 "),e("br"),r._v(" 0000")]),r._v(" "),e("td",[r._v("Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" Likeness = 0 "),e("br"),r._v(" System Locked Down")])])])])])}),[],!1,null,null,null);e.default=t.exports}}]);