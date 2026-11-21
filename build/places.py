# Source data for the Nottingham guide. geo = geocoder query; ll = fallback/override coordinates.
CATS = {
 "sights":   {"sec":"see","title":"Sights & oddities","emoji":"🏰","color":"#C0392B"},
 "galleries":{"sec":"see","title":"Galleries","emoji":"🎨","color":"#8E44C9"},
 "shops":    {"sec":"see","title":"Indie shops & makers","emoji":"🛍️","color":"#E8930C"},
 "records":  {"sec":"see","title":"Records, books & comics","emoji":"📀","color":"#1877D0"},
 "vintage":  {"sec":"see","title":"Vintage & antiques","emoji":"🧥","color":"#0F766E"},
 "cafes":    {"sec":"eat","title":"Cafés & coffee","emoji":"☕","color":"#0F9D8A"},
 "cheap":    {"sec":"eat","title":"Cheap eats & street food","emoji":"🌮","color":"#E8483B"},
 "mid":      {"sec":"eat","title":"Mid-range","emoji":"🍽️","color":"#E8930C"},
 "splurge":  {"sec":"eat","title":"Splurge & Michelin","emoji":"⭐","color":"#8E44C9"},
 "pubs":     {"sec":"eat","title":"Historic & real-ale pubs","emoji":"🍺","color":"#A0522D"},
 "bars":     {"sec":"eat","title":"Cocktails & craft bars","emoji":"🍸","color":"#1877D0"},
}

P = []
def add(cat, name, addr, text, tip, price=0, web="", ta=True, far=False, geo=None, ll=None):
    P.append(dict(cat=cat, name=name, addr=addr, text=text, tip=tip, price=price, web=web, ta=ta, far=far,
                  geo=geo or f"{name}, Nottingham", ll=ll))

# ---------------- SIGHTS & ODDITIES ----------------
add("sights","City of Caves","Upper Level, Broadmarsh, NG1 7LS",
 "Nottingham sits on soft sandstone riddled with more than 800 man-made caves. This guided tour takes you through medieval tannery pits, a WWII air-raid shelter and Victorian slum cellars right under the city centre. Tours run about every 30–45 minutes and take around an hour.",
 "Book a timed slot online at weekends",web="https://www.cityofcaves.com",ll=(52.9500,-1.1474),geo="City of Caves, Nottingham")
add("sights","National Justice Museum","Shire Hall, High Pavement, NG1 1HN",
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
 "A working tower windmill in Sneinton, once owned by the mathematician George Green, whose work underpins modern physics. You can buy stoneground flour milled on site and learn about Green in the small science centre.",
 "Open limited days; check before you go",web="https://www.greensmill.org.uk",geo="Green's Windmill, Nottingham")
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
add("galleries","Fletcher Gate Fine Art","Fletcher Gate, Lace Market, NG1 2FZ",
 "An independent gallery focused on original fine art for sale, from local and national artists, in the Lace Market. A relaxed place to browse paintings you could actually take home.",
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
add("shops","Paul Smith, Willoughby House","20 Low Pavement, NG1 7DL",
 "Sir Paul Smith is Nottingham born and opened his first tiny shop here in 1970. His flagship is a gorgeous Georgian townhouse on Low Pavement, worth seeing for the interiors and the eccentric displays.",
 "Look out for the quirky objects in the windows",web="https://www.paulsmith.com",geo="Willoughby House, Low Pavement, Nottingham",ll=(52.9508,-1.1480))
add("shops","Delilah Fine Foods","12 Victoria Street, NG1 2EX",
 "A deli in a grand old banking hall: marble counters, a mezzanine café and a huge cheese counter. Buy Nottinghamshire Stilton, charcuterie and wine to take home in the car.",
 "Ask for Colston Bassett Stilton, made in Notts",web="https://www.delilahfinefoods.co.uk",geo="Delilah Fine Foods, Victoria Street, Nottingham",ll=(52.9531,-1.1477))
add("shops","Victoria Centre Market","Victoria Centre (upper level), NG1 3QN",
 "An old-school indoor market above the shopping centre: fishmongers, butchers, bric-a-brac, sewing supplies and cafés. Downstairs, don't miss Rowland Emett's whimsical water clock.",
 "Emett clock performs on the hour",ta=False,geo="Victoria Centre Market, Nottingham",ll=(52.9567,-1.1474))

# ---------------- RECORDS, BOOKS & COMICS ----------------
add("records","Rough Trade Nottingham","5 Broad Street, Hockley, NG1 3AJ",
 "Two floors of new vinyl, books and zines, plus a café-bar and a small venue for in-store gigs. The anchor of Hockley's music scene.",
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
 "Several Hockley vintage shops have closed recently; check it's trading",ta=False,geo="Cow Vintage, Nottingham",ll=(52.9536,-1.1449))
add("vintage","Goose Gate vintage & Hockley shops","Goose Gate, Hockley, NG1 1FF",
 "Goose Gate and Carlton Street are Hockley's main browsing streets: vintage clothes, skate and streetwear, plants, tattoo parlours and bars. Jesse Boot opened his first shop at 16 Goose Gate; look up for the original ironwork.",
 "Best late morning before the bars fill",ta=False,geo="Goose Gate, Nottingham",ll=(52.9534,-1.1430))

# ---------------- CAFÉS ----------------
add("cafes","200 Degrees, Flying Horse Walk","Flying Horse Walk, NG1 2HN",
 "The Nottingham-born roaster that went national. This branch sits in the old coaching-inn arcade, and beans are roasted in the city.",
 "Buy a bag of beans to take home",price=1,web="https://200degs.com",geo="200 Degrees Flying Horse Walk, Nottingham",ll=(52.9527,-1.1482))
add("cafes","Doughnotts","Exchange Arcade, NG1 2DD",
 "Nottingham's own doughnut company, started here in 2015, with its city café in the Council House's Exchange Arcade. Big, inventive, sourdough doughnuts with vegan options.",
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
add("cheap","Annie's Burger Shack","5 Broadway, Lace Market, NG1 1PR",
 "Enormous menu of American burgers, many with vegan versions, plus a great craft-beer fridge. A Lace Market institution.",
 "Check it's open: listings conflict",price=2,web="https://www.anniesburgershack.com",geo="Annie's Burger Shack, Broadway, Nottingham",ll=(52.9527,-1.1444))
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
add("mid","Sexy Mamma Love Spaghetti","3 Heathcoat Street, Hockley, NG1 3AA",
 "The name's a joke but the pasta isn't. A tiny, cosy, family-run trattoria in Hockley with fresh pasta.",
 "Tiny room; book even midweek",price=2,geo="Sexy Mamma Love Spaghetti, Nottingham",ll=(52.9542,-1.1437))
add("mid","Shio","Six Richmond House, Hurts Yard, NG1 6JD",
 "One of 2026's notable new openings, in the Hurts Yard alley of independents.",
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
 "An ordinary-looking frontage, but the back room is a cave carved into the sandstone cliff. Good real ales and food; quieter than the Trip.",
 "Sit in the cave room",price=1,geo="Hand and Heart, Derby Road, Nottingham",ll=(52.9546,-1.1574))
add("pubs","Kean's Head","46 St Mary's Gate, NG1 1QA",
 "A small, friendly corner pub opposite St Mary's church in the Lace Market. Castle Rock ales and decent food.",
 "Stop between galleries",price=1,geo="Kean's Head, St Mary's Gate, Nottingham",ll=(52.9520,-1.1448))
add("pubs","The Herbert Kilpin","4 Bridlesmith Gate, NG1 2GR",
 "Named after the Nottingham lace worker who founded AC Milan. Cosy, small, well-kept ales and good pies.",
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
