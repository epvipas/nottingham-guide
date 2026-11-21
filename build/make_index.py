import re
s = open('index.src.html').read()
def R(a, b, count=1):
    global s
    assert a in s, "MISSING: " + a[:70]
    s = s.replace(a, b) if count == 0 else s.replace(a, b, count)

# ---- head / branding ----
R('<title>Málaga Guide</title>', '<title>Nottingham Guide</title>')
R('content="Sights, museums, galleries, shops, cafés, tapas, restaurants and bars in Málaga, with maps, reviews and directions."',
  'content="Independent Nottingham: places to eat and drink, quirky shops, vintage, records and small galleries, with maps, reviews and directions."')
R('<meta name="theme-color" content="#E8483B">', '<meta name="theme-color" content="#1F5C45">')
R('content="Málaga">', 'content="Nottingham">')
R('--red:#E8483B;', '--red:#1F5C45;')
R('--bg:#FFFBF4;', '--bg:#F6F5F0;')
R('background:linear-gradient(110deg,#FF6B6B,#FF9A3C 55%,#FFD23F)', 'background:linear-gradient(110deg,#174A37,#2E7D5B 55%,#C9A227)')
R('text-shadow:0 2px 0 rgba(192,57,43,.6)', 'text-shadow:0 2px 0 rgba(10,40,28,.6)')
R('<h1>Málaga</h1><small>Sights · Art · Shops · Eat · Drink · Out</small>', '<h1>Nottingham</h1><small>Eat · Drink · Indie shops · Vintage · Galleries</small>')
R('.fact{background:#FFF8E1;', '.fact{background:#EEF5F0;')
R('.meta span{background:#F3EFE7;', '.meta span{background:#ECEEE8;')

# ---- sort labels ----
R('<option value="walk">Closest to hotel</option><option value="name">A–Z</option><option value="me">Closest to me</option></select></div>\n  <div class="grid" id="list-see">',
  '<option value="walk">Closest to Market Square</option><option value="name">A–Z</option><option value="me">Closest to me</option></select></div>\n  <div class="grid" id="list-see">')
R('<option value="walk">Closest to hotel</option><option value="price">', '<option value="walk">Closest to Market Square</option><option value="price">')

# ---- history + caves views ----
a = s.index(' <section class="view" id="v-history">'); b = s.index(' <section class="view" id="v-info"></section>')
s = s[:a] + open('build/views.html').read() + s[b:]

# ---- tabs ----
R(' <button data-v="vermouth"><span class="ic">🥂</span>Vermouth</button>', ' <button data-v="caves"><span class="ic">🍺</span>Caves &amp; pubs</button>')
R('<div class="t"><b>Install the Málaga guide</b>', '<div class="t"><b>Install the Nottingham guide</b>')

# ---- script ----
R('const G = window.GUIDE, CATS = G.cats, ITEMS = G.items, HOTEL = G.hotel;', 'const G = window.GUIDE, CATS = G.cats, ITEMS = G.items, HOTEL = G.base;')
R("enc(it.name + ' Malaga')", "enc(it.name + ' Nottingham')")
R("'€'.repeat(it.price)", "'£'.repeat(it.price)", 0)
R("'€'.repeat(p)", "'£'.repeat(p)")
R("<span>🚶 ${it.walk} min from hotel</span>", "<span>🚶 ${it.walk} min from the Square</span>")
R("${it.far ? '<span>🚕 outside centre</span>' : ''}", "${it.far ? '<span>🚋 tram, bus or car</span>' : ''}")
R("🚶 ${it.walk} min from hotel<br>", "🚶 ${it.walk} min from the Square<br>")
R("setView([36.7205, -4.4215], 15)", "setView([52.9525, -1.1480], 15)")
R("""const hi = L.divIcon({ className: '', html: '<div class="pin hotel">H</div>'""", """const hi = L.divIcon({ className: '', html: '<div class="pin hotel">★</div>'""")
R(".bindPopup(`<div class=\"pop\"><h4>🏨 ${esc(HOTEL.name)}</h4><div class=\"addr\">${esc(HOTEL.addr)}</div>${actions({q: HOTEL.name + ', Calle Mármoles 6, Málaga', name: HOTEL.name, ta: true}, true)}</div>`);",
  ".bindPopup(`<div class=\"pop\"><h4>🦁 ${esc(HOTEL.name)}</h4><div class=\"addr\">${esc(HOTEL.addr)}<br>Distances in the guide are walking minutes from here.</div>${actions({q: 'Council House, Old Market Square, Nottingham', name: 'Council House Nottingham', ta: true}, true)}</div>`);")
R("'Located: you\\'re not in Málaga yet!'", "'Located: you\\'re not in Nottingham yet!'")
R("k !== 'malaga-tiles'", "k !== 'nottingham-tiles'")

# replace renderInfo + coffee
a = s.index('// ---------- info ----------'); b = s.index('// ---------- navigation ----------')
s = s[:a] + open('build/info.js').read() + '\n' + s[b:]

R("go(['explore', 'eat', 'map', 'saved', 'info'].includes(startV) ? startV : 'explore');",
  "go(['explore', 'history', 'eat', 'caves', 'map', 'saved', 'info'].includes(startV) ? startV : 'explore');")
R("['explore','history','eat','vermouth','map','saved','info']", "['explore','history','eat','caves','map','saved','info']")
R("renderInfo(); renderAll();", "renderInfo(); renderCaves(); renderAll();")
assert 'Málaga' not in s and 'malaga' not in s.lower().replace('malaga-guide',''), [m.start() for m in re.finditer('álaga|alaga', s)]
open('index.html', 'w').write(s)
print('ok', len(s))
