import json, time, math, urllib.request, urllib.parse, sys
sys.path.insert(0,'.')
from places import P
def d(a,b):
    R=6371000;t=math.radians
    h=math.sin(t(b[0]-a[0])/2)**2+math.cos(t(a[0]))*math.cos(t(b[0]))*math.sin(t(b[1]-a[1])/2)**2
    return 2*R*math.asin(math.sqrt(h))
C=(52.9533,-1.1500)
out={}
try: out=json.load(open('geo.json'))
except: pass
for p in P:
    if p['name'] in out: continue
    url="https://nominatim.openstreetmap.org/search?"+urllib.parse.urlencode({"q":p['geo'],"format":"json","limit":3,"viewbox":"-1.30,53.02,-1.05,52.88","bounded":1})
    req=urllib.request.Request(url,headers={"User-Agent":"nottingham-guide-builder/1.0"})
    try: r=json.load(urllib.request.urlopen(req,timeout=20))
    except Exception as e: r=[]; print("ERR",p['name'],e)
    out[p['name']]=[(float(x['lat']),float(x['lon']),x.get('class'),x.get('type'),x.get('display_name','')[:70]) for x in r]
    time.sleep(1.1)
json.dump(out,open('geo.json','w'),indent=0)
for p in P:
    r=out[p['name']]; ll=p['ll']
    if r:
        g=r[0]; dd=d(ll,g[:2]) if ll else -1
        print(f"{p['name'][:34]:34} {g[2]}/{g[3]:12} {'%5d'%dd}m  {g[4]}")
    else: print(f"{p['name'][:34]:34} NONE  ll={ll}")
