# Source data for the Nottingham guide. geo = geocoder query; ll = fallback/override coordinates.
CATS = {
 "sights":   {"sec":"see","title":"Sights & oddities","emoji":"🏰","color":"#C0392B"},
 "galleries":{"sec":"see","title":"Galleries","emoji":"🎨","color":"#8E44C9"},
 "shops":    {"sec":"see","title":"Indie shops & makers","emoji":"🛍️","color":"#E8930C"},
 "records":  {"sec":"see","title":"Records, books & comics","emoji":"📀","color":"#1877D0"},
 "vintage":  {"sec":"see","title":"Vintage & antiques","emoji":"🧥","color":"#0F766E"},
 "gear":     {"sec":"see","title":"Cameras, music & tech","emoji":"📷","color":"#0E7490"},
 "food":     {"sec":"see","title":"Food shops & world grocers","emoji":"🧀","color":"#B45309"},
 "fun":      {"sec":"see","title":"Escape rooms & things to do","emoji":"🧩","color":"#DB2777"},
 "museums":  {"sec":"see","title":"Museums","emoji":"🏛️","color":"#7C2D12"},
 "sport":    {"sec":"see","title":"Sport","emoji":"🏏","color":"#166534"},
 "markets":  {"sec":"see","title":"Markets","emoji":"🧺","color":"#A16207"},
 "fashion":  {"sec":"see","title":"Clothes & boutiques","emoji":"👗","color":"#9D174D"},
 "charity":  {"sec":"see","title":"Charity shops","emoji":"♻️","color":"#15803D"},
 "parks":    {"sec":"see","title":"Parks & walks","emoji":"🌳","color":"#2F855A"},
 "trips":    {"sec":"see","title":"Day trips","emoji":"🚗","color":"#1D4ED8"},
 "cafes":    {"sec":"eat","title":"Cafés & coffee","emoji":"☕","color":"#0F9D8A"},
 "cheap":    {"sec":"eat","title":"Cheap eats & street food","emoji":"🌮","color":"#E8483B"},
 "mid":      {"sec":"eat","title":"Mid-range","emoji":"🍽️","color":"#E8930C"},
 "splurge":  {"sec":"eat","title":"Splurge & Michelin","emoji":"⭐","color":"#8E44C9"},
 "pubs":     {"sec":"eat","title":"Historic & real-ale pubs","emoji":"🍺","color":"#A0522D"},
 "bars":     {"sec":"eat","title":"Cocktails & craft bars","emoji":"🍸","color":"#1877D0"},
 "music":    {"sec":"eat","title":"Live music & comedy","emoji":"🎸","color":"#7C3AED"},
}

P = []
def add(cat, name, addr, text, tip, price=0, web="", ta=True, far=False, geo=None, ll=None, drive="", who=None):
    P.append(dict(cat=cat, name=name, addr=addr, text=text, tip=tip, price=price, web=web, ta=ta, far=far, drive=drive, who=who or [],
                  geo=geo or f"{name}, Nottingham", ll=ll))

# ---------------- SIGHTS & ODDITIES ----------------
add("sights","City of Caves","Garner's Hill steps, Sussex Street / Cliff Road, NG1 1HF",
 "Nottingham sits on soft sandstone riddled with more than 800 man-made caves. This guided tour takes you through medieval tannery pits, a WWII air-raid shelter and Victorian slum cellars right under the city centre. Tours run about every 30–45 minutes and take around an hour.",
 "Entrance at the foot of the Garner's Hill steps, by Nottingham Contemporary · now run by the National Justice Museum",web="https://nationaljusticemuseum.org.uk/cityofcaves",ll=(52.95045,-1.14520),geo="City of Caves, Nottingham")
add("museums","National Justice Museum","Shire Hall, High Pavement, NG1 1HN",
 "A Victorian courthouse and county gaol in the Lace Market, where you can stand in the dock, see the cells and the execution yard, and hear the grim stories of people tried here. Actors in costume bring the courtroom to life on some days.",
 "Allow 2 hours; good on a rainy day",web="https://www.nationaljusticemuseum.org.uk",geo="National Justice Museum, High Pavement, Nottingham")
add("sights","Nottingham Castle","Lenton Road, NG1 6EL",
 "Not a medieval castle but a 17th-century ducal mansion on top of Castle Rock, rebuilt after rioters burned it in 1831. Inside: the city's art collection, lace galleries and the Robin Hood story; underneath, Mortimer's Hole and other caves. Free grounds views over the city.",
 "Check opening and cave tour times before you go",web="https://www.nottinghamcastle.org.uk",geo="Nottingham Castle, Lenton Road")
add("sights","Park Tunnel","Derby Road entrance by Canning Circus, NG7 1",
 "A tunnel cut through the sandstone in 1855 as a carriage entrance to The Park, the private Victorian estate of grand villas below the Castle. It was never used for carriages because the slope was too steep. Now a free, atmospheric footpath with an open-air light well in the middle.",
 "Walk down from Derby Road into The Park",ta=False,geo="Park Tunnel, Nottingham",ll=(52.9530,-1.1612))
add("sights","Old Market Square & the Council House","Old Market Square, NG1 2DT",
 "The UK's second-largest civic square, overlooked by the 1929 Council House with its dome and two stone lions. 'Meet you by the left lion' is the classic local rendezvous, and gave the city's culture magazine its name. The Exchange Arcade inside the Council House has a painted dome.",
 "Christmas market and ice rink here every winter",geo="Council House, Old Market Square, Nottingham")
add("sights","Lace Market & St Mary's Church","High Pavement, NG1 1HF",
 "The medieval heart of Nottingham, rebuilt in the 1800s as a canyon of tall red-brick lace warehouses and showrooms. St Mary's is the city's oldest church, a 15th-century Perpendicular giant with fine stained glass. The Adams Building on Stoney Street was built with a chapel and library for its workers.",
 "Wander Stoney St, Broadway and St Mary's Gate",geo="St Mary's Church, High Pavement, Nottingham")
add("sights","Robin Hood statue","Castle Road, NG1 6AA",
 "The bronze outlaw by James Woodford, unveiled in 1952 below the Castle walls. His arrow has been stolen so many times it's a running joke. Every visitor gets the photo.",
 "Quick photo stop on the way to the Trip",geo="Robin Hood Statue, Castle Road, Nottingham")
add("sights","Green's Windmill","Windmill Lane, Sneinton, NG2 4QB",
 "A tower windmill in Sneinton, once owned by the mathematician George Green, whose work underpins modern physics. It has been under major repair, with the mill closed to visitors, but the small science centre tells Green's story.",
 "Repairs were due to finish in November 2026; check before you go",web="https://www.greensmill.org.uk",geo="Green's Windmill, Nottingham")
add("sights","The Arboretum","Waverley Street, NG7 4HF",
 "Nottingham's first public park, opened in 1852: a hilly Victorian garden with a pagoda, bandstand, aviary and Crimean War cannons. Quiet, free and a short walk north of the centre.",
 "Pair with Mansfield Road pubs",ta=True,geo="The Arboretum, Nottingham")
add("sights","Theatre Royal & Royal Concert Hall","Theatre Square, NG1 5ND",
 "The 1865 Theatre Royal with its six Corinthian columns, joined to the modern Royal Concert Hall. Touring West End shows, panto, comedy and big concerts. Even if you're not going in, the portico lit at night is one of the city's best sights.",
 "Panto season runs through December",web="https://trch.co.uk",geo="Theatre Royal, Theatre Square, Nottingham")
add("sights","Broadway Cinema","14–18 Broad Street, NG1 3AL",
 "The city's independent cinema in a former Methodist chapel in Hockley, showing art-house, world and classic film. Its café-bar is open to everyone and is one of Hockley's best meeting spots. A room here was designed by Paul Smith.",
 "Drop in for a drink even without a ticket",web="https://www.broadway.org.uk",geo="Broadway Cinema, Broad Street, Nottingham")
add("sights","Wollaton Hall & Deer Park","Wollaton Park, NG8 2AE",
 "A spectacular Elizabethan prodigy house, built in the 1580s, set in a 500-acre park with free-roaming red and fallow deer. It was Wayne Manor in The Dark Knight Rises. The natural history museum inside is free; parking is paid.",
 "Drive or bus 30; allow half a day",far=True,geo="Wollaton Hall, Nottingham")

# ---------------- GALLERIES ----------------
add("galleries","Nottingham Contemporary","Weekday Cross, NG1 2GB",
 "One of the UK's largest contemporary art centres, in a building wrapped in concrete panels cast from a Victorian lace pattern. Four free galleries, a strong bookshop and a café, right on the edge of the Lace Market. 2026 includes the first institutional solo show of the late British artist Sarah Cunningham.",
 "Free · closed Mondays",web="https://www.nottinghamcontemporary.org",geo="Nottingham Contemporary, Weekday Cross")
add("galleries","Surface Gallery","16 Southwell Road, NG1 1DL",
 "A volunteer-led, artist-run contemporary gallery run as a co-operative by early-career artists. Ambitious, rough-edged shows, open calls and an annual street art festival.",
 "Opens around exhibitions; check dates",web="https://www.surfacegallery.org",ta=False,geo="Surface Gallery, Southwell Road, Nottingham",ll=(52.9531,-1.1384))
add("galleries","BACKLIT","Alfred House, Ashley Street, NG3 1JG",
 "An independent artist-led space founded in 2008, with galleries across three floors of an 1872 Victorian building in Sneinton, plus studios. A new ground-floor gallery and People's Archive opened through 2026. Its 'Our Marian' sculpture now stands at Tollhouse Hill.",
 "Open during exhibitions; check online",ta=False,geo="Backlit, Alfreton Road, Nottingham",ll=(52.9577,-1.1667))
add("galleries","New Art Exchange","39–41 Gregory Boulevard, Hyson Green, NG7 6BE",
 "The UK's largest gallery dedicated to culturally diverse contemporary art, in the heart of Hyson Green. Free exhibitions, a café, and Radford Road's food shops on the doorstep.",
 "Tram to Hyson Green Market",web="https://www.nae.org.uk",far=True,geo="New Art Exchange, Gregory Boulevard, Nottingham")
add("galleries","Primary","33 Seely Road, Lenton, NG7 1NU",
 "A former Victorian primary school, now artists' studios with a public programme of exhibitions, talks and events. A real look inside the city's artist community.",
 "Best on open days and event nights",web="https://www.weareprimary.org",ta=False,geo="Primary, Seely Road, Nottingham",ll=(52.9561,-1.1798))
add("galleries","Bonington Gallery","Bonington Building, Dryden Street, NG1 4FZ",
 "Nottingham Trent University's free gallery in its brutalist art-school building. Thoughtful, often experimental contemporary exhibitions and rarely crowded.",
 "Term-time programme",ta=False,geo="Bonington Building, Dryden Street, Nottingham")
add("galleries","Fletcher Gate Fine Art Gallery","18 Fletcher Gate, Lace Market, NG1 2FZ",
 "Also known as the Fletcher Gate Art Gallery. An independent gallery for original fine art for sale, from local and national artists, in the Lace Market. A relaxed place to browse paintings you could actually take home.",
 "Thu–Sun 11:00–16:00",ta=False,geo="Fletcher Gate, Nottingham",ll=(52.9530,-1.1458))
add("galleries","Nottingham Society of Artists","61 Friar Lane, NG1 6DA",
 "Founded in 1880, the society runs its own gallery behind an unassuming door on Friar Lane. Rolling exhibitions of members' work, often very affordable.",
 "Combine with the Castle",ta=False,geo="61 Friar Lane, Nottingham")
add("galleries","Djanogly Gallery, Lakeside Arts","University Park, NG7 2RD",
 "The University of Nottingham's arts centre beside the Highfields lake, with a gallery of historic and modern shows, plus theatre and music. A lovely place for a lakeside walk.",
 "Tram to University of Nottingham",web="https://www.lakesidearts.org.uk",far=True,geo="Djanogly Art Gallery, Nottingham")
add("galleries","Hooten Street Project","Sneinton, NG3",
 "A tiny space converted from part of an artist's studio, showing print and wall-based work by invited artists. Very small and occasional, which is the charm.",
 "Check dates before you go",ta=False,geo="Sneinton Market, Nottingham",ll=(52.9548,-1.1378))
add("galleries","Debbie Bryan","1st floor, 4–6 St Peter's Gate, NG1 2JG",
 "An award-winning independent creative gallery, shop and tearoom run by a textile designer. Nottingham lace, local makers, prints and gifts, plus craft workshops you can book.",
 "Book a workshop for a creative afternoon",web="https://www.debbiebryan.co.uk",geo="Debbie Bryan, St Peter's Gate, Nottingham",ll=(52.9525,-1.1478))

# ---------------- INDIE SHOPS & MAKERS ----------------
add("shops","Sneinton Market Avenues","Avenue A–C, Sneinton Market, NG1 1DW",
 "Rows of old wholesale-market units converted into tiny shops and studios for designers, makers, florists and creative businesses, with Bustler street food in the middle. The heart of the Creative Quarter's east side.",
 "Saturdays are best · market hall refurbishment from autumn 2026",ta=False,geo="Sneinton Market Avenues, Nottingham",ll=(52.9543,-1.1393))
add("shops","Cobden Chambers","off Pelham Street, NG1 2ED",
 "A hidden courtyard off Pelham Street, home to small independent shops, makers and cafés. Easy to walk straight past the entrance.",
 "Tenants change; peek in whenever you pass",ta=False,geo="Cobden Chambers, Nottingham",ll=(52.9540,-1.1467))
add("shops","Hurts Yard","Hurts Yard, NG1 6JD",
 "A narrow Victorian alley between Upper Parliament Street and Long Row packed with independents: records, barbers, vintage, and newer food spots like Shio at Six Richmond House.",
 "Start at the Upper Parliament St end",ta=False,geo="Hurts Yard, Nottingham",ll=(52.9548,-1.1515))
add("shops","Flying Horse Walk","Poultry, NG1 2HN",
 "A shopping passage through a former 17th-century coaching inn, with timbered gables over the entrance. Small shops, 200 Degrees coffee and Bar Gigi.",
 "Good start to a shopping loop",ta=False,geo="Flying Horse Walk, Nottingham",ll=(52.9527,-1.1484))
add("shops","Bridlesmith Gate & Bridlesmith Walk","Bridlesmith Gate, NG1 2GR",
 "Nottingham's old fashion street, still lined with independent boutiques alongside designer names, plus the tucked-away Bridlesmith Walk lane of small units.",
 "Walk it towards Hockley",ta=False,geo="Bridlesmith Gate, Nottingham")
add("shops","West End Arcade","Upper Parliament Street, NG1 6JR",
 "A small arcade off Upper Parliament Street with independent fashion, gifts and cafés, near Hurts Yard and the Theatre Royal.",
 "Combine with Hurts Yard",ta=False,geo="West End Arcade, Nottingham",ll=(52.9550,-1.1532))
add("fashion","Paul Smith, Willoughby House","20 Low Pavement, NG1 7DL",
 "Sir Paul Smith is Nottingham born and opened his first tiny shop here in 1970. His flagship is a gorgeous Georgian townhouse on Low Pavement, worth seeing for the interiors and the eccentric displays.",
 "Look out for the quirky objects in the windows",web="https://www.paulsmith.com",who=["m","w"],geo="Willoughby House, Low Pavement, Nottingham",ll=(52.9508,-1.1480))
add("shops","Delilah Fine Foods","12 Victoria Street, NG1 2EX",
 "A deli in a grand old banking hall: marble counters, a mezzanine café and a huge cheese counter. Buy Nottinghamshire Stilton, charcuterie and wine to take home in the car.",
 "Ask for Colston Bassett Stilton, made in Notts",web="https://www.delilahfinefoods.co.uk",geo="Delilah Fine Foods, Victoria Street, Nottingham",ll=(52.9531,-1.1477))
add("shops","Victoria Centre Market","Victoria Centre (upper level), NG1 3QN",
 "The city's old indoor market above the shopping centre. The council began closing it in 2023 and only a handful of traders remain, so go for nostalgia rather than a full market. Rowland Emett's whimsical water clock was removed in May 2026 for refurbishment.",
 "Check what's still open before making a special trip",ta=False,geo="Victoria Centre Market, Nottingham",ll=(52.9567,-1.1474))

# ---------------- RECORDS, BOOKS & COMICS ----------------
add("records","Rough Trade Nottingham","5 Broad Street, Hockley, NG1 3AJ",
 "New vinyl, books and zines on the ground floor, with a bar and a 150-capacity live room upstairs for in-store gigs. The anchor of Hockley's music scene.",
 "In-store sets are often free; check events",web="https://www.roughtrade.com",geo="Rough Trade, Broad Street, Nottingham",ll=(52.9540,-1.1440))
add("records","Rob's Records","4–5 Hurts Yard, NG1 6JD",
 "A crate-digger's institution: crammed racks of second-hand vinyl across every genre, in the Hurts Yard alley.",
 "Check @robsrecordsnottingham for hours",ta=False,geo="Rob's Records, Hurts Yard, Nottingham",ll=(52.9549,-1.1513))
add("records","Five Leaves Bookshop","14a Long Row, NG1 2DH",
 "A radical, independent bookshop and publisher up a passage off Long Row. Strong on politics, poetry, local history, LGBTQ+ and small-press fiction, with regular author events.",
 "Their Nottingham history titles make great gifts",web="https://fiveleavesbookshop.co.uk",geo="Five Leaves Bookshop, Long Row, Nottingham",ll=(52.9538,-1.1495))
add("records","Page 45","9 Market Street, NG1 6HY",
 "An award-winning comics and graphic novel shop, with handwritten staff reviews on half the shelves. Brilliant for beginners: tell them what novels you like and let them pick.",
 "Ask for a recommendation",web="https://www.page45.com",geo="Page 45, Market Street, Nottingham",ll=(52.9540,-1.1510))

# ---------------- VINTAGE & ANTIQUES ----------------
add("vintage","Hopkinsons Vintage & Antiques","21 Station Street, NG2 3AJ",
 "A huge multi-dealer vintage, antique and retro emporium in a former warehouse opposite the railway station. Furniture, homewares, clothes, militaria and odd curios over several floors.",
 "Allow at least an hour",geo="Hopkinsons, Station Street, Nottingham",ll=(52.9476,-1.1452))
add("vintage","Derby Road antiques & vintage strip","Derby Road, NG1 5",
 "The slope from the centre up to Canning Circus is lined with antique dealers, vintage furniture, guitar shops and odd specialists. A slow browse that ends at three good pubs.",
 "Walk up, lunch at the top, stroll down",ta=False,geo="Derby Road, Nottingham",ll=(52.9543,-1.1588))
add("vintage","Cow Vintage","3 Carlton Street, Hockley, NG1 1NL",
 "A big vintage clothing store listed among the city's go-to second-hand fashion shops, with racks of denim, sportswear and retro jackets.",
 "Two floors, 1980s to early 2000s; check it's trading",ta=False,who=["m","w"],geo="Cow Vintage, Nottingham",ll=(52.9536,-1.1449))
add("vintage","Goose Gate vintage & Hockley shops","Goose Gate, Hockley, NG1 1FF",
 "Goose Gate and Carlton Street are Hockley's main browsing streets: vintage clothes, skate and streetwear, plants, tattoo parlours and bars. Boots grew from the herbalist's shop John Boot opened on Goose Gate in 1849, and his son Jesse built his first big store at 16–20 Goose Gate in the 1880s. Look up for the original ironwork.",
 "Best late morning before the bars fill",ta=False,geo="Goose Gate, Nottingham",ll=(52.9534,-1.1430))

# ---------------- CAFÉS ----------------
add("cafes","200 Degrees, Flying Horse Walk","Flying Horse Walk, NG1 2HN",
 "The Nottingham-born roaster that went national. This branch sits in the old coaching-inn arcade, and beans are roasted in the city.",
 "Buy a bag of beans to take home",price=1,web="https://200degs.com",geo="200 Degrees Flying Horse Walk, Nottingham",ll=(52.9527,-1.1482))
add("cafes","Doughnotts","14 Cheapside, NG1 2HU",
 "Nottingham's own doughnut company, started here in 2015, with its city café on Cheapside beside the Council House. Big, inventive, sourdough doughnuts with vegan options.",
 "Closed Mondays · get there before they sell out",price=1,geo="Doughnotts, Goose Gate, Nottingham",ll=(52.9535,-1.1431))
add("cafes","The Pudding Pantry","Trinity Square, NG1 4AF",
 "Over-the-top pancake stacks, brunches and cakes. Exactly what it sounds like, and very popular.",
 "Weekend queues from 10am",price=2,geo="The Pudding Pantry, Trinity Square, Nottingham",ll=(52.9572,-1.1514))
add("cafes","Debbie Bryan tearoom","1st floor, 4–6 St Peter's Gate, NG1 2JG",
 "Tea, cake and light lunches among the makers' displays at Debbie Bryan's creative shop.",
 "Combine with a craft workshop",price=1,geo="Debbie Bryan, St Peter's Gate, Nottingham",ll=(52.9525,-1.1477))
add("cafes","Malt Cross","16 St James's Street, NG1 6FG",
 "A rare surviving 1877 Victorian music hall, with a glass barrel-vaulted roof and iron balconies, now a charity-run café-bar. Coffee by day, drinks and music at night, and caves below with a small exhibition space.",
 "Ask if the caves are open to wander",price=1,web="https://www.maltcross.com",geo="Malt Cross, St James's Street, Nottingham")

# ---------------- CHEAP EATS ----------------
add("cheap","Bustler Market","Sneinton Market Avenues, NG1 1DW",
 "A big street-food hall with permanent traders, bars and 500+ seats in Sneinton Market. Something for everyone and very sociable.",
 "Busiest and best Fri–Sat evenings",price=1,geo="Bustler Market, Sneinton, Nottingham",ll=(52.9542,-1.1389))
add("cheap","Shanghai Shanghai","15 Goose Gate, Hockley, NG1 1FE",
 "Proper numbing Sichuan cooking in a no-frills Hockley dining room. A local favourite for years.",
 "Share in a group; order the dry-fried green beans",price=2,geo="Shanghai Shanghai",ll=(52.95375,-1.14312))
add("cheap","Kayal","8 Broad Street, Hockley, NG1 3AL",
 "South Indian cooking from Kerala: dosas, coconut curries and seafood. A refreshing change from the standard curry house.",
 "The lunchtime thali is excellent value",price=2,web="https://www.kayalrestaurant.com",geo="Kayal, Broad Street, Nottingham",ll=(52.9538,-1.1442))

# ---------------- MID-RANGE ----------------
add("mid","Kushi-ya","Enfield Chambers, 14a Low Pavement, NG1 7DL",
 "A small, buzzy izakaya that moved in 2024 to Enfield Chambers, reached through a gated alleyway off Low Pavement. Charcoal-grilled skewers, Japanese small plates, and strong sake and natural wine lists.",
 "Sit at the counter to watch the grill",price=3,web="https://www.kushi-ya.co.uk",geo="Kushi-ya, Cannon Court, Nottingham",ll=(52.9536,-1.1517))
add("mid","Ibérico World Tapas","The Shire Hall, High Pavement, NG1 1HN",
 "Tapas in the vaulted, tiled basement of the old Shire Hall, candlelit and romantic. Spanish classics with detours to Asia and South America.",
 "The set lunch is great value",price=3,web="https://www.ibericotapas.com",geo="Iberico World Tapas, High Pavement, Nottingham",ll=(52.9512,-1.1446))
add("mid","Bar Gigi","Flying Horse Walk, NG1 2HN",
 "A small Italian bar and kitchen in the Flying Horse Walk arcade, five years old in 2026. Aperitivo, pasta and a famously good burger.",
 "Casual lunch between shops",price=2,geo="Bar Gigi, Flying Horse Walk, Nottingham",ll=(52.9528,-1.1485))
add("mid","Sexy Mamma Love Spaghetti","3 Heathcoat Street, Hockley, NG1 3AF",
 "The name's a joke but the pasta isn't. A tiny, cosy, family-run trattoria in Hockley with fresh pasta.",
 "No bookings: walk in and expect a short wait",price=2,geo="Sexy Mamma Love Spaghetti, Nottingham",ll=(52.9542,-1.1437))
add("mid","Shio","Six Richmond House, Hurts Yard, NG1 6JD",
 "A small, well-reviewed Japanese restaurant hidden in Six Richmond House in the Hurts Yard alley of independents.",
 "New places change fast; check menu and hours",price=2,ta=False,geo="Six Richmond House, Hurts Yard, Nottingham",ll=(52.9547,-1.1514))
add("mid","Café Roya","130 Wollaton Road, Beeston, NG9 2PE",
 "A much-loved vegetarian and vegan restaurant in Beeston with Persian-influenced cooking. Worth the tram ride.",
 "Small and mostly evenings; book",price=2,far=True,geo="Cafe Roya, Wollaton Road, Beeston")

# ---------------- SPLURGE ----------------
add("splurge","Alchemilla","192 Derby Road, NG7 1NF",
 "Alex Bond's Michelin-starred restaurant, built into a long-derelict Victorian coach house with a living roof. Inventive, vegetable-led tasting menus.",
 "Book weeks ahead · 15-min walk up Derby Road",price=4,web="https://www.alchemillarestaurant.uk",geo="Alchemilla, Derby Road, Nottingham",ll=(52.9548,-1.1647))
add("splurge","Restaurant Sat Bains","Lenton Lane, NG7 2SA",
 "Nottingham's two-Michelin-star restaurant with rooms, curiously sited by the river under a flyover. One of the UK's great tasting menus; stay over and skip the drive home.",
 "Opens fewer days than it used to; book well ahead",price=4,web="https://www.restaurantsatbains.com",far=True,geo="Restaurant Sat Bains, Lenton Lane, Nottingham",ll=(52.9353,-1.1690))
add("splurge","Hart's Kitchen","Standard Hill, Park Row, NG1 6GN",
 "A long-running, grown-up brasserie by the Castle, in Hart's Hotel. Reliable, polished modern British cooking.",
 "Lovely for Sunday lunch",price=3,web="https://www.hartsnottingham.co.uk",geo="Harts Hotel, Standard Hill, Nottingham",ll=(52.9516,-1.1547))

# ---------------- PUBS ----------------
add("pubs","Ye Olde Trip to Jerusalem","1 Brewhouse Yard, NG1 6AD",
 "Painted with '1189 AD', it claims to be England's oldest inn. The back rooms are caves cut straight into the sandstone under the Castle. Find the cursed model galleon in its glass case.",
 "Weekday afternoon for a cave room",price=1,web="https://www.triptojerusalem.com",geo="Ye Olde Trip to Jerusalem, Nottingham")
add("pubs","The Bell Inn","18 Angel Row, NG1 6HL",
 "A timber-framed pub right on the Market Square with medieval cellars and caves carved into the rock beneath. Live jazz some nights.",
 "Ask about cellar tours",price=1,geo="The Bell Inn, Angel Row, Nottingham")
add("pubs","Hand & Heart","65 Derby Road, NG1 5BA",
 "An ordinary-looking frontage, but the back room is a cave carved into the sandstone cliff. Good real ales and food, and calmer than the Trip. It reopened under new owners after closing in 2022.",
 "Sit in the cave room",price=1,geo="Hand and Heart, Derby Road, Nottingham",ll=(52.9546,-1.1574))
add("pubs","Kean's Head","46 St Mary's Gate, NG1 1QA",
 "A small, friendly corner pub opposite St Mary's church in the Lace Market. Castle Rock ales and decent food.",
 "Stop between galleries",price=1,geo="Kean's Head, St Mary's Gate, Nottingham",ll=(52.9520,-1.1448))
add("pubs","The Kilpin Beer Cafe","10 Bridlesmith Walk, NG1 2HR",
 "Formerly The Herbert Kilpin, named after the Nottingham lace worker who founded AC Milan. A cosy little bar with well-kept cask ales and craft beer.",
 "Trivia to drop on your friends",price=1,geo="The Herbert Kilpin, Bridlesmith Gate, Nottingham",ll=(52.9520,-1.1474))
add("pubs","The Organ Grinder","21 Alfreton Road, Canning Circus, NG7 3JE",
 "Blue Monkey brewery's pub at Canning Circus. Unpretentious, excellent beer and the famous pork pie and cheese plates.",
 "Pair with the Borlase Warren opposite",price=1,geo="The Organ Grinder, Alfreton Road, Nottingham",ll=(52.9558,-1.1631))
add("pubs","Sir John Borlase Warren","1 Ilkeston Road, Canning Circus, NG7 3GD",
 "A rambling old pub of small rooms at the top of Derby Road, with a sun-trap beer garden.",
 "Last stop before strolling back down",price=1,geo="Sir John Borlase Warren, Ilkeston Road, Nottingham",ll=(52.9553,-1.1640))
add("pubs","The Lincolnshire Poacher","161 Mansfield Road, NG1 3FR",
 "A pilgrimage pub for beer people, a 15-minute walk up Mansfield Road. Long tap list, whisky shelf, no nonsense.",
 "Mansfield Road has more good pubs for a crawl",price=1,geo="Lincolnshire Poacher, Mansfield Road, Nottingham",ll=(52.9631,-1.1484))
add("pubs","Fox & Grapes","21 Southwell Road, Sneinton, NG1 1DL",
 "A Castle Rock pub on the edge of Sneinton Market, handy for galleries, studios and Bustler.",
 "Pair with Surface Gallery",price=1,geo="Fox and Grapes, Southwell Road, Nottingham",ll=(52.9530,-1.1388))
add("pubs","The Vat & Fiddle","12–14 Queen's Bridge Road, NG2 1NB",
 "Castle Rock brewery's own tap, next to the brewery and a few minutes from the station. Fresh ales and a proper local atmosphere.",
 "Last pint before the train",price=1,geo="Vat and Fiddle, Queensbridge Road, Nottingham",ll=(52.9459,-1.1478))
add("pubs","The Angel Microbrewery","7 Stoney Street, Lace Market, NG1 1LG",
 "A historic Lace Market pub with its own microbrewery, gigs upstairs and a slightly chaotic, friendly vibe.",
 "Check the gig listings",price=1,geo="Angel Microbrewery, Stoney Street, Nottingham",ll=(52.9532,-1.1442))

# ---------------- BARS ----------------
add("bars","The Hockley Arts Club","20A Carlton Street, Hockley, NG1 1NN",
 "A grand cocktail bar in a Grade II-listed building, dressed with art and music memorabilia. One of the city's showier nights out.",
 "Wed–Sun · lively late at weekends",price=3,geo="Hockley Arts Club, Nottingham",ll=(52.9537,-1.1436))
add("bars","Junkyard","12 Bridlesmith Walk, NG1 2HR",
 "A small, dark, serious craft beer bar with a rotating tap list and good bar food.",
 "Ask the staff for a recommendation",price=2,geo="Junkyard, Bridlesmith Walk, Nottingham",ll=(52.9524,-1.1475))
add("bars","The Canal House","48–52 Canal Street, NG1 7EH",
 "An arm of the Nottingham Canal runs right through the middle of the bar, with a footbridge over it and a canalside terrace.",
 "Sit by the water inside",price=2,geo="Canal House, Canal Street, Nottingham",ll=(52.9480,-1.1487))
add("bars","Broadway Cinema bar","14–18 Broad Street, NG1 3AL",
 "The independent cinema's café-bar, open to everyone. Full of film people and Hockley regulars.",
 "Pair with a film",price=1,web="https://www.broadway.org.uk",geo="Broadway Cinema, Broad Street, Nottingham")
add("bars","The Bodega","23 Pelham Street, NG1 2ED",
 "A pub downstairs and a small gig venue upstairs, where plenty of bands played early in their careers. A Hockley staple for a pint and a gig.",
 "Check the gig calendar",price=1,geo="The Bodega, Pelham Street, Nottingham",ll=(52.9538,-1.1462))

# ---------------- CAMERAS, MUSIC & TECH ----------------
add("gear","Wex Photo Video","103–107 Carrington Street, NG1 7FE",
 "A big camera shop near the station with a proper used counter: second-hand lenses, bodies, flashes and accessories, all with a 12-month warranty. Stock changes daily and isn't all online, so it's worth a browse in person. They'll also buy or part-exchange your old kit.",
 "Used stock is first come, first served",web="https://www.wexphotovideo.com/about-us/store-finder/nottingham/",geo="Wex Photo Video, Carrington Street, Nottingham",ll=(52.9490,-1.1459))
add("gear","Drum & Guitar","Cranbrook House, Cranbrook Street, NG1 1ES",
 "Calls itself the largest independent music store in the East Midlands. Especially strong on drums, cymbals and percussion, with guitars and amps too, and staff who know their stuff.",
 "Ask about part-exchange and any used stock",ta=False,geo="Drum and Guitar, Cranbrook Street, Nottingham",ll=(52.9536,-1.1418))
add("gear","Nottingham City Guitars","Lace Market, NG1",
 "A luthier's workshop building hand-made electric guitars, with some finished shop stock for sale. Guitars start from around £1,500. A treat for a serious player.",
 "Open by appointment only; contact them first",ta=False,geo="Lace Market, Nottingham",ll=(52.9523,-1.1440))
add("gear","CeX, Victoria Centre","Unit 310, Upper Mall, Victoria Centre, NG1 3QN",
 "The buy-sell-exchange chain for second-hand phones, laptops, tablets, cameras, consoles and games, everything graded with a warranty. Handy for a cheap spare phone or a retro console.",
 "A second branch is on Exchange Walk",ta=False,geo="Victoria Centre, Nottingham",ll=(52.9568,-1.1478))
add("gear","CeX, Exchange Walk","2 Exchange Walk, NG1 2NX",
 "The smaller central CeX, just off the Old Market Square, for second-hand tech, games and phones.",
 "Compare stock with the Victoria Centre branch",ta=False,geo="Exchange Walk, Nottingham",ll=(52.9524,-1.1497))

# ---------------- FOOD SHOPS & WORLD GROCERS ----------------
add("food","The Cheese Shop","4 Flying Horse Walk, NG1 2HN",
 "Run by brothers Rob and Webb Freckingham for more than 15 years: a counter of British and continental cheeses, charcuterie, chutneys and crackers, plus the only café in Flying Horse Walk. A past World Cheese Awards placer.",
 "Ask for Colston Bassett or Cropwell Bishop Stilton, both made in Notts",geo="The Cheese Shop, Flying Horse Walk, Nottingham",ll=(52.9528,-1.1483))
add("food","Oriental Mart","1A Goldsmith Street, NG1 5ED",
 "Nottingham's best-known East Asian supermarket, with more than 3,000 Chinese, Japanese, Korean, Thai and Vietnamese products: fresh, frozen and dried. Its Umai street-food café serves bao, ramen and Hong Kong snacks.",
 "Good for snacks you won't find anywhere else",web="https://www.orientalmart.co.uk",geo="Oriental Mart, Goldsmith Street, Nottingham",ll=(52.9567,-1.1540))
add("food","Asiana Hypermarket","108 Woodborough Road, NG3 1AR",
 "A huge Oriental supermarket on the edge of the centre, stocking foods from China, Hong Kong, Korea, Thailand, Japan, Vietnam and the Philippines, with big fresh and frozen sections.",
 "Easiest by car; it's uphill from Victoria Centre",ta=False,geo="Asiana Hypermarket, Woodborough Road, Nottingham",ll=(52.9620,-1.1420))
add("food","Radford Road world food trail","Radford Road, Hyson Green, NG7",
 "Half a mile of international grocers and bakeries where a dozen languages are spoken: South Asian and Middle Eastern spices at Medina Continental (79–83 Radford Road), exotic fruit and veg at Green Oranges, Polish bakes at Olawa Bakery and Eastern European goods at the Tani Shop. Wiloks nearby does African and Caribbean foods.",
 "Tram to Hyson Green Market; pair with New Art Exchange",ta=False,far=True,geo="Radford Road, Hyson Green, Nottingham",ll=(52.9668,-1.1702))

# ---------------- ESCAPE ROOMS & THINGS TO DO ----------------
add("fun","Cave Escape","63 Mansfield Road, NG1 3FN",
 "Escape rooms built into a real sandstone cave system under Mansfield Road, which could only be in Nottingham. Three rooms for up to 18 players at once.",
 "Book ahead, especially at weekends",geo="Cave Escape, Mansfield Road, Nottingham",ll=(52.9588,-1.1489))
add("fun","Escapologic","21–23 Castle Gate, NG1 7AQ",
 "The city's biggest escape-room venue, with 11 themed rooms across two buildings including 18+ horror games in the autumn.",
 "20% off a second room booked on the day · check hours",geo="Escapologic, Stanford Street, Nottingham",ll=(52.9512,-1.1512))
add("fun","Break Escape","9a Market Street & 107 Upper Parliament Street, NG1",
 "A family-friendly escape-room company with two city-centre sites and a Robin Hood-themed room, plus Christmas rooms in December.",
 "Cheaper tickets for children",geo="Break Escape, Market Street, Nottingham",ll=(52.9541,-1.1509))
add("fun","The Original Nottingham Ghost Walk","Starts at Ye Olde Trip to Jerusalem, NG1 6AD",
 "A costumed storyteller leads you round the Castle Quarter after dark, telling the city's ghost stories over about half a mile. Runs on Saturday evenings; the 2026 season ends on 7 December.",
 "Saturdays 7pm · £9 · about 1½–2 hours",geo="Ye Olde Trip to Jerusalem, Nottingham",ll=(52.94925,-1.15255))
add("fun","Ludorati Café","72 Maid Marian Way, NG1 6BJ",
 "A board-game café with over 750 games, from old favourites to new ones, plus coffee, food and staff who'll teach you the rules. Great on a rainy afternoon.",
 "Book a table at weekends",geo="Ludorati, Maid Marian Way, Nottingham",ll=(52.9520,-1.1530))
add("fun","The Dice Cup","68–70 Mansfield Road, NG1 3GY",
 "Nottingham's first board-game café and a proper games shop: dice, board games, tabletop miniatures and comics, with vegan-friendly food.",
 "Browse the shop even if you're not staying to play",geo="The Dice Cup, Mansfield Road, Nottingham",ll=(52.9580,-1.1485))

# ---------------- LIVE MUSIC & COMEDY ----------------
add("music","Rock City","8 Talbot Street, NG1 5GG",
 "A legendary independent rock venue since 1980, holding about 2,000 people. Just about every big guitar band of the last 40 years has played here, and its club nights are a Nottingham rite of passage.",
 "Check listings and book early for touring bands",web="https://www.rock-city.co.uk",geo="Rock City, Talbot Street, Nottingham")
add("music","Rescue Rooms","Masonic Place, off Goldsmith Street, NG1 5JT",
 "Rock City's 480-capacity little sibling next door, where you catch bands on the way up. It has a bar and kitchen, so it works for a drink even without a gig.",
 "Tickets often around £15–25",web="https://www.rescuerooms.com",geo="Rescue Rooms, Nottingham")
add("music","Metronome & the Glee Club","Huntingdon Street, NG1 1AP",
 "Nottingham Trent University's music and arts venue, now home to the Glee Club's comedy nights and Just the Tonic, plus gigs and club nights.",
 "Comedy weekends sell out; book ahead",geo="Metronome, Huntingdon Street, Nottingham",ll=(52.9567,-1.1432))
add("music","Nottingham Playhouse","Wellington Circus, NG1 5AF",
 "The city's producing theatre, with drama, its famous panto and touring work. Outside stands Anish Kapoor's Sky Mirror, a huge polished steel dish reflecting the sky, which is worth a look even if you're not seeing a show.",
 "The Sky Mirror is free to see any time",web="https://www.nottinghamplayhouse.co.uk",geo="Nottingham Playhouse, Wellington Circus")
add("pubs","Ye Olde Salutation Inn","Hounds Gate, NG1 7AA",
 "A 13th-century-founded pub with caves beneath it, and a long-standing rock and live-music haunt. A third contender in the 'oldest pub in Nottingham' argument.",
 "Ask about seeing the caves",price=1,geo="Ye Olde Salutation Inn, Nottingham")

# ---------------- PARKS & WALKS ----------------
add("parks","Victoria Embankment","Victoria Embankment, NG2",
 "A broad tree-lined promenade along the River Trent, with memorial gardens, rowing clubs and views of Trent Bridge, the cricket ground and the City Ground. Flat and easy, and best on a sunny afternoon.",
 "Tram to Meadows Embankment",ta=True,geo="Victoria Embankment Memorial Gardens, Nottingham")
add("parks","Nottingham Canal towpath","Castle Wharf, Canal Street, NG1 7EH",
 "Join the canal by the Canal House and walk west past old warehouses, narrowboats and Castle Marina. It's flat all the way, and you can carry on for an hour or more towards Beeston.",
 "Start or finish with a drink at the Canal House",ta=False,geo="Castle Wharf, Nottingham",ll=(52.9479,-1.1499))
add("parks","Highfields Park","University Boulevard, NG7 2PS",
 "A lakeside Victorian park beside the University of Nottingham, with a boating lake, a waterfall, a café and Lakeside Arts. Pair it with a walk up through the campus to the Trent Building.",
 "Tram to University of Nottingham",far=True,geo="Highfields Park, Nottingham")
add("parks","The Forest Recreation Ground","Mansfield Road, NG7",
 "A huge open green on the hill north of the centre, home to Goose Fair every October and a tram Park & Ride. Big skies and views back over the city.",
 "The Forest tram stop is right there",ta=False,geo="Forest Recreation Ground, Nottingham")
add("parks","Colwick Country Park","Mile End Road, Colwick, NG4 2DW",
 "Lakes, woods and riverside paths on the east side of the city, with a marina and plenty of birdlife. Easy circular walks.",
 "About 10 minutes' drive; paid parking",far=True,geo="Colwick Country Park")
add("parks","Attenborough Nature Reserve","Barton Lane, Attenborough, NG9 6DY",
 "Flooded gravel pits turned into a wildlife haven beside the Trent, opened by Sir David Attenborough. A floating nature centre and café, kingfishers, herons and easy level paths.",
 "Train to Attenborough station, or 20 minutes by car",far=True,geo="Attenborough Nature Centre")

# ---------------- DAY TRIPS ----------------
add("trips","Sherwood Forest & the Major Oak","Edwinstowe, NG21",
 "The heart of the old royal forest, with ancient oaks and woodland trails around the Major Oak, a giant tree held up by props and thought to be 800–1,000 years old. The visitor centre is in Edwinstowe, where legend says Robin Hood married Marian.",
 "Go early on weekends; Robin Hood Festival in August",far=True,drive="40 min",geo="Major Oak, Sherwood Forest")
add("trips","Newstead Abbey","Ravenshead, NG15 8NA",
 "Lord Byron's ancestral home: the soaring west front of a medieval priory ruin attached to a country house, set in lakes, gardens and parkland with peacocks.",
 "Gardens daily · house weekends & school holidays 11–4",web="https://newsteadabbey.org.uk",far=True,drive="25 min",geo="Newstead Abbey")
add("trips","Southwell","Southwell, NG25",
 "A small Georgian minster town. The Norman Minster's chapter house has the famous 'Leaves of Southwell' stone carvings, and the National Trust Workhouse shows Victorian poor-relief. There are good independent shops and tearooms, and the Bramley apple started here.",
 "Pair the Minster and Workhouse with lunch in town",far=True,drive="35 min",geo="Southwell Minster")
add("trips","Creswell Crags","Crags Road, Welbeck, S80 3LH",
 "A limestone gorge of caves holding the UK's only known Ice Age cave art, plus hundreds of 'witches' marks' scratched to ward off evil. Guided cave tours, a lakeside walk and a visitor centre.",
 "Cave tours are guided; no under-5s on tours",far=True,drive="45 min",geo="Creswell Crags")
add("trips","Clumber Park","Worksop, S80 3BX",
 "National Trust parkland with a big serpentine lake, a Gothic chapel, one of the longest double avenues of lime trees in Europe and a beautiful walled kitchen garden. Bikes to hire.",
 "Great for a long walk or a bike ride",far=True,drive="40 min",geo="Clumber Park")
add("trips","Hardwick Hall","Doe Lea, Chesterfield, S44 5QJ",
 "Bess of Hardwick's dazzling Elizabethan house, famous as 'more glass than wall', with huge tapestries and her initials on the rooftop. The ruined Old Hall stands next door.",
 "Just off M1 junction 29",far=True,drive="35 min",geo="Hardwick Hall")
add("trips","Ruddington","Ruddington, NG11",
 "A village with the Framework Knitters Museum (working Victorian knitting frames in original workshops), the Great Central Railway heritage steam and diesel line, and Debbie Bryan's second shop.",
 "Check the railway's running days",far=True,drive="15 min",geo="Framework Knitters Museum, Ruddington")
add("trips","Colston Bassett Dairy","Harby Lane, Colston Bassett, NG12",
 "One of only a handful of dairies allowed to make Stilton, still making it by hand. Its small shop sells Stilton and Shropshire Blue straight from the source, in Vale of Belvoir countryside.",
 "Shop hours are short: weekdays & Saturday mornings",far=True,drive="25 min",geo="Colston Bassett Dairy")
add("trips","Belvoir Castle","Grantham, NG32 1PE",
 "The Duke of Rutland's romantic hilltop castle overlooking the Vale of Belvoir, with lavish state rooms and landscaped gardens. Pair it with the Colston Bassett dairy shop on the way.",
 "Opening is seasonal; check dates before you go",far=True,drive="40 min",geo="Belvoir Castle")

# ---------------- MORE GALLERIES ----------------
add("galleries","George Thornton Art","12A Flying Horse Walk, NG1 2HN",
 "An independent contemporary gallery in the Flying Horse Walk arcade, championing original, thought-provoking paintings and sculpture by living artists. Offers the Own Art interest-free scheme.",
 "Easy to combine with The Cheese Shop next door",geo="George Thornton Art, Flying Horse Walk",ll=(52.952789,-1.148546))
add("galleries","Lauren Paige Art Gallery & Writing Bureau","211 Mansfield Road, NG1 3FS",
 "A one-artist gallery in a Victorian terrace at the Huntingdon Street junction, selling Lauren Paige's original paintings and limited-edition prints, with a writing bureau alongside.",
 "Free 2-hour parking on North Sherwood Street behind",ta=False,geo="Lauren Paige Fine Art Gallery",ll=(52.963289,-1.151988))
add("galleries","PSpowage Art Gallery","185 Mansfield Road, NG1 3FS",
 "Artist Pete Spowage's gallery and studio, showing his own work and local artists. It moved here from Byard Lane in 2020 and was then open by appointment.",
 "Check first: by appointment and may have moved",ta=False,geo="185 Mansfield Road",ll=(52.962751,-1.15166))
add("galleries","Castle Fine Art","8–10 Exchange Arcade, NG1 2DD",
 "A large commercial gallery inside the Council House's Exchange Arcade, part of a national chain selling original works and limited editions by well-known contemporary and celebrity artists. Good for browsing big names.",
 "Chain gallery; staff are happy for you to browse",ta=False,geo="Castle Fine Art",ll=(52.953299,-1.148418))
add("galleries","Aura Fine Art","23 Bridlesmith Gate, NG1 2GR",
 "A commercial gallery on Bridlesmith Gate selling originals and limited editions for homes and offices, part of a small chain with branches in Hertfordshire and Guildford. Offers home consultations and flexible payment.",
 "Chain gallery · around 9:30–17:30",ta=False,geo="Aura Fine Art",ll=(52.95234,-1.14707))
add("galleries","The Harley Gallery, Welbeck","Welbeck, Worksop, S80 3LW",
 "A major contemporary art and craft gallery on the Welbeck estate, with the Portland Collection of treasures from the Dukes of Portland. The Harley Open exhibition runs until 3 January 2027. Pair it with Creswell Crags, ten minutes away.",
 "Free entry to the gallery; café and estate shops",far=True,drive="45 min",geo="Harley Gallery",ll=(53.262015,-1.178983))

# ---------------- CLOTHES & BOUTIQUES ----------------
add("fashion","Gigi Bottega","15 Flying Horse Walk, NG1 2HN",
 "An independent luxury boutique run by mother and daughter Debra and Gabriella Trivigno, with high-end and contemporary designer labels for men and women. It has a cult following.",
 "Treat yourself, or just browse",who=["m","w"],geo="Gigi Bottega",ll=(52.95308,-1.148549))
add("fashion","Tutu Urban Boutique","Exchange Arcade, NG1 2DD",
 "A multi-brand independent womenswear boutique, trading in Nottingham since 1989 and now in the Council House's Exchange Arcade.",
 "Tue–Sat 10:00–17:00",ta=False,who=["w"],geo="Tutu, Exchange Arcade",ll=(52.9534,-1.148762))
add("fashion","Flannels","11–13 Lister Gate, NG1 7DE",
 "Frasers Group's luxury multi-brand store, the kind you only find in big cities: Stone Island, Moncler, Gucci, Off-White and more for men, women and children.",
 "Opened 2023 in the old River Island building",who=["m","w","k"],geo="Flannels, Lister Gate",ll=(52.951152,-1.148471))
add("fashion","John Lewis","Victoria Centre, Milton Street, NG1 3QA",
 "One of the big John Lewis department stores, which have closed in several smaller cities. Fashion for everyone including children, plus home, beauty and tech.",
 "Good café upstairs",who=["m","w","k"],geo="John Lewis Nottingham",ll=(52.956066,-1.147674))
add("fashion","Urban Outfitters","Victoria Centre, Milton Street, NG1 3QL",
 "The big-city lifestyle chain: streetwear, its own vintage line, homewares, vinyl and gifts.",
 "Check the Urban Renewal vintage rail",ta=False,who=["m","w"],geo="Urban Outfitters Nottingham",ll=(52.95536,-1.147363))
add("fashion","Lucy & Yak","11 The Poultry, moving to 29 Bridlesmith Gate, NG1",
 "The bright, sustainably made dungarees brand, mostly womenswear with lots of unisex pieces. It's moving in late 2026 to a bigger Bridlesmith Gate shop with its Re:Yak repair and pre-loved range.",
 "Check which address is open when you visit",ta=False,who=["w","m"],geo="Lucy & Yak Nottingham",ll=(52.953082,-1.147583))
add("fashion","Metro Fashion","Middle Pavement, NG1",
 "A discount designer shop selling new, discontinued and pre-loved designer clothing for men, women and children at a fraction of retail price.",
 "Stock changes constantly; check it's still trading",ta=False,who=["m","w","k"],geo="Middle Pavement Nottingham",ll=(52.9515,-1.14632))

# ---------------- VINTAGE (clothes) ----------------
add("vintage","Glass Onion","Bridlesmith Gate, NG1 2GQ",
 "A big vintage clothing emporium from Yorkshire that opened in Nottingham in 2025 after success in Leeds and Sheffield: rails of graded vintage for men and women.",
 "A good first stop on a Bridlesmith Gate vintage crawl",ta=False,who=["m","w"],geo="Glass Onion Nottingham",ll=(52.951678,-1.147133))
add("vintage","101 Vintage","15 Bridlesmith Gate, NG1 2GR",
 "A unisex vintage store focused on American 1990s and Y2K fashion, hand-picked and restocked daily, with around 800 items.",
 "Check it's trading; it was on the street as of 2021",ta=False,who=["m","w"],geo="15 Bridlesmith Gate",ll=(52.95245,-1.14720))
add("vintage","White Rose","26a Long Row, NG1 2DR",
 "A Nottingham-grown recycled fashion chain with around eight local shops, selling pre-loved designer and branded clothing at bargain prices.",
 "Another branch is in the Victoria Centre",ta=False,who=["m","w"],geo="White Rose WR7",ll=(52.953752,-1.149683))

# ---------------- CHARITY SHOPS ----------------
add("charity","Oxfam Books & Music","19 Market Street, NG1 6HX",
 "Oxfam's specialist shop for second-hand books, vinyl, CDs, DVDs and sheet music, sorted by volunteers who know their stuff. The best charity shop in the centre for records and music.",
 "Another Oxfam Books & Music is in West Bridgford",ta=False,geo="Oxfam Books & Music, Market Street",ll=(52.954423,-1.151512))
add("charity","British Heart Foundation, Clumber Street","12–14 Clumber Street, NG1 3GA",
 "A big central BHF shop with a vintage section, plus clothes for men, women and children, books, toys and homewares.",
 "Open Sundays 11:00–17:00",ta=False,who=["m","w","k"],geo="British Heart Foundation, Clumber Street",ll=(52.954094,-1.147371))
add("charity","BHF Furniture & Electrical, Bulwell","Main Street, Bulwell, NG6",
 "The British Heart Foundation's furniture and electrical store: second-hand sofas, tables, wardrobes and tested home appliances and electricals at charity prices, with delivery available.",
 "Drive or tram to Bulwell; weekday and Saturday hours",ta=False,far=True,drive="20 min",geo="British Heart Foundation Bulwell",ll=(53.00193,-1.196076))
add("charity","Headway Charity Shop, Mapperley","23A Plains Road, Mapperley, NG3",
 "A small brain-injury charity shop with a well-known vinyl section, where volunteers sort, grade and clean the records. A favourite of local crate-diggers.",
 "Worth a detour for record collectors",ta=False,far=True,drive="15 min",geo="Headway Mapperley",ll=(52.984582,-1.121469))

# ---------------- ANTIQUES FAIR (day trip) ----------------
add("trips","Newark International Antiques & Collectors Fair","Newark Showground, Lincoln Road, NG24 2NY",
 "One of Europe's biggest antiques fairs: thousands of stalls across the Newark showground several times a year. There's also a smaller one-day 'Runway Monday' fair. The town of Newark has its own antiques centres and a castle too.",
 "2026: Runway Monday 23 Nov; next main fair 10–11 Dec (check)",far=True,drive="35 min",geo="Newark Showground",ll=(53.098808,-0.767005))

# ---------------- REVIEW ADDITIONS (Nov 2026) ----------------
add("gear","London Camera Exchange","7 Pelham Street, NG1 2EH",
 "A camera dealer with a constantly changing used counter: film and digital bodies and lenses, often serviced, plus part-exchange. A good second stop after Wex.",
 "Browse the used stock on lcegroup.co.uk and reserve before you travel",web="https://www.lcegroup.co.uk",geo="London Camera Exchange, Pelham Street, Nottingham")
add("gear","Make It Easy Lab","18 Queen's Bridge Road, NG2 1NB",
 "A film-photography lab and darkroom offering developing, darkroom hire and courses from beginner film to wet-plate collodion. The hub of Nottingham's analogue scene.",
 "Workshop-based; check sessions and drop-off times first",ta=False,geo="Make It Easy, Queens Bridge Road, Nottingham",ll=(52.9455,-1.1481))
add("charity","Sue Ryder Superstore, Clifton","Clifton Triangle, Green Lane, NG11 9LN",
 "A retail-park charity superstore full of donated furniture, electricals, books and clothes, plus new homeware. The biggest charity shop near the city for furniture.",
 "Mon–Fri 9:30–16:30 only; take the car",ta=False,far=True,drive="15 min",who=["m","w","k"],geo="Sue Ryder, Clifton Triangle, Nottingham")
add("food","Small Food Bakery","Primary, 33 Seely Road, NG7 1NU",
 "A slow-fermentation sourdough and pastry bakery inside the Primary arts building, named one of Britain's top 50 bakeries by the Good Food Guide in January 2026.",
 "Thu–Sat 9:30–16:00; the custard doughnuts sell out. Pair with Primary",geo="Small Food Bakery, Nottingham",ll=(52.95531,-1.16770))
add("food","Murat Food Centre","30–40 Bath Street, Sneinton, NG1 1DF",
 "A big Turkish-run international supermarket with Turkish, Polish and South Asian groceries, fresh bread, olives and a halal butcher, beside Sneinton Market.",
 "Check it's trading at this address before a special trip",ta=False,geo="Murat, Bath Street, Nottingham",ll=(52.9551,-1.1395))
add("fun","Warhammer World","Willow Road, Lenton, NG7 2WS",
 "Games Workshop's global headquarters visitor centre: a miniatures exhibition hall, huge gaming tables, a store with exclusives, and the Bugman's Bar pub. Only in Nottingham.",
 "The exhibition is ticketed · late opening on Thursdays",web="https://warhammerworld.warhammer-community.com",far=True,geo="Warhammer World, Willow Road, Nottingham")
add("fun","NQ64","10 Thurland Street, NG1 3DR",
 "A retro arcade bar in the old Roxy Ballroom, with 30-plus arcade cabinets, pinball, dance mats and consoles, plus game-themed cocktails.",
 "Free play in the day at weekends; busy late",web="https://nq64.co.uk/nottingham",geo="NQ64, Thurland Street, Nottingham")
add("fun","National Ice Centre public skating","Bolero Square, NG1 1LA",
 "Public skating on an Olympic-size rink in the Lace Market, at the home of British ice skating where Torvill and Dean's Bolero is celebrated. Festive sessions run in December.",
 "Book sessions online",web="https://www.national-ice-centre.com",geo="National Ice Centre, Nottingham")
add("fun","Winter Wonderland (seasonal)","Old Market Square, NG1 2DT",
 "The Christmas market fills the Old Market Square, with an ice rink, Observation Wheel and Ice Bar. Entry is free and the rides are ticketed. Runs 12 November to 31 December 2026, with stalls until 24 December.",
 "Weekday daytimes are far quieter",ta=False,geo="Old Market Square, Nottingham",ll=(52.95300,-1.14960))
add("music","JT Soar","2 Aberdeen Street, Sneinton, NG3 1JB",
 "A volunteer-run DIY venue and recording studio in an old warehouse, booking touring UK and US underground punk, indie and noise bands.",
 "Tickets around £10 · small and informal",ta=False,geo="JT Soar, Aberdeen Street, Nottingham")
add("music","Albert Hall","North Circus Street, NG1 5AA",
 "A grand Victorian hall with a famous organ, used for seated gigs, touring bands, comedy and candlelit concerts.",
 "Balcony seats have the best sound",web="https://www.alberthallnottingham.co.uk",geo="Albert Hall, North Circus Street, Nottingham")
add("mid","Piccalilli","1a Cannon Court, off Long Row West, NG1 6JE",
 "A Michelin Bib Gourmand small-plates restaurant up a staircase in a rustic old building, with a seasonal modern British menu. Excellent value for the quality.",
 "Thu–Sun only; book ahead",price=2,geo="Piccalilli, Cannon Court, Nottingham",ll=(52.9536,-1.1517))
add("mid","Little Brickhouse","110 Derby Road, NG1 5FB",
 "A cosy neighbourhood bistro and natural-wine bar with French and Scandinavian-leaning sharing plates, picked by the Good Food Guide as a Best Local Restaurant.",
 "Fits neatly into a Derby Road antiques browse",price=2,web="https://www.littlebrickhouse.co.uk",geo="Little Brickhouse, Derby Road, Nottingham")
add("mid","Pici","17 Broad Street, Hockley, NG1 3AJ",
 "Fresh handmade pasta in a small Hockley dining room, the Good Food Guide's Italian pick for the city.",
 "Closed Mondays; book at weekends",price=2,geo="Pici, Broad Street, Nottingham")
add("cheap","Everyday People","12 Byard Lane, NG1 2GJ",
 "MasterChef finalist Pete Hewitt's ramen and small-plates bar, which calls itself the city's first ramen shop.",
 "Go for the tonkotsu",price=2,geo="Everyday People, Byard Lane, Nottingham")
add("cafes","Effy","20A Heathcoat Street, NG1 3AA",
 "A pink, design-led specialty coffee shop with its own pastries, regularly ranked among the city's best cafés.",
 "Near Hockley; arrive early for the pastries",price=1,geo="Effy, Heathcoat Street, Nottingham")
add("pubs","The Barrel Drop","7 Hurts Yard, NG1 6JD",
 "A tiny two-level micropub run with Magpie Brewery, with five changing cask beers and no TV or music, just conversation.",
 "Steep curved steps with no handrail",price=1,geo="Barrel Drop, Hurts Yard, Nottingham")
add("fashion","Universal Works","120–122 Derby Road, NG1 5FB",
 "The flagship of the Nottingham-born menswear label known nationally for workwear-inspired jackets and knitwear, which is hard to find in shops outside London.",
 "Mon–Sat 10:00–18:00",web="https://universalworks.co.uk",who=["m"],geo="Universal Works, Derby Road, Nottingham")
add("parks","Bestwood Country Park & Winding Engine House","Bestwood Lodge Drive, Arnold, NG5 8NE",
 "650 acres of woods and lakes around a preserved 1873 colliery winding-engine house.",
 "The engine house opens on Saturday mornings · free parking",far=True,drive="20 min",geo="Bestwood Winding House")
add("parks","Rushcliffe Country Park","Mere Way, Ruddington, NG11 6JS",
 "Former colliery land turned into meadows, woodland paths and a lake, with a lakeside café. Pairs with a Ruddington day out.",
 "Parking about £3",far=True,drive="20 min",geo="Rushcliffe Country Park")
add("trips","Calke Abbey","Ticknall, Derbyshire, DE73 7JF",
 "The National Trust's 'un-stately home', left as it was found after its reclusive family's decline, with tunnels, crumbling rooms and an ancient deer park.",
 "Christmas opening daily 27 Nov–23 Dec 2026",web="https://www.nationaltrust.org.uk/visit/peak-district-derbyshire/calke-abbey",far=True,drive="35 min",geo="Calke Abbey")
add("trips","Chatsworth","Bakewell, Derbyshire, DE45 1PP",
 "The Duke of Devonshire's Peak District palace, with a vast garden and a superb art collection. Christmas at Chatsworth runs 7 November 2026 to 3 January 2027, with the Christmas market until 13 December.",
 "Booking needed at Christmas; add Bakewell",web="https://www.chatsworth.org",far=True,drive="1 hr 5 min",geo="Chatsworth House")
add("trips","Lincoln","Castle Square, Lincoln, LN1 3AA",
 "A hilltop cathedral city: the castle holds an original Magna Carta, the cathedral is one of England's finest, and steep Steep Hill is lined with independent shops. The cathedral holds a ticketed Christmas market on 3–5 December 2026.",
 "Park at the top of the hill and walk down Steep Hill",far=True,drive="55 min",geo="Lincoln Castle")

# ---------------- CINEMA ----------------
add("sights","Savoy Cinema","233 Derby Road, Lenton, NG7 1QN",
 "Nottingham's oldest working cinema, opened in 1935 and the city's only surviving pre-war picture house. It shows new releases and NT Live screenings, and you can book a two-person booth.",
 "Cheap tickets compared with the multiplexes · a walk up Derby Road",web="https://www.savoycinemas.co.uk",geo="Savoy Cinema, Derby Road, Nottingham")

# ---------------- MUSEUMS ----------------
add("museums","Museum of Nottingham Life at Brewhouse Yard","Castle Boulevard, NG7 1FB",
 "A row of 17th-century cottages built against Castle Rock, recreating Nottingham homes and shops through the centuries, with caves cut into the rock behind. Right next to the Trip to Jerusalem.",
 "Check first: listed as weekends 12:00–15:00, but some sources say temporarily closed",ta=True,geo="Museum of Nottingham Life at Brewhouse Yard")
add("museums","Nottingham Industrial Museum","Courtyard Buildings, Wollaton Park, NG8 2AE",
 "Volunteer-run collection in Wollaton Hall's 18th-century stable block, covering lace machines, bicycles, telephones and a working beam engine. On 'steaming Sundays' the engines run under steam.",
 "Thu–Sun 11–4 · steaming Sunday 29 Nov 2026 (£6 adults)",web="https://nottinghamindustrialmuseum.org.uk",far=True,geo="Nottingham Industrial Museum")
add("museums","D.H. Lawrence Birthplace Museum","8a Victoria Street, Eastwood, NG16 3AW",
 "The small terraced miner's house where D.H. Lawrence was born in 1885, furnished as it would have been, with changing exhibitions. Eastwood is the 'Bestwood' of Sons and Lovers.",
 "Thu–Sat 10:00–16:00",web="https://www.broxtowe.gov.uk/dhlawrencemuseum",far=True,drive="25 min",geo="D.H. Lawrence Birthplace Museum")
add("museums","National Holocaust Centre and Museum","Acre Edge Road, Laxton, NG22 0PA",
 "Britain's only dedicated Holocaust museum, in quiet countryside, with a Jewish refugee children's exhibition, memorial gardens and survivor testimony events. Moving and very well done.",
 "Hours vary between listings; check before you go",far=True,drive="35 min",geo="National Holocaust Centre")

# ---------------- SPORT ----------------
add("sport","Trent Bridge","Bridgford Road, West Bridgford, NG2 6AG",
 "One of the world's great Test cricket grounds, home of Nottinghamshire since 1841, with a heritage centre and a famous pavilion. The season runs April to September.",
 "Guided tours Tuesdays 14:00 · Heritage Open Days free visits in September",web="https://www.trentbridge.co.uk",far=True,geo="Trent Bridge Cricket Ground")
add("sport","The City Ground (Nottingham Forest)","Pavilion Road, NG2 5FJ",
 "Home of the twice European Cup-winning club, on the banks of the Trent. Museum and stadium tours run on selected non-match days, including legends tours led by former players.",
 "Book tours via the club; match tickets are scarce",far=True,geo="City Ground, Nottingham")
add("sport","Meadow Lane (Notts County)","Meadow Lane, NG2 3HJ",
 "Home of Notts County, founded in 1862 and the oldest professional football league club in the world. Match tickets are far easier to get than at Forest across the river.",
 "A ten-minute walk from the station",far=True,geo="Meadow Lane Stadium, Nottingham")
add("sport","Nottingham Panthers ice hockey","Motorpoint Arena, Bolero Square, NG1 1LA",
 "The city's Elite League ice hockey team plays in a big, loud arena in the Lace Market. A brilliant night out even if you've never watched a game. Next home game I found: Friday 27 November 2026 against Dundee Stars.",
 "Match tickets about £11–27; season tickets sold out",web="https://www.panthers.co.uk",geo="Motorpoint Arena Nottingham")
add("sport","National Water Sports Centre","Adbolton Lane, Holme Pierrepont, NG12 2LU",
 "An Olympic-standard rowing lake and white-water course beside the Trent, where you can try white-water rafting, paddleboarding and more. The surrounding country park is good for walks.",
 "Book activities in advance; 15 min drive",web="https://www.nwscnotts.com",far=True,drive="15 min",geo="National Water Sports Centre, Holme Pierrepont")

# ---------------- MARKETS ----------------
add("markets","West Bridgford Farmers' Market","Central Avenue (Croquet Lawn), West Bridgford, NG2",
 "A proper farmers' market with local meat, cheese, bread, veg and street food, in West Bridgford's lively main street of independent cafés and shops.",
 "2nd & 4th Saturdays from 8am · next: Sat 28 Nov and Sat 12 Dec",far=True,drive="15 min",geo="Central Avenue, West Bridgford")
add("markets","Sneinton Market weekend markets","Sneinton Market, Bath Street, NG1 1DW",
 "Sneinton Market is liveliest from Friday to Sunday, with regular food markets, makers' and vintage markets and seasonal events among the studio shops and Bustler street food.",
 "Check the Sneinton Market Avenues listings for this weekend's market",ta=False,geo="Sneinton Market, Nottingham",ll=(52.95474,-1.13791))
