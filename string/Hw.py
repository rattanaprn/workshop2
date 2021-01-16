string = "I am the best ptogrammer"
# จงเขียนคำสั่งเพื่อแสดงความยาวของตัวอักษร "I am the best ptogrammer languages"
print(len(string))


# จงเขียนคำสั่งเพื่อแสดงอักษรแรกของข้อความ "I am the best ptogrammer languages"
print(string[1])

# จงเขียนคำสั่งเพื่อแสดง "best " ของข้อความ "I am the best ptogrammer languages"
print(string[9:13])

# จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best ptogrammer languages" ที่ไม่มี space
print(string.replace(" ", ""))

# จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best ptogrammer languages" ให้เป็นตัวพิมใหญ่ทั้งหมด
print(string.upper())

# จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best ptogrammer" ให้เป็นตัวพิมเล็กทั้งหมด
print(string.lower())

# จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best ptogrammer" ที่ถูกแทนที่อักษร e ด้วย z ทั้งหมด
print(string.replace("e", "z"))

# จงเติมคำในช่องว่าเพื่อแสดงชื่อ
myname = "Yayee"


txt = "{} is the best ptogrammer"

print(txt.format(myname))