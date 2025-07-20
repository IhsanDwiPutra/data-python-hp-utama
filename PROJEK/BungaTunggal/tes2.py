nilai1_1 = 1
nilai1_2 = -1
nilai1 = 6

nilai2_1 = 1
nilai2_2 = 1
nilai2 = 10

hasil1_1 = nilai2_1 * nilai1_1
hasil1_2 = nilai2_1 * nilai1_2
hasil1_3 = nilai2_1 * nilai1

hasil2_1 = nilai1_1 * nilai2_1
hasil2_2 = nilai1_1 * nilai2_2
hasil2_3 = nilai1_1 * nilai2

hasill1 = hasil1_1 - hasil2_1
hasill2 = hasil1_2 - hasil2_2
hasill3 = hasil1_3 - hasil2_3

jadi = hasill3 / hasill2


print(f"""
{nilai1_1}  {nilai1_2} = {nilai1}  |x{nilai2_1}| {hasil1_1}  {hasil1_2} = {hasil1_3} 
{nilai2_1} + {nilai2_2} = {nilai2} |x{nilai1_1}| {hasil2_1} + {hasil2_2} = {hasil2_3}
	   {15*"-"} -
	       {hasill1} {hasill2} = {hasill3}
	        = {jadi}
	   
""")