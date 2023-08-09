'''
BMI Calculate

รับ input 2 จำนวนโดยที่ input ที่ 1 คือ h เป็นค่าความสูง(เมตร) และ Input ที่ 2 คือ w เป็นค่าน้ำหนัก(กิโลกรัม) โดยให้คำนวณหาค่า BMI ที่คำนวณจากสูตร BMI = w / (h^2) โดยให้แสดงผลตามข้อความข้างล่าง

BMI < 18.50 แสดงผล Less Weight

18.50 <= BMI  < 23 แสดงผล Normal Weight

23 <= BMI  < 25 แสดงผล Morethan Normal Weight

25 <= BMI  < 30 แสดงผล Getting Fat

BMI  >= 30 แสดงผล Fat
'''


h,w= input("Enter your High and Weight : ").split()
h = float(h)
w = float(w)
BMI = w/h/h
if BMI<18.50:
    print("Less Weight")
elif BMI>=18.50 and BMI<23 :
    print("Normal Weight")
elif BMI>=23 and BMI<25:
    print("More than Normal Weight")
elif BMI>=25 and BMI<30:
    print("Getting Fat")
else :
    print("Fat")

'''
Enter your High and Weight : 1.7 70
More than Normal Weight

Enter your High and Weight : 1.7 65
Normal Weight

Enter your High and Weight : 1.7 60
Normal Weight

Enter your High and Weight : 1.85 70
Normal Weight

Enter your High and Weight : 1.90 65
Less Weight

Enter your High and Weight : 1.7 90
Fat

Enter your High and Weight : 1.7 85
Getting Fat

Enter your High and Weight : 1.87 120
Fat
'''