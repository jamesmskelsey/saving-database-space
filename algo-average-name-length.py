import math

names = [
    ["James",   	4700229],
    ["Robert",  	4455696],
    ["John",    	4453807],
    ["Michael", 	4335919],
    ["William", 	3564276],
    ["David",   	3564053],
    ["Richard", 	2454407],
    ["Joseph",  	2335792],
    ["Thomas",  	2151864],
    ["Charles", 	2084043],
    ["Christopher", 2038798],
    ["Daniel",  	1895292],
    ["Matthew", 	1607467],
    ["Anthony", 	1406030],
    ["Mark",    	1347519],
    ["Donald",  	1336753],
    ["Steven",  	1282598],
    ["Paul",    	1275700],
    ["Andrew",  	1254054],
    ["Joshua",  	1220730],
    ["Kenneth", 	1220221],
    ["Kevin",   	1174762],
    ["Brian",   	1168073],
    ["George",  	1135235],
    ["Edward",  	1079619],
    ["Ronald",  	1072746],
    ["Timothy", 	1070916],
    ["Jason",   	1038335],
    ["Jeffrey", 	975915],	
    ["Ryan",    	942977],	
    ["Jacob",   	933692],	
    ["Gary",    	900088],	
    ["Nicholas",    894521],	
    ["Eric",    	879257],	
    ["Jonathan",    848774],	
    ["Stephen", 	839278],	
    ["Larry",   	802272],	
    ["Justin",  	779504],	
    ["Scott",   	769980],	
    ["Brandon", 	761473],	
    ["Benjamin",    740347],	
    ["Samuel",  	714013],	
    ["Gregory", 	707501],	
    ["Frank",   	691530],	
    ["Alexander",   675746],	
    ["Raymond", 	668793],	
    ["Patrick", 	664723],	
    ["Jack",    	636674],	
    ["Dennis",  	611128],	
    ["Jerry",   	602117],	
    ["Tyler",   	592495],	
    ["Aaron",   	583990],	
    ["Jose",    	562444],	
    ["Adam",    	554559],	
    ["Henry",   	552861],	
    ["Nathan",  	549445],	
    ["Douglas", 	548008],	
    ["Zachary", 	540674],	
    ["Peter",   	538899],	
    ["Kyle",    	481259],	
    ["Walter",  	464525],	
    ["Ethan",   	444913],	
    ["Jeremy",  	439166],	
    ["Harold",  	435205],	
    ["Keith",   	431424],	
    ["Christian",   429981],	
    ["Roger",   	428417],	
    ["Noah",    	427157],	
    ["Gerald",  	425285],	
    ["Carl",    	425085],	
    ["Terry",   	422213],	
    ["Sean",    	419666],	
    ["Austin",  	415211],	
    ["Arthur",  	407825],	
    ["Lawrence",    401973],	
    ["Jesse",   	387954],	
    ["Dylan",   	383878],	
    ["Bryan",   	382874],	
    ["Joe", 	    382502],	
    ["Jordan",  	382332],	
    ["Billy",   	378364],	
    ["Bruce",   	375579],	
    ["Albert",  	367790],	
    ["Willie",  	361107],	
    ["Gabriel", 	359009],	
    ["Logan",   	350490],	
    ["Alan",    	350127],	
    ["Juan",    	347289],	
    ["Wayne",   	337274],	
    ["Roy", 	    332214],	
    ["Ralph",   	330142],	
    ["Randy",   	328086],	
    ["Eugene",  	323717],	
    ["Vincent", 	323196],	
    ["Russell", 	318213],	
    ["Elijah",  	316573],	
    ["Louis",   	314537],	
    ["Bobby",   	313403],	
    ["Philip",  	313385],	
    ["Johnny",  	308289],	
    ["Mary",	    3196385],
    ["Patricia",	1558407],
    ["Jennifer",	1468377],
    ["Linda",	    1448303],
    ["Elizabeth",	1420377],
    ["Barbara",	    1397635],
    ["Susan",	    1103569],
    ["Jessica",	    1046322],
    ["Sarah",	    991910],
    ["Karen",	    986057],
    ["Nancy",	    966867],
    ["Lisa",	    965015],
    ["Betty",	    924629],
    ["Margaret",	918541],
    ["Sandra",	    873509],
    ["Ashley",  	849297],
    ["Kimberly",	839796],
    ["Emily",	    830999],
    ["Donna",	    822330],
    ["Michelle",	812335],
    ["Dorothy",	    811392],
    ["Carol",	    806170],
    ["Amanda",	    773199],
    ["Melissa",	    753994],
    ["Deborah",	    740019],
    ["Stephanie",	738523],
    ["Rebecca",	    729630],
    ["Sharon",  	720826],
    ["Laura",	    718006],
    ["Cynthia",	    705717],
    ["Kathleen",	686217],
    ["Amy",	        681397],
    ["Shirley",	    663452],
    ["Angela",	    658968],
    ["Helen",	    618563],
    ["Anna",	    618367],
    ["Brenda",	    606291],
    ["Pamela",	    592696],
    ["Nicole",	    589434],
    ["Emma",	    580610],
    ["Samantha",	578986],
    ["Katherine",	571574],
    ["Christine",	561161],
    ["Debra",	    548280],
    ["Rachel",	    546153],
    ["Catherine",	542748],
    ["Carolyn",	    540963],
    ["Janet",	    539224],
    ["Ruth",	    538629],
    ["Maria",	    529342],
    ["Heather",	    524166],
    ["Diane",	    515183],
    ["Virginia",	515088],
    ["Julie",	    506594],
    ["Joyce",	    499340],
    ["Victoria",    485786],
    ["Olivia",	    481364],
    ["Kelly",	    471621],
    ["Christina",	471106],
    ["Lauren",	    470902],
    ["Joan",	    467459],
    ["Evelyn",	    461952],
    ["Judith",	    449805],
    ["Megan",	    437647],
    ["Cheryl",	    436882],
    ["Andrea",	    436126],
    ["Hannah",	    431117],
    ["Martha",	    426247],
    ["Jacqueline",	420505],
    ["Frances",	    414289],
    ["Gloria",	    408565],
    ["Ann",	        407374],
    ["Teresa",	    404253],
    ["Kathryn",	    402613],
    ["Sara",	    400884],
    ["Janice",	    399546],
    ["Jean",	    399416],
    ["Alice",	    396362],
    ["Madison",	    393297],
    ["Doris",	    383158],
    ["Abigail",	    381738],
    ["Julia",	    380836],
    ["Judy",	    377815],
    ["Grace",	    377678],
    ["Denise",	    371269],
    ["Amber",	    370577],
    ["Marilyn",	    369781],
    ["Beverly",	    369669],
    ["Danielle",	368485],
    ["Theresa",	    367426],
    ["Sophia",	    364383],
    ["Marie",	    361371],
    ["Diana",	    359617],
    ["Brittany",    358850],
    ["Natalie",	    356379],
    ["Isabella",	354245],
    ["Charlotte",	347772],
    ["Rose",	    344656],
    ["Alexis",	    340587],
    ["Kayla",	    340511]
]

total_characters_to_save = 0
total_people = 0
for n in names:
    name = n[0]
    num = n[1]
    total_characters_to_save += len(name) * num
    total_people += num

average_length = math.ceil(total_characters_to_save / total_people)

# Totals to save every character of every name
print("Average name length", average_length)
print("Number of people", total_people)
print("Total number of letters", total_characters_to_save)
print("kB to save every persons name: ", total_characters_to_save / 1024)
print("mB to save every persons name: ", total_characters_to_save / 1024 / 1024)
print("gB to save every persons name: ", total_characters_to_save / 1024 / 1024 / 1024)

total_pointers_to_save = total_people / len(names)
print("kB to save a name for every person: ", total_pointers_to_save / 1024)
print("mB to save a name for every person: ", total_pointers_to_save / 1024 / 1024)
print("gB to save a name for every person: ", total_pointers_to_save / 1024 / 1024 / 1024)

print(f"Saving pointers to names in a database represents an average savings of {(1 - total_pointers_to_save / total_characters_to_save):%}")
