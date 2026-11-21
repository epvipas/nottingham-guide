import json,time,urllib.request,urllib.parse
qs={"Nottingham Castle":["Nottingham Castle Museum","Ducal Palace Nottingham"],
"Robin Hood statue":["Robin Hood statue","Statue of Robin Hood"],
"BACKLIT":["Backlit Gallery","Backlit"],"Primary":["Primary, Seely Road","Seely Road"],
"Bonington Gallery":["Bonington Building","Bonington Gallery"],
"Djanogly Gallery, Lakeside Arts":["Lakeside Arts","Djanogly Recital Hall","Djanogly Art Gallery"],
"Debbie Bryan":["Debbie Bryan","St Peter's Gate"],"Sneinton Market Avenues":["Sneinton Market","Avenue C"],
"Delilah Fine Foods":["Delilah","Delilah Fine Foods"],"Rob's Records":["Robs Records","Rob's Records"],
"Hopkinsons Vintage & Antiques":["Hopkinsons","21 Station Street"],"Cow Vintage":["Cow","Cow Vintage"],
"Cartwheel Coffee":["Cartwheel","Cartwheel Coffee"],"Doughnotts":["Doughnotts","Doughnotts Goose Gate"],
"Annie's Burger Shack":["Annie's Burger Shack","Annies Burger Shack"],"Shanghai Shanghai":["Shanghai Shanghai","15 Goldsmith Street"],
"Kushi-ya":["Kushi-ya","Kushiya","Cannon Court"],"Ibérico World Tapas":["Iberico","Iberico World Tapas","Shire Hall"],
"The Larder on Goosegate":["The Larder on Goosegate","Larder on Goosegate","16 Goose Gate"],"MemSaab":["MemSaab","Memsaab"],
"Hart's Kitchen":["Hart's Hotel","Harts","Hart's"],"The Herbert Kilpin":["Herbert Kilpin","The Herbert Kilpin"],
"Fox & Grapes":["Fox and Grapes","Fox & Grapes"],"The Vat & Fiddle":["Vat and Fiddle","Vat & Fiddle","Castle Rock Brewery"],
"Boilermaker":["Boilermaker"],"The Canal House":["The Canal House","Canal House"],"Shio":["Shio","Richmond House"],
"Derby Road antiques & vintage strip":["Derby Road, The Park"]}
out={}
for n,ql in qs.items():
  res=[]
  for q in ql:
    u="https://nominatim.openstreetmap.org/search?"+urllib.parse.urlencode({"q":q,"format":"json","limit":3,"viewbox":"-1.30,53.02,-1.05,52.88","bounded":1})
    try: r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"nottingham-guide-builder/1.0"}),timeout=20))
    except Exception as e: r=[]
    time.sleep(1.1)
    res+= [(q,float(x['lat']),float(x['lon']),x['class'],x['type'],x['display_name'][:80]) for x in r]
    if r: break
  out[n]=res
  print(n); [print("   ",x) for x in res[:3]]
json.dump(out,open('retry.json','w'))
