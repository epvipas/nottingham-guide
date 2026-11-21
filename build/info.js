// ---------- info ----------
function iref(id, label) { const it = ITEMS.find(x => x.id === id); return `<button class="linkchip" data-goto="${id}" style="color:${CATS[it.cat].color}">${CATS[it.cat].emoji} ${esc(label || it.name)}</button>`; }
function byName(n) { const it = ITEMS.find(x => x.name === n); if (!it) throw new Error('No place called ' + n); return it.id; }
function refs(names) { return names.map(n => iref(byName(n))).join(' '); }
function renderCaves() {
  const stops = [
    ['City of Caves', 'Start in daylight with the guided tour under the old Broadmarsh. Tours take about an hour.'],
    ['Ye Olde Trip to Jerusalem', 'England\'s self-styled oldest inn, with drinking rooms cut into Castle Rock. Ten minutes\' walk west.'],
    ['Malt Cross', 'Victorian music hall with caves below. Ask if you can see them.'],
    ['The Bell Inn', 'Timber-framed pub on the Market Square with medieval cellars in the rock.'],
    ['Hand & Heart', 'Up Derby Road: the back room is carved into the cliff.'],
    ['The Organ Grinder', 'Finish at Canning Circus with a Blue Monkey pint and a pork pie.'],
  ];
  $('#caveTrail').innerHTML = '<ol>' + stops.map(([n, t]) => `<li style="margin-bottom:8px">${iref(byName(n))}<br>${esc(t)}</li>`).join('') + '</ol>';
}
function renderInfo() {
  const hq = { q: 'Council House, Old Market Square, Nottingham', name: 'Council House Nottingham', ta: true };
  $('#v-info').innerHTML = `
  <div class="hero"><img src="img/cover.svg" alt=""><div class="cap"><span style="color:#FFD23F;font-size:11px;font-weight:800;letter-spacing:2px">YOUR BASE</span><br><b>Old Market Square</b><br><span style="font-size:13px">"Meet you by the left lion": the stone lions in front of the Council House. Walking times in the guide are from here.</span></div></div>
  <div class="sec"><h2>🚗 Getting in from an hour away</h2>
   <img src="img/transit.svg" alt="" style="width:100%;border-radius:12px;aspect-ratio:16/7;object-fit:cover">
   <div class="opt" style="border-color:#1F5C45"><h4 style="background:#1F5C45"><span>🚋 Tram Park &amp; Ride</span><span>free parking · ≈ £5.70 day</span></h4><ol>
    <li>The easiest option. Park at a tram Park &amp; Ride: <b>Phoenix Park</b> (M1 J26), <b>Toton Lane</b> (M1 J25), <b>Clifton South</b> (A453, from M1 J24) or <b>Hucknall</b> (from the north).</li>
    <li>Parking is free if you hold a valid tram ticket from the moment you park. An adult day ticket is about £5.65–5.80 in 2026; tapping in with contactless caps the fare for you.</li>
    <li>Get off at <b>Old Market Square</b> for the centre, <b>Lace Market</b> for Hockley and the galleries, or <b>Nottingham Station</b> for Hopkinsons and the canal.</li></ol></div>
   <div class="opt" style="border-color:#C9A227"><h4 style="background:#C9A227"><span>🅿️ Driving into the centre</span><span>pricier · slower</span></h4><ol>
    <li>Good multi-storeys for this guide: <b>Victoria Centre</b> (Hockley side), <b>Trinity Square</b> (north), and the <b>Broad Marsh</b> car park by the bus station (south, near the Lace Market and caves).</li>
    <li>Saturday afternoons and December get very busy. The Workplace Parking Levy applies to employers, not visitors.</li></ol></div>
   <div class="opt" style="border-color:#1877D0"><h4 style="background:#1877D0"><span>🚆 By train</span><span>10 min walk to the Square</span></h4><ol>
    <li>Nottingham station is south of the centre. Walk up Carrington Street, or take the tram from the bridge over the platforms.</li>
    <li>Hopkinsons vintage emporium and the Vat &amp; Fiddle are right by the station, for the first or last stop of the day.</li></ol></div>
   ${actions(hq, true)}
  </div>
  <div class="sec"><h2>🗓️ Three easy days</h2>
   <div class="day" style="background:#FDE3DF"><b>Day 1 · Hockley &amp; the Lace Market:</b> ${refs(['Paul Smith, Willoughby House', 'Nottingham Contemporary', 'Lace Market & St Mary\'s Church', 'Fletcher Gate Fine Art', 'Delilah Fine Foods', 'Rough Trade Nottingham', 'Goose Gate vintage & Hockley shops', 'Broadway Cinema', 'Ibérico World Tapas'])}</div>
   <div class="day" style="background:#DDEBFA"><b>Day 2 · Arcades, books &amp; caves:</b> ${refs(['Flying Horse Walk', 'Page 45', 'Five Leaves Bookshop', 'Hurts Yard', 'Rob\'s Records', 'Kushi-ya', 'City of Caves', 'Ye Olde Trip to Jerusalem', 'Hart\'s Kitchen'])}</div>
   <div class="day" style="background:#EFE2F8"><b>Day 3 · Makers &amp; artist-run galleries (best on a Saturday):</b> ${refs(['Sneinton Market Avenues', 'Surface Gallery', 'BACKLIT', 'Bustler Market', 'Fox & Grapes', 'New Art Exchange', 'Derby Road antiques & vintage strip', 'The Organ Grinder', 'Alchemilla'])}</div>
  </div>
  <div class="sec"><h2>🌙 Evenings by budget</h2>
   <div class="day" style="background:#D8F3EE"><b>£ Cheap &amp; cheerful:</b> ${refs(['Bustler Market', 'Kayal', 'Shanghai Shanghai', 'The Angel Microbrewery'])}</div>
   <div class="day" style="background:#FDEFD6"><b>££ Small plates &amp; good drinks:</b> ${refs(['Kushi-ya', 'Bar Gigi', 'Sexy Mamma Love Spaghetti', 'Junkyard', 'The Canal House'])}</div>
   <div class="day" style="background:#EFE2F8"><b>££££ The big night:</b> ${refs(['Alchemilla', 'Restaurant Sat Bains', 'Hart\'s Kitchen', 'The Hockley Arts Club'])}
    <p style="margin:8px 0 0;font-size:13px">Sat Bains is a restaurant with rooms: stay over and skip the drive home.</p></div>
  </div>
  <div class="sec"><h2>🎄 What's on this winter</h2><ul>
   <li><b>Winter Wonderland</b> in Old Market Square, 12 November to 31 December 2026: Christmas market stalls until 24 December, plus an ice rink, Observation Wheel and Ice Bar. Entry is free and the rides are ticketed.</li>
   <li><b>Panto</b> at the Theatre Royal runs through December and into January, so book ahead.</li>
   <li>Later in the year: <b>Goose Fair</b> (one of England's oldest travelling fairs, early October) and <b>Hockley Hustle</b> (a one-day music festival across Hockley's venues, October).</li>
   <li>For gigs, exhibitions and new openings, check <a href="https://leftlion.co.uk" target="_blank" rel="noopener">LeftLion</a>, the city's culture magazine.</li></ul></div>
  <div class="sec"><h2>🏘️ Neighbourhoods</h2><ul>
   <li><b>Hockley:</b> red-brick streets of record shops, vintage, cafés and cocktail bars around Goose Gate, Carlton Street and Broad Street. The indie heartland, 5 minutes east of the Square.</li>
   <li><b>Lace Market:</b> tall Victorian lace warehouses around St Mary's church, with Nottingham Contemporary, the Shire Hall and quiet streets to wander.</li>
   <li><b>Around the Square:</b> the jitties (alleys) and arcades off the Old Market Square: Hurts Yard, Flying Horse Walk, Bridlesmith Walk, Long Row and the Exchange Arcade.</li>
   <li><b>Castle &amp; The Park:</b> Castle Rock, the Trip to Jerusalem, the canal, and the private Victorian estate of grand villas reached through the Park Tunnel.</li>
   <li><b>Derby Road &amp; Canning Circus:</b> antiques and vintage climbing west to three good pubs, with Alchemilla at the top.</li>
   <li><b>Sneinton:</b> Sneinton Market's makers' units, Bustler street food, Surface Gallery, BACKLIT and Green's Windmill, 10 minutes east of Hockley.</li>
  </ul></div>
  <div class="sec"><h2>🗣️ Speak Nottingham</h2><div class="gloss">
   <div><b>Ay up, me duck</b>: hello, said to everyone</div><div><b>Mardy</b>: grumpy, sulky</div>
   <div><b>Jitty</b>: a narrow alley between buildings. Plenty of the best shops are down one</div><div><b>Cob</b>: a bread roll</div>
   <div><b>Gizza</b>: give me ("gizza cob")</div><div><b>Gooz Fair</b>: Goose Fair, the October fair</div>
   <div><b>Left lion</b>: the Council House lion everyone meets by</div><div><b>Notts</b>: Nottingham or Nottinghamshire</div></div></div>
  <div class="sec"><h2>🕐 Opening hours</h2><ul>
   <li><b>Mondays</b> are the quiet day: many independent restaurants, Nottingham Contemporary and several galleries close, and some restaurants close on Tuesdays too.</li>
   <li><b>Saturdays</b> are best for Sneinton Market and the small shops. Sundays are shorter, usually about 10:00 or 11:00 to 16:00.</li>
   <li>The small artist-run galleries (Surface, BACKLIT, Primary, Hooten Street) open mainly while a show is on, so check before you go.</li>
   <li>Book Friday and Saturday dinners ahead, and the Michelin restaurants weeks ahead.</li></ul></div>
  <div class="sec"><h2>⚠️ Before you go</h2><ul>
   <li>Independent places come and go quickly. Check each venue's own site or socials the day before.</li>
   <li><b>Recently closed:</b> The Larder on Goosegate, Boilermaker (the site is now Boca Lima), Petit Paris, Chino Latino and Long Row Social have all closed, so they're not in the guide.</li>
   <li>Listings conflicted for <b>Annie's Burger Shack</b> and <b>Cow Vintage</b>. Check they're trading before you plan around them.</li>
   <li>Sneinton Market's hall is due for refurbishment from autumn 2026, so some units may be shut.</li>
   <li>Map pins come from OpenStreetMap and are close but not exact; use the Directions buttons for door-to-door routes.</li>
   <li>Information was checked in November 2026. The illustrations are original artwork drawn for this guide.</li></ul>
   <button class="btn b-map" id="installAgain" style="width:100%;margin-top:8px">📲 Install this guide on your phone</button></div>
  <div class="sec"><h2>🔄 Updates</h2><p>The guide checks for new content whenever you're online. If something looks out of date, tap below to clear the saved copy and reload.</p>
  <button class="iconbtn" id="refreshBtn" style="padding:10px 14px;box-shadow:0 1px 5px rgba(0,0,0,.2)">Refresh guide</button></div>`;
}
